from flask import Flask, Blueprint, render_template, url_for, redirect, request
import json
from common.database import DataBaseClient

page = Blueprint("/page", __name__)

database = DataBaseClient("localhost", port=27017)


@page.route("", methods=["GET", "POST"])
def main():
    if request.method == "GET":
        title = request.args.get("title", "")
        database.setDB("owner_article")
        database.setCollection("article")
        article = database.get_one({"title": title})
        return render_template("page.html", Article=article, title=title)
