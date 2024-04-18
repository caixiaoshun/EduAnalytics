from flask import Flask,jsonify
from flask_cors import CORS
import pandas as pd
import os

app = Flask(__name__)
CORS(app)

root_data = './data/'


@app.route('/getStudentGrade')
def getStudentGrade():
    """
    得到学生成绩
    :return:
    """
    df = pd.read_excel(os.path.join(root_data, '2022数据分析与处理技术课程据-成绩计算.xlsx'), sheet_name="最终成绩计算")
    df = df.drop(['序号', '期中'], axis=1)
    data = df.to_dict(orient='records')
    columns = list(df.columns)[1:]
    return jsonify({"columns":columns,"data":data})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
