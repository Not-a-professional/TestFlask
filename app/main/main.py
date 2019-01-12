from flask import jsonify
from flask import render_template
from flask import request
from app.main import main


@main.route('/')
def hello_world():
    return 'Hello World!'


@main.route('/test_template')
def test_template():
    return render_template('index.html')


# post、delete、put请求
# 参数获取方式：request.get_json()
# get请求
# 参数获取方式：request.args
@main.route('/test_ajax', methods=['POST'])
def test_ajax():
    data = request.get_json()
    print('name:' + data['name'] + "age:" + str(data['age']))
    return jsonify('成功')


@main.route('/health')
def health():
    return jsonify({"status": "up"})


@main.route("/getUser")
def get_user():
    return jsonify({'username': 'python', 'password': 'python'})

