# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 01:01:15 2019

@author: hp
"""
from flask import Flask,render_template,request,url_for,Markup

from scrapp import users
from chart import fig

app = Flask(__name__)

@app.route("/main")
def home():
    return render_template("index.html")
@app.route("/hello",methods=["POST"])
def hello():
    form_data = request.form
    status = users(form_data["name1"],form_data["name2"])
    return render_template("coloumns.html",user1=form_data["name1"],user2=form_data["name2"],status=status,div_placeholder=Markup(status[5]),name1=form_data["name1"],name2=form_data["name2"])

@app.route("/detail")
def detail():
    chart=fig()
    return render_template("detail.html",div_placeholder=Markup(chart))


if __name__ == '__main__':
   app.run(port=8000)

