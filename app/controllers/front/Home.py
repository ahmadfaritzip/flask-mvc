from flask import render_template
from app.models.Auth_model import authmodel

class Home():

    def __init__(self):
        pass

    def index(self):
        print(authmodel.getUser())
        data = {'judul' : 'Home'}
        return render_template('frontend/pages/home.html', data=data)

    def about(self):
        data = {'judul' : 'About'}
        return render_template('frontend/pages/about.html', data=data)

home_controller = Home()
