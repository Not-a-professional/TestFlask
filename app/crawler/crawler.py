import os

from flask import request, jsonify

from app.crawler import app2


@app2.route("/", methods=['GET'])
def crawler():
    # os.chdir('./SCRAPY/SCRAPY') # 必须切换目录，不然爬虫跑不起来
    # print(os.getcwd()) # 获取当前绝对路径
    # 执行命令，让爬虫启动

    data = request.args

    # -a表示额外参数，必须使用name=value键值对方式传入
    os.system('scrapy runspider ./SCRAPY/SCRAPY/CrawlSpider.py '
              '-a url=http://stackoverflow.com/questions?sort=votes -o ./SCRAPY/SCRAPY/' + data['filename'])
    from flask import redirect
    return redirect('crawler/read_json?filename=' + data['filename'])


@app2.route("/read_json", methods=['GET'])
def read_json():
    data = request.args
    try:
        file = open('./SCRAPY/SCRAPY/' + data['filename'], 'r')
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
