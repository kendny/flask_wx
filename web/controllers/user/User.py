# -*- coding utf-8 -*-

"""
用户管理相关
"""
from flask import Blueprint, render_template

route_user = Blueprint('user_page', __name__)


@route_user.route("/login")
def login():
    return render_template("user/login.html")
