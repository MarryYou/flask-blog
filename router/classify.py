from flask import Flask, Blueprint, render_template, url_for, redirect, request

classfiy = Blueprint('/classfiy', __name__)


@classfiy.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        return render_template('classfiy.html')
