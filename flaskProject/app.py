import os

import pandas as pd
from flask import Flask, jsonify
from flask_cors import cross_origin

app = Flask(__name__)


@app.route('/getAllStudents')
@cross_origin()
def get_all_students():
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
    total = df.iloc[:,5:]
    df['total'] = total.sum(axis=1)
    df = df.astype("str")
    names = df['姓名'].tolist()
    score1 = df['自评1'].tolist()
    score2 = df['自评2'].tolist()
    score3 = df['自评3'].tolist()
    score4 = df['自评4'].tolist()
    score5 = df['自评5'].tolist()
    score6 = df['自评6'].tolist()
    score7 = df['自评7'].tolist()
    total = df['total'].tolist()
    res = [
        {"cdate": "自评1", "name": names, "scores": score1},
        {"cdate": "自评2", "name": names, "scores": score2},
        {"cdate": "自评3", "name": names, "scores": score3},
        {"cdate": "自评4", "name": names, "scores": score4},
        {"cdate": "自评5", "name": names, "scores": score5},
        {"cdate": "自评6", "name": names, "scores": score6},
        {"cdate": "自评7", "name": names, "scores": score7},
        {"cdate": "总分", "name": names, "scores": total},
    ]
    return jsonify(res)


if __name__ == '__main__':
    app.run()
