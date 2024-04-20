import os

import pandas as pd
from flask import Flask, jsonify, request
from flask_cors import cross_origin
from sklearn.cluster import KMeans, MeanShift, estimate_bandwidth, SpectralClustering, AgglomerativeClustering, DBSCAN, \
    OPTICS
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

root_data = './data'
def get_name_score(filename):
    """
    一个工具函数，得到姓名和分数
    :param filename:
    :return:
    """
    df = pd.read_excel(filename)
    df.fillna(0, inplace=True)
    res = []
    for i in range(len(df)):
        res.append({"name": df.iloc[i]['姓名'], "value": int(df.iloc[i]['分数'])})
    return res


def merge_DataFrame(filename: str, df):
    """
    工具函数，将小组评分合并到df中
    :param filename:
    :param df:
    :return:
    """
    temp_df = pd.read_excel(filename)
    temp_df.fillna(0, inplace=True)
    series_name = filename.split(os.sep)[-1].split('.')[0][:-1]
    df[series_name] = pd.Series()
    for i in temp_df.index:
        name = temp_df.iloc[i]["姓名"]
        score = temp_df.iloc[i]["分数"]
        name = name.strip()
        try:
            match_index = df.loc[df['姓名'] == name].index[0]
        except IndexError:
            continue
        df.at[match_index, series_name] = int(score)
    return df


def process_data(df: pd.DataFrame):
    """
    对数据进行最大最小化处理
    :param df:
    :return:
    """
    scaler = StandardScaler()
    scaler_data = scaler.fit_transform(df)
    return scaler_data


def cluster_kmeans(df: pd.DataFrame, k=3):
    """
    工具函数，进行Kmeans聚类分析，返回聚类的结果,包括标签和评价指标
    :param df:
    :param k:
    :return:
    """
    scaler_data = process_data(df)
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(scaler_data)
    label = kmeans.labels_
    sil_score = silhouette_score(scaler_data, label)
    return label, sil_score


def cluster_mean_shift(df: pd.DataFrame):
    scaler_data = process_data(df)
    bandwidth = estimate_bandwidth(scaler_data, quantile=0.2, n_samples=500)
    model = MeanShift(bandwidth=bandwidth, bin_seeding=True)
    model.fit(scaler_data)
    labels = model.labels_
    sil_score = silhouette_score(scaler_data, labels)
    return labels, sil_score, bandwidth


def cluster_spectral_cluster(df: pd.DataFrame, cluster: int):
    scaler_data = process_data(df)
    model = SpectralClustering(n_clusters=cluster)
    model.fit(scaler_data)
    labels = model.labels_
    sil_score = silhouette_score(scaler_data, labels)
    return labels, sil_score


def cluster_agglomerative_cluster(df: pd.DataFrame, cluster):
    scaler_data = process_data(df)
    model = AgglomerativeClustering(n_clusters=cluster)
    model.fit(scaler_data)
    labels = model.labels_
    sil_score = silhouette_score(scaler_data, labels)
    return labels, sil_score


def cluster_dbscan(df: pd.DataFrame, min_samples: int):
    scaler_data = process_data(df)
    model = DBSCAN(eps=0.5, min_samples=min_samples)
    model.fit(scaler_data)
    labels = model.labels_
    sil_score = silhouette_score(scaler_data, labels)
    return labels, sil_score


def cluster_optics(df: pd.DataFrame, min_samples: int):
    scaler_data = process_data(df)
    model = OPTICS(eps=0.5, min_samples=min_samples)
    model.fit(scaler_data)
    labels = model.labels_
    sil_score = silhouette_score(scaler_data, labels)
    return labels, sil_score


def get_student_summary():
    """
    工具函数，得到学生的综合信息
    Index(['学号', '姓名', '性别', '班级', '课堂表现记录', '自评', '第一次组员打分', '第一次组长打分', '第二次组员打分',
       '第二次组长打分'],
    :return:
    """
    df = pd.DataFrame()
    df0 = pd.read_excel(os.path.join(os.getcwd(), "data", "2022数据分析与处理技术课程综课堂表现记录名单.xlsx"))
    df0.fillna(0, inplace=True)
    df['学号'] = df0['学号']
    df['姓名'] = df0['姓名'].map(lambda x: x.strip())
    df['性别'] = df0['性别']
    df['班级'] = df0['班级']
    df['课堂表现记录'] = df0.iloc[:, 4:].sum(axis=1)

    df1 = pd.read_excel(os.path.join(os.getcwd(), "data", "2022数据分析与处理技术课程自评.xlsx"))
    df1.fillna(0, inplace=True)
    df['自评'] = df1.iloc[:, 5:].sum(axis=1)

    filenames = ["第一次组员打分表.xlsx", "第一次组长打分表.xlsx", "第二次组员打分表.xlsx", "第二次组长打分表.xlsx"]
    for filename in filenames:
        df = merge_DataFrame(os.path.join(os.getcwd(), "data", filename), df)
    df = df.fillna(0)
    return df


def get_result_from_df(df: pd.DataFrame):
    """
    将结果包装成json数据
    :param df:
    :return:
    """
    columns = df.columns.tolist()
    result = []
    for i in range(len(df)):
        dic = {}
        for column in columns:
            if df[column].dtype == 'object':
                dic[column] = str(df.iloc[i][column])
            else:
                dic[column] = int(df.iloc[i][column])
        result.append(dic)
    return result


@app.route('/getStudentCluster')
@cross_origin()
def get_student_cluster():
    """
    对学生进行聚类分析
    :return:
    """
    method = request.args.get("method", "Kmeans")
    cluster = int(request.args.get("cluster", 3))
    df = get_student_summary()
    if method == "Kmeans":
        label, sil_score = cluster_kmeans(df.iloc[:, 4:], cluster)
        df['label'] = label
        return jsonify({"data": get_result_from_df(df), "score": sil_score, "cluster": cluster})
    elif method == 'Spectral clustering':
        label, sil_score = cluster_spectral_cluster(df.iloc[:, 4:], cluster)
        df['label'] = label
        return jsonify({"data": get_result_from_df(df), "score": sil_score, "cluster": cluster})
    elif method == '层次聚类':
        label, sil_score = cluster_agglomerative_cluster(df.iloc[:, 4:], cluster)
        df['label'] = label
        return jsonify({"data": get_result_from_df(df), "score": sil_score, "cluster": cluster})


@app.route('/getStudentGrade')
@cross_origin()
def getStudentGrade():
    """
    得到学生成绩
    :return:
    """
    df = pd.read_excel(os.path.join(root_data, '2022数据分析与处理技术课程据-成绩计算.xlsx'), sheet_name="最终成绩计算")
    df = df.drop(['序号', '期中'], axis=1)
    data = df.to_dict(orient='records')
    columns = list(df.columns)[1:]
    return jsonify({"columns": columns, "data": data})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
