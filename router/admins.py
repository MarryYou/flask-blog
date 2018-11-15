from flask import Flask, Blueprint, render_template, url_for, redirect, request, g
import json
from common.database import DataBaseClient
import pymongo
from flask_basicauth import BasicAuth

blog_admin = Blueprint("/admin", __name__)

BASE_USERNAME = "admin"
BASE_PASSWORD = "FANHAOTIAN"
basic_auth = BasicAuth(blog_admin)


@blog_admin.route("", methods=["GET", "POST"])
@basic_auth.required
def admin():
    return render_template("base.html")

