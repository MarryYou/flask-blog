from flask import Flask, Blueprint, render_template, url_for, redirect, request
import json
from common.database import DataBaseClient
from common.recommend import get_new_article
from urllib.parse import unquote

page = Blueprint("/page", __name__)

database = DataBaseClient("localhost", port=27017)


@page.route("", methods=["GET", "POST"])
def main():
    if request.method == "GET":
        title = request.args.get("title", "")
        print(title)
        database.setDB("owner_article")
        database.setCollection("article")
        title = unquote(title, "utf-8")
        print(title)
        article = database.get_one({"title": title})
        recommend = get_new_article()
        return render_template(
            "page.html", Article=article, title=title, recommend=recommend
        )
