from flask import Flask, Blueprint, render_template, url_for, redirect,request
import json
from common.database import DataBaseClient
home = Blueprint('/', __name__)

database = DataBaseClient('localhost', port=27017)

@home.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        database.setDB('owner_article')
        database.setCollection('article')
        articles = database.get_many({})
        return render_template('index.html',Articles=articles)
