#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Blueprint,request,json
# from flask_pymongo import ObjectId
# from ..app import mongo
from flask import render_template
from app.controllers.front import *

front = Blueprint("front", __name__)

# inisialisasi class
Home = Home.home_controller
Mahasiswa = Mahasiswa.mahasiswa_controller

@front.route('/', methods=['GET','POST'])
def home():
    return Home.index()

@front.route('/about')
def about():
    return Home.about()

@front.route('/mahasiswa')
def mahasiswa():
    return Mahasiswa.index()

@front.errorhandler(404)
def pageNotFound(e):
    return render_template('frontend/errors/404.html'), 404

