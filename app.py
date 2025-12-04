#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
智能瞭望数据分析处理系统 - 主应用
"""

from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
import os

# 创建Flask应用
app = Flask(__name__)

# 加载配置
app.config.from_object('config.Config')

# 初始化数据库
from models import db
with app.app_context():
    db.init_app(app)
    db.create_all()

# 导入路由
from routes import auth, main
app.register_blueprint(auth.bp)
app.register_blueprint(main.bp)

if __name__ == '__main__':
    app.run(debug=True)