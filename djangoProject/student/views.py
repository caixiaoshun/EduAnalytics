import os.path

from django.http import JsonResponse
from djangoProject import settings
import pandas as pd


# Create your views here.
def getAllStudents(request):
    """
    得到所有学生信息
    :param request:
    :return:
    """
    df = pd.read_sql("student", con=settings.engine)
    ids = df['id'].tolist()
    student_ids = df['student_id'].tolist()
    student_names = df['name'].tolist()
    student_gender = df['gender'].tolist()
    student_class = df['class_name'].tolist()
    res = []
    for s_id, student_id, student_name, student_gender, student_class in zip(ids, student_ids, student_names,
                                                                             student_gender, student_class):
        res.append({"id": s_id, "student_id": student_id, "name": student_name, "gender": student_gender,
                    "class_name": student_class})
    return JsonResponse(res, safe=False)


def getGender(request):
    """
    得到学生中男女数量
    :param request:
    :return:
    """
    df = pd.read_sql("student", con=settings.engine)['gender'].value_counts().to_dict()
    male = df['男']
    female = df['女']
    return JsonResponse({"male": male, "female": female}, safe=False)


def getComposition(request):
    """
    得到班级组成
    :param request:
    :return:
    """
    df = pd.read_sql("student", con=settings.engine)
    ids = df['id'].tolist()
    student_ids = df['student_id'].tolist()
    student_names = df['name'].tolist()
    student_gender = df['gender'].tolist()
    student_class = df['class_name'].tolist()

    student_all = []
    for s_id, student_id, student_name, student_gender, student_class in zip(ids, student_ids, student_names,
                                                                             student_gender, student_class):
        student_all.append({"id": s_id, "student_id": student_id, "name": student_name, "gender": student_gender,
                            "class_name": student_class})

    result = {}
    for student in student_all:
        if student["class_name"] not in result:
            result[student["class_name"]] = []

        result[student["class_name"]].append(
            {"姓名": student["name"], "学号": student["student_id"], "性别": student["gender"]})
    return JsonResponse(result, safe=False)


def getSelfAssessment(request):
    """
    得到自评分数
    :param request:
    :return:
    """
    df = pd.read_sql("select * from student_self_assessment", con=settings.engine)
    df['total'] = df['self_assessment_1'] + df['self_assessment_2'] + df['self_assessment_3'] + df[
        'self_assessment_4'] + df['self_assessment_5'] + df['self_assessment_6'] + df['self_assessment_7']
    df = df.astype("str")
    names = df['name'].tolist()
    score1 = df['self_assessment_1'].tolist()
    score2 = df['self_assessment_2'].tolist()
    score3 = df['self_assessment_3'].tolist()
    score4 = df['self_assessment_4'].tolist()
    score5 = df['self_assessment_5'].tolist()
    score6 = df['self_assessment_6'].tolist()
    score7 = df['self_assessment_7'].tolist()
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
    return JsonResponse(res, safe=False)


def getStudentInformation(request):
    df = pd.read_sql("select * from student", con=settings.engine)
    class_names = df['class_name'].tolist()
    res = {'class_name': {}, 'gender': {}}
    for class_name in class_names:
        count = df.loc[df['class_name'] == class_name].shape[0]
        res['class_name'][class_name] = count
    res['gender']['男'] = df.loc[df['gender'] == '男'].shape[0]
    res['gender']['女'] = df.loc[df['gender'] == '女'].shape[0]
    res['total'] = len(df)
    return JsonResponse(res, safe=False)


def getStudentPerformer(request):
    df = pd.read_excel(
        os.path.join(os.getcwd(), "student", "data", "2022数据分析与处理技术课程综课堂表现记录名单.xlsx"))
    df.fillna(0, inplace=True)

    # yAxis = df['姓名'].to_list()
    # xAxis = df.columns.tolist()[4:]
    data = []
    for i in range(len(df)):
        for j in range(1, 17):
            key = f"第{j}课"
            data.append([df.iloc[i]['姓名'], key, df.iloc[i][key]])
            # data.append({"name":df.iloc[i]['姓名'],"score":df.iloc[i][key],"week":key})
    return JsonResponse({"data": data}, safe=False)
