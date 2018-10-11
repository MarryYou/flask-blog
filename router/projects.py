from flask import Flask, Blueprint, render_template, url_for, redirect, request
import splider.repositories as Github
projects = Blueprint('/project', __name__)


@projects.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        sources = Github.getGithub()
        return render_template('project.html', repositories = sources)
