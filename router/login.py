from flask import Flask, Blueprint, render_template, url_for, redirect,request,jsonify
import json
from common.database import DataBaseClient
import common.commonfunc as commonFunc
login = Blueprint('/login', __name__)

database = DataBaseClient('localhost',port=27017)

@login.route('/',methods=['GET','POST'])
def main():
    if request.method == 'GET':
        return render_template('login.html',arg='注册')
    elif request.method == 'POST':
        database.setDB('flask_blog_user')
        database.setCollection('user')
        personInfo  = json.loads(request.get_data())
        person = database.get_many({'name': personInfo['username']})
        if len(person)> 0:
            md5_salt = commonFunc.create_salt(personInfo['username'])
            md5_pwd = commonFunc.create_md5(personInfo['pwd'],md5_salt)
            if person[0]['md5_salt'] == md5_salt and person[0]['md5_pwd'] == md5_pwd:               
                 return jsonify({'status': '登陆成功', 'code': '0', 'status': person[0]['md5_salt']})
            else:
                return jsonify({'status': '用户名或者密码错误，请重新验证', 'code': '2'})
        else:
            return jsonify({'status': '用户不存在，请先注册', 'code': '1'})



       
