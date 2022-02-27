from flask import Flask

# Inisialisasi folder views
app = Flask(__name__, template_folder="views")

# Inisialisasi Secret Key
app.secret_key = '&^*&$3424#@^(*'

# Inisialisasi folder static
app._static_folder = 'static'

###
# Inisialisasi core blueprint
###
from app.core.Front_routes import front
from app.core.Back_routes import back

app.register_blueprint(front)
app.register_blueprint(back)

