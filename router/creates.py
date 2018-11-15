from flask import Flask, Blueprint, render_template, url_for, redirect, request, jsonify
import os
import json
import re
import pymongo
from common.database import DataBaseClient

creates = Blueprint("/create", __name__)

database = DataBaseClient("localhost", port=27017)


@creates.route("/", methods=["GET", "POST"])
def main():
    if request.method == "GET":
        return render_template("create.html")
    else:
        article = json.loads(request.get_data())
        database.setDB("owner_classify")
        database.setCollection("class")
        database.add_one({"class_name": article["classfiy"]})
        database.setDB("owner_article")
        database.setCollection("article")
        try:
            database.add_one(article)
            return jsonify({"status": 0, "msg": "保存成功!", "id": article["id"]})
        except Exception as e:
            return jsonify({"status": 1, "msg": "保存失败!"})


@creates.route("/autocomplete", methods=["GET", "POST"])
def autocomplete():
    base = pymongo.MongoClient()
    db = base["owner_classify"]
    collection = db["class"]
    queryValue = request.args.get("query", "")
    searchValue = "^%s.*" % queryValue
    try:
        classify = collection.find({"class_name": re.compile(searchValue)})
        class_list = []
        for category in classify:
            class_list.append({"value": category["class_name"], "data": ""})
        return jsonify({"suggestions": class_list})
    except Exception as e:
        return jsonify({"data": class_list})

