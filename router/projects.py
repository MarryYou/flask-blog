from flask import Flask, Blueprint, render_template, url_for, redirect, request
import splider.repositories as Github
from common.recommend import get_new_article

projects = Blueprint("/project", __name__)


@projects.route("/", methods=["GET", "POST"])
def main():
    if request.method == "GET":
        sources = Github.getGithub()
        recommend = get_new_article()
        if len(sources) > 0:
            return render_template(
                "project.html", repositories=sources, recommend=recommend
            )
        else:
            return redirect("/home")
