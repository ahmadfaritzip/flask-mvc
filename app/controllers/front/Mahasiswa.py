from flask import render_template

class Mahasiswa():
    data = {}

    def __init__(self):
        pass

    def index(self):
        self.data['judul'] = 'Mahasiswa'
        return render_template('frontend/pages/mahasiswa.html', data=self.data)

mahasiswa_controller = Mahasiswa()
