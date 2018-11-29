import json

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

# post、delete、put请求
# 参数获取方式：request.get_json()
# get请求
# 参数获取方式：request.args
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
    # os.chdir('./SCRAPY/SCRAPY') # 必须切换目录，不然爬虫跑不起来
    # print(os.getcwd())
    os.system('scrapy runspider ./SCRAPY/SCRAPY/CrawlSpider.py -o top-stackoverflow-questions.json')  # 执行命令，让爬虫启动
    if os.path.exists('./SCRAPY/SCRAPY/top-stackoverflow-questions.json'):
        try:
            file = open('t./SCRAPY/SCRAPY/op-stackoverflow-questions.json','r')
            lines = file.readlines()
            # sb = ''
            # for line in lines:
            #     sb = sb + str(line.rstrip('\n').rstrip().split('\t'))
            # file.close()
            return jsonify(lines)
        except FileNotFoundError:
            return jsonify({"status": "文件不存在"})
        except PermissionError:
            return jsonify({"status": "您的权限不足"})


@app.route('/read_json', methods=['GET'])
def read_json():
    data = request.args
    if os.path.exists('./SCRAPY/SCRAPY/' + data['filename']):
        try:
            file = open('./SCRAPY/SCRAPY/' + data['filename'],'r')
            lines = file.readlines()
            # sb = ''
            # for line in lines:
            #     sb = sb + str(line)
            # file.close()
            return jsonify(lines)
        except FileNotFoundError:
            return jsonify({"status": "文件不存在"})
        except PermissionError:
            return jsonify({"status": "您的权限不足"})


if __name__ == '__main__':
    app.run(port=5678)
