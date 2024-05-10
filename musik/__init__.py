from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://musikdbuser:vadget-wyhhuz-3cAkry@192.168.0.112/musikdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "3ecb35af150463b6b420a478902cb4787648611af6e75e9b3d22c1635faae3aa"

db = SQLAlchemy(app)

from musik import routes