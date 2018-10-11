from flask import Flask, Blueprint, render_template, url_for, redirect, request

comments = Blueprint('/comment', __name__)


@comments.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        return render_template('comment.html')
