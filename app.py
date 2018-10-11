from flask import Flask
from flask import render_template,url_for,Blueprint,request
from router.home import home
from router.login import login
from router.register import register
from router.classify import classfiy
from router.projects import projects
from router.comments import comments
from router.abouts import abouts
from router.creates import creates
app = Flask(__name__,instance_relative_config=True)
app.config.from_pyfile('config.py',silent=True)
app.register_blueprint(home, url_prefix='/')
app.register_blueprint(login, url_prefix='/login')
app.register_blueprint(register, url_prefix='/register')
app.register_blueprint(classfiy, url_prefix='/classfiy')
app.register_blueprint(projects, url_prefix='/project')
app.register_blueprint(comments, url_prefix='/comment')
app.register_blueprint(abouts, url_prefix='/about')
app.register_blueprint(creates, url_prefix='/create')

def main():
    app.run(host='localhost',port=9999,debug=True)

if __name__ == '__main__':
    main()
