from flask import Flask, Blueprint, render_template, url_for, redirect, request

abouts = Blueprint('/abouts', __name__)


@abouts.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        return render_template('about.html')
