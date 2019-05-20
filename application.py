# -*- coding utf-8 -*-
"""
封装的Flask的全局变量， 包括app，数据库等
"""

from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
import os


class Application(Flask):
    """配置按需加载进行分离"""

    def __init__(self, import_name, template_folder=None):
        super(Application, self).__init__(import_name)
        # 加载配置
        self.config.from_pyfile('config/base_setting.py')

        # 配置文件按不同的环境进行加载
        # 在linux系统中设置环境变量，通过命令行设置：
        # export ops_config = local
        if "ops_config" in os.environ:
            self.config.from_pyfile('config/%s_setting.py' % os.environ['ops_config'])

        db.init_app(self)


db = SQLAlchemy()
# app = Flask(__name__)
# os.getcwd() 获取当前路径
app = Application(__name__, template_folder=os.getcwd() + "、web/templates/")
manager = Manager(app)

"""
函数模板：
    将模板方法注入进去
"""
from common.libs.UrlManager import UrlManager
app.add_template_global(UrlManager.buildStaticUrl, 'buildStaticUrl')
app.add_template_global(UrlManager.buildUrl, 'buildUrl')
