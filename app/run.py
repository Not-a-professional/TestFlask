from flask import Flask

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False  # 用于显示jsonify后的中文编码

from app.main import main
app.register_blueprint(main, url_prefix='/main')

from app.crawler import app2
app.register_blueprint(app2, url_prefix='/crawler')


if __name__ == '__main__':
    app.run(port=5678)


