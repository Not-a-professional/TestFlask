from flask import Flask
from flask import jsonify
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/test_template')
def test_template():
    return render_template('index.html')


@app.route('/test_ajax', methods=['POST'])
def test_ajax():
    data = request.get_json()
    print('name:' + data['name'] + "age:" + str(data['age']))
    return jsonify('成功')


if __name__ == '__main__':
    app.run()  # 修改监听host和port需要在控制台输入命令：flask run -h 127.0.0.1 -p 8888执行
