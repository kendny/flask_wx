# -*- coding utf-8 -*-
"""
在实际生产环境部署是不需要的，解决在本地环境无法加载的问题
部署上线有另外的方式让它直接找到静态资源
"""
from flask import Blueprint, send_from_directory
from application import app

route_static = Blueprint('static', __name__)


@route_static.route("/<path:filename>")
def index(filename):
    app.logger.info(filename)
    return send_from_directory(app.root_path + "/web/static/", filename)
