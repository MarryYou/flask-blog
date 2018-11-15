from flask import Flask, Blueprint, render_template, url_for, redirect, request
from common.recommend import get_new_article

comments = Blueprint("/comment", __name__)


@comments.route("/", methods=["GET", "POST"])
def main():
    if request.method == "GET":
        recommend = get_new_article()
        return render_template("comment.html", recommend=recommend)
