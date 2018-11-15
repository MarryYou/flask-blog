from flask import Flask, Blueprint, render_template, url_for, redirect, request
import json
from common.database import DataBaseClient
import pymongo
from common.recommend import get_new_article

home = Blueprint("/home", __name__)

database = DataBaseClient("localhost", port=27017)


@home.route("", methods=["GET", "POST"])
def main():
    if request.method == "GET":
        tag = request.args.get("tag", "ALL")
        page = request.args.get("page", 1)
        pagesize = 10
        database.setDB("owner_classify")
        database.setCollection("class")
        classes = database.get_many({})
        recommend = get_new_article()
        client = pymongo.MongoClient()
        db = client["owner_article"]
        collection = db["article"]
        page = int(page)
        pagesize = int(pagesize)
        if len(tag) <= 0 or tag == "ALL":
            data = collection.find().limit(pagesize).skip((page - 1) * pagesize)
            total = collection.count({})
            if total != 0:
                if total % int(pagesize) == 0:
                    total = total // int(pagesize)
                else:
                    total = total // int(pagesize) + 1

        else:
            data = (
                collection.find({"classfiy": tag})
                .limit(pagesize)
                .skip((page - 1) * pagesize)
            )
            total = collection.count({"classfiy": tag})
            if total != 0:
                if total % pagesize == 0:
                    total = total // pagesize
                else:
                    total = total // pagesize + 1
        articles = []
        for d in data:
            articles.append(d)
        if len(articles) == 0 and tag != "ALL":
            database.setDB("owner_classify")
            database.setCollection("class")
            database.delete_one({"class_name": tag})
        return render_template(
            "index.html",
            Articles=articles,
            classes=[{"class_name": "ALL"}] + classes,
            recommend=recommend,
            tag=tag,
            page=page,
            total=total,
        )

