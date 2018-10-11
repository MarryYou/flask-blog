from flask import Flask, Blueprint, render_template, url_for, redirect, request, jsonify
import os
import json
import common.commonfunc as comnonFunc
from common.database import DataBaseClient
import common.commonval as commonVal
register = Blueprint('/register', __name__)

database = DataBaseClient('localhost', port=27017)


@register.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        try:
            personInfo = json.loads(request.get_data())
            database.setDB('flask_blog_user')
            database.setCollection('user')
            name = personInfo['username']
            pwd = personInfo['pwd']
            md5_salt = comnonFunc.create_salt(name)
            md5_pwd = comnonFunc.create_md5(pwd, md5_salt)
            if personInfo['avatar'] == None:
                personInfo['avatar'] = commonVal.default_avatar
            personList = database.get_many({'name': name})
            emailList = database.get_many({'email': personInfo['email']})
            if len(personList)>0 or len(emailList) >0 :
                return jsonify({'status': '用户已存在，请重新注册。', 'code': '1'})
            else:                
                database.add_one({
                    'name': personInfo['username'],
                    'email': personInfo['email'],
                    'md5_pwd': md5_pwd,
                    'md5_salt': md5_salt,
                    'avatar': personInfo['avatar']
                })
                del personInfo, name, pwd, md5_pwd, md5_salt
                return jsonify({'status': '注册成功!', 'code': '0'})
        except Exception as e:
            return jsonify({'status': e, 'code': '1'})


@register.route('/avatar', methods=['GET', 'POST'])
def upload_avatar():
    if request.method == 'GET':
        return 'hehe'
    elif request.method == 'POST':
        try:
            path = os.path.join(os.getcwd(), 'static', 'avatar', 'avatar.png')
            f = request.files['avatar']
            f.save(path)
            return 'success'
        except Exception as e:
            print(e)
