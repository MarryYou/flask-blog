from flask import Flask
from flask import render_template, url_for, Blueprint, request, redirect
from router.home import home
from router.login import login
from router.register import register
from router.classify import classfiy
from router.projects import projects
from router.comments import comments
from router.abouts import abouts

from router.creates import creates
from router.pages import page
from flask_basicauth import BasicAuth

import os
import json
import re
import pymongo

# 并发版tornado
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

######################

from common.database import DataBaseClient

database = DataBaseClient("localhost", port=27017)

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile("config.py", silent=True)
app.register_blueprint(home, url_prefix="/home")
app.register_blueprint(login, url_prefix="/login")
app.register_blueprint(register, url_prefix="/register")
app.register_blueprint(classfiy, url_prefix="/classfiy")
app.register_blueprint(projects, url_prefix="/project")
app.register_blueprint(comments, url_prefix="/comment")
app.register_blueprint(abouts, url_prefix="/about")
app.register_blueprint(creates, url_prefix="/create")
app.register_blueprint(page, url_prefix="/page")

app.config["BASIC_AUTH_USERNAME"] = "admin"
app.config["BASIC_AUTH_PASSWORD"] = "fanhaotian"
basic_auth = BasicAuth(app)


@app.route("/")
def appRouter():
    return redirect("home")


@app.route("/admin")
@basic_auth.required
def admin():
    return render_template("base.html")


# @app.route("/create/", methods=["GET", "POST"])
# @basic_auth.required
# def create():
#     if request.method == "GET":
#         return render_template("create.html")
#     else:
#         article = json.loads(request.get_data())
#         database.setDB("owner_classify")
#         database.setCollection("class")
#         data = database.find({"class_name": article["classfiy"]})
#         if len(data) == 0:
#             database.add_one({"class_name": article["classfiy"]})
#         database.setDB("owner_article")
#         database.setCollection("article")
#         try:
#             database.add_one(article)
#             return jsonify({"status": 0, "msg": "保存成功!", "id": article["id"]})
#         except Exception as e:
#             return jsonify({"status": 1, "msg": "保存失败!"})


# @app.route("/create/autocomplete", methods=["GET", "POST"])
# def autocomplete():
#     base = pymongo.MongoClient()
#     db = base["owner_classify"]
#     collection = db["class"]
#     queryValue = request.args.get("query", "")
#     searchValue = "^%s.*" % queryValue
#     try:
#         classify = collection.find({"class_name": re.compile(searchValue)})
#         class_list = []
#         for category in classify:
#             class_list.append({"value": category["class_name"], "data": ""})
#         return jsonify({"suggestions": class_list})
#     except Exception as e:
#         return jsonify({"data": class_list})


def main():
    app.run(debug=True)
    server = HTTPServer(WSGIContainer(app))
    server.listen(port=3366, address="0.0.0.0")
    IOLoop.instance().start()


if __name__ == "__main__":
    main()
