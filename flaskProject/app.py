import os

import pandas as pd
from flask import Flask, jsonify, request
from flask_cors import cross_origin
from sklearn.cluster import KMeans, MeanShift, estimate_bandwidth, SpectralClustering, AgglomerativeClustering, DBSCAN, \
    OPTICS
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)


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

def cluster_dbscan(df: pd.DataFrame,min_samples:int):
    scaler_data = process_data(df)
    model = DBSCAN(eps=0.5, min_samples=min_samples)
    model.fit(scaler_data)
    labels = model.labels_
    sil_score = silhouette_score(scaler_data, labels)
    return labels, sil_score
def cluster_optics(df: pd.DataFrame,min_samples:int):
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


@app.route('/getAllStudents')
@cross_origin()
def get_all_students():
    """
    得到所有学生的信息
    :return:
    """
    df = pd.read_excel(os.path.join(os.getcwd(), 'data', '2022数据分析与处理技术课程综课堂表现记录名单.xlsx'))
    data = []
    for i in range(len(df)):
        data.append(
            {"student_id": str(df.iloc[i]['学号']), "name": df.iloc[i]['姓名'], "gender": df.iloc[i]['性别'],
             "class_name": df.iloc[i]['班级']})
    return jsonify(data)


@app.route('/getGender')
@cross_origin()
def get_gender():
    """
    得到性别比例
    :return:
    """
    df = pd.read_excel(os.path.join(os.getcwd(), 'data', '2022数据分析与处理技术课程综课堂表现记录名单.xlsx'))
    male = len(df[df['性别'] == '男'])
    female = len(df[df['性别'] == '女'])
    return jsonify({"male": male, "female": female})


@app.route('/getComposition')
@cross_origin()
def get_composition():
    """
    得到班级组成
    :param request:
    :return:
    """
    df = pd.read_excel(os.path.join(os.getcwd(), 'data', '2022数据分析与处理技术课程综课堂表现记录名单.xlsx'))
    student_ids = df['学号'].tolist()
    student_names = df['姓名'].tolist()
    student_gender = df['性别'].tolist()
    student_class = df['班级'].tolist()

    student_all = []
    for student_id, student_name, student_gender, student_class in zip(student_ids, student_names,
                                                                       student_gender, student_class):
        student_all.append({"student_id": student_id, "name": student_name, "gender": student_gender,
                            "class_name": student_class})

    result = {}
    for student in student_all:
        if student["class_name"] not in result:
            result[student["class_name"]] = []

        result[student["class_name"]].append(
            {"姓名": student["name"], "学号": student["student_id"], "性别": student["gender"]})
    return jsonify(result)


@app.route('/getStudentInformation')
@cross_origin()
def get_student_information():
    """
    学生表综述
    :return:
    """
    df = pd.read_excel(os.path.join(os.getcwd(), 'data', '2022数据分析与处理技术课程综课堂表现记录名单.xlsx'))
    class_names = df['班级'].tolist()
    res = {'class_name': {}, 'gender': {}}
    for class_name in class_names:
        count = df.loc[df['班级'] == class_name].shape[0]
        res['class_name'][class_name] = count
    res['gender']['男'] = df.loc[df['性别'] == '男'].shape[0]
    res['gender']['女'] = df.loc[df['性别'] == '女'].shape[0]
    res['total'] = len(df)
    return jsonify(res)


@app.route('/getStudentPerformer')
@cross_origin()
def get_student_performance():
    """
    得到学生自我评价信息
    :return:
    """
    df = pd.read_excel(os.path.join(os.getcwd(), 'data', '2022数据分析与处理技术课程综课堂表现记录名单.xlsx'))
    df.fillna(0, inplace=True)
    data = []
    for i in range(len(df)):
        for j in range(1, 17):
            key = f"第{j}课"
            data.append([df.iloc[i]['姓名'], key, df.iloc[i][key]])
    return jsonify({"data": data})


@app.route('/getSelfAssessment')
@cross_origin()
def get_self_assessment():
    """
    得到自评分数
    :return:
    """
    df = pd.read_excel(os.path.join(os.getcwd(), 'data', '2022数据分析与处理技术课程自评.xlsx'))
    df.fillna(0, inplace=True)
    total = df.iloc[:, 5:]
    df['总分'] = total.sum(axis=1)
    df = df.astype("str")
    scores_key = df.columns.tolist()[5:]
    names = df['姓名'].tolist()
    scores_list = []
    res = []
    for score_key in scores_key:
        scores_list.append(df[score_key].tolist())
        res.append({"cdate": score_key, "name": names, "scores": df[score_key].tolist()})
    return jsonify(res)


@app.route('/getFirstLeaderScore')
@cross_origin()
def get_first_leader_score():
    """
    第一次组长打分数据
    :return:
    """
    filename = os.path.join(os.getcwd(), 'data', '第一次组长打分表.xlsx')
    result = get_name_score(filename)
    return jsonify({"data": result})


@app.route('/getSecondLeaderScore')
@cross_origin()
def get_second_leader_score():
    """
    第一次组长打分数据
    :return:
    """
    filename = os.path.join(os.getcwd(), 'data', '第二次组长打分表.xlsx')
    result = get_name_score(filename)
    return jsonify({"data": result})


@app.route('/getFirstMemberScore')
@cross_origin()
def get_first_member_score():
    """
    第一次组员打分数据
    :return:
    """
    filename = os.path.join(os.getcwd(), 'data', '第一次组员打分表.xlsx')
    result = get_name_score(filename)
    return jsonify({"data": result})


@app.route('/getSecondMemberScore')
@cross_origin()
def get_second_member_score():
    """
    第一次组长打分数据
    :return:
    """
    filename = os.path.join(os.getcwd(), 'data', '第二次组员打分表.xlsx')
    result = get_name_score(filename)
    return jsonify({"data": result})


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
    elif method == "Mean Shift":
        label, sil_score, bandwidth = cluster_mean_shift(df.iloc[:, 4:])
        df['label'] = label
        cluster = len(set(label))
        return jsonify({"data": get_result_from_df(df), "score": sil_score, "cluster": cluster, "bandwidth": bandwidth})
    elif method == 'Spectral clustering':
        label, sil_score = cluster_spectral_cluster(df.iloc[:, 4:], cluster)
        df['label'] = label
        return jsonify({"data": get_result_from_df(df), "score": sil_score, "cluster": cluster})
    elif method == '层次聚类':
        label, sil_score = cluster_agglomerative_cluster(df.iloc[:, 4:], cluster)
        df['label'] = label
        return jsonify({"data": get_result_from_df(df), "score": sil_score, "cluster": cluster})
    elif method == 'DBSCAN':
        min_samples = int(request.args.get('min_samples',4))
        label, sil_score = cluster_dbscan(df.iloc[:, 4:], min_samples)
        df['label'] = label
        cluster = len(set(label))
        return jsonify({"data": get_result_from_df(df), "score": sil_score, "cluster": cluster})
    elif method == 'OPTICS':
        min_samples = int(request.args.get('min_samples', 4))
        label, sil_score = cluster_optics(df.iloc[:, 4:], min_samples)
        df['label'] = label
        cluster = len(set(label))
        return jsonify({"data": get_result_from_df(df), "score": sil_score, "cluster": cluster})


if __name__ == '__main__':
    app.run()
