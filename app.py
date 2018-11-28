from flask import Flask
from flask import jsonify
from flask import render_template
from flask import request

import os

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


@app.route('/health')
def health():
    return jsonify({"status": "up"})


@app.route("/getUser")
def get_user():
    return jsonify({'username': 'python', 'password': 'python'})


@app.route("/crawler")
def crawler():
    os.chdir('./SCRAPY/SCRAPY') # 必须切换目录，不然爬虫跑不起来
    print(os.getcwd())
    os.system('scrapy runspider CrawlSpider.py -o top-stackoverflow-questions.json')  # 执行命令，让爬虫启动


if __name__ == '__main__':
    app.run(port=5678)
