from flask import Blueprint

app2 = Blueprint('crawler', __name__, static_folder="static", template_folder='templates')

from .crawler import app2

