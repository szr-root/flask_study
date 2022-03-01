# -*- coding:utf-8 -*-
"""
@ Author:John
@ File:view.py
@ Time:2022/3/1 11:46
@ Content:
"""
from flask import Blueprint, request, render_template, redirect

from apps.user.model import User

user_bp = Blueprint('user', __name__)

users = []


@user_bp.route('/')
def user_center():
    return render_template('user/show.html', users=users)


@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # 获取post提交的数据
        username = request.form.get('username')
        password = request.form.get('password')
        phone = request.form.get('phone')
        for user in users:
            if user.username == username:
                return render_template('user/register.html', msg='用户命已存在')
        # 创建用户对象
        user = User(username, password, phone)
        # 添加到用户列表
        users.append(user)
        return redirect('/')

    return render_template('user/register.html')


@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    return 'login'


@user_bp.route('/logout', methods=['GET', 'POST'])
def logout():
    return 'logout'


@user_bp.route('/update', methods=['GET', 'POST'], endpoint='update')
def update():
    if request.method == 'POST':
        realname = request.form.get('realname')
        username = request.form.get('username')
        password = request.form.get('password')
        phone = request.form.get('phone')
        for user in users:
            if user.username == realname:
                user.username = username
                user.phone = phone
                return redirect('/')

    else:
        username = request.args.get('username')
        for user in users:
            if user.username == username:
                return render_template('user/update.html', user=user)


@user_bp.route('/del')
def del_user():
    # 获取传递的username
    username = request.args.get('username')
    # 根据username找到列表中的user对象
    for user in users:
        if user.username == username:
            # 删掉user
            users.remove(user)
            return redirect('/')
    else:
        return '删除失败'
