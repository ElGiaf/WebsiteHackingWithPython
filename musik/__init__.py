from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://musikdbuser:vadget-wyhhuz-3cAkry@192.168.0.112/musikdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "this15asecretk3y"

db = SQLAlchemy(app)

from musik import routes