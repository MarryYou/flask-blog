from flask import Flask, Blueprint, render_template, url_for, redirect, request,jsonify
import os
import json
from common.database import DataBaseClient
creates = Blueprint('/create', __name__)

database = DataBaseClient('localhost', port=27017)

@creates.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        return render_template('create.html')
    else:
        database.setDB('owner_article')
        database.setCollection('article')
        article = json.loads(request.get_data())
        try:
                database.add_one(article)
                return jsonify({'status': 0, 'msg': '保存成功!','id':article['id']})
        except Exception as e:
                return jsonify({'status': 1,'msg':'保存失败!'})


       
      
