from flask import render_template

class Admin():

    def __init__(self):
        pass

    def index(self):
        data = {'judul' : 'Dashboard'}
        return render_template('backend/pages/dashboard.html', data=data)

    def category(self):
        data = {'judul' : 'Kategori'}
        return render_template('backend/pages/category.html', data=data)

admin_controller = Admin()
