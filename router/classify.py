from flask import Flask, Blueprint, render_template, url_for, redirect, request
from common.recommend import get_new_article

classfiy = Blueprint("/classfiy", __name__)


@classfiy.route("", methods=["GET", "POST"])
def main():
    if request.method == "GET":
        recommend = get_new_article()

        return render_template("classfiy.html", recommend=recommend)
