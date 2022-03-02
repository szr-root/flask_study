# -*- coding:utf-8 -*-
"""
@ Author:John
@ File:view.py
@ Time:2022/3/1 11:46
@ Content:
"""
import hashlib

from flask import Blueprint, request, render_template, redirect, url_for
from sqlalchemy import or_, and_

from apps.user.model import User
from exts import db

user_bp = Blueprint('user', __name__)


@user_bp.route('/')
def user_center():
    users = User.query.filter(User.isdelete == False).all()
    return render_template('user/show.html', users=users)


@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # 获取post提交的数据
        username = request.form.get('username')
        password = request.form.get('password')
        phone = request.form.get('phone')
        user = User()
        user.username = username
        user.password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        user.phone = phone
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('user.user_center'))
        # return render_template('user/register.html', msg='用户命已存在')

    return render_template('user/register.html')


@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        new_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        # 查询用户
        user_list = User.query.filter_by(username=username)
        # user = User.query.filter(and_)
        for u in user_list:
            if u.password == new_password:
                return 'ok'
        else:
            return render_template('user/login.html', msg='用户名或密码有误！')

    return render_template('user/login.html')


@user_bp.route('/search')
def search():
    keyword = request.args.get('search')
    user_list = User.query.filter(or_(User.username.contains(keyword), User.phone.contains(keyword))).all()
    return render_template('user/show.html', users=user_list)


@user_bp.route('/logout', methods=['GET', 'POST'])
def logout():
    return 'logout'


@user_bp.route('/update', methods=['GET', 'POST'], endpoint='update')
def user_update():
    if request.method == 'POST':
        username = request.form.get('username')
        phone = request.form.get('phone')
        id = request.form.get('id')
        #  找用户
        user = User.query.get(id)
        user.phone = phone
        user.username = username
        #  提交
        db.session.commit()
        return redirect(url_for('user.user_center'))
    else:
        id = request.args.get('id')
        user = User.query.get(id)
        return render_template('user/update.html', user=user)


@user_bp.route('/del')
def user_delete():
    user_id = request.args.get('id')
    user = User.query.get(user_id)
    # 逻辑删除
    # user.isdelete = True
    # db.session.commit()


    # 物理删除
    db.session.delete(user)
    db.session.commit()

    return redirect(url_for('user.user_center'))
    # # 获取传递的username
    # username = request.args.get('username')
    # # 根据username找到列表中的user对象
    # for user in users:
    #     if user.username == username:
    #         # 删掉user
    #         users.remove(user)
    #         return redirect('/')
    # else:
    #     return '删除失败'
