#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Blueprint,request,json
# from flask_pymongo import ObjectId
# from ..app import mongo
from flask import render_template
from app.controllers.back import *

back = Blueprint("back", __name__)

# inisialisasi class
admin = Admin.admin_controller
backend_route = '/admin/'

@back.route('/admin/')
def home():
    return admin.index()

@back.route(f'{backend_route}category', methods=['GET','POST'])
def about():
    return admin.category()


