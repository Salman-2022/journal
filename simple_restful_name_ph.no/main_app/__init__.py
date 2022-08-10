from flask import Flask
from flask_restful import Api
# from sample import app


app = Flask(__name__)
api = Api(app)
import main_app.routes.routes