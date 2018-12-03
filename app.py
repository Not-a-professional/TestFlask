from flask import Flask
from flask import jsonify
from flask import render_template
from flask import request

import os

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False # 用于显示jsonify后的中文编码


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


@app.route("/crawler", methods=['GET'])
def crawler():
    # os.chdir('./SCRAPY/SCRAPY') # 必须切换目录，不然爬虫跑不起来
    # print(os.getcwd()) # 获取当前绝对路径
    # 执行命令，让爬虫启动
    data = request.args
    os.system('scrapy runspider ./SCRAPY/SCRAPY/CrawlSpider.py -o ./SCRAPY/SCRAPY/' + data['filename'])
    from flask import redirect
    return redirect('read_json?filename=' + data['filename'])


@app.route('/read_json', methods=['GET'])
def read_json():
    data = request.args
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
