from flask import Flask

app = Flask(__name__)
app.config["SECRET_KEY"] = "15damatina"

from app import routes