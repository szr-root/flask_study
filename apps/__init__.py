# -*- coding:utf-8 -*-
"""
@ Author:John
@ File:__init__.py.py
@ Time:2022/3/1 11:33
@ Content:
"""
from flask import Flask

import settings
from apps.user.view import user_bp


def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object(settings)  # 加载配置
    # 蓝图
    app.register_blueprint(user_bp)
    print(app.url_map)
    return app
