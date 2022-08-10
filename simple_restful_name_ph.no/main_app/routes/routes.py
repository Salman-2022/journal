# from flask import Flask,jsonify,request
# from flask_restful import Resource,Api
from main_app import api
from main_app.controlers.hello_controller import Hello
from main_app.controlers.square_controller import Square
from main_app.controlers.info_controller import info

api.add_resource(Hello,'/')
api.add_resource(Square,'/square/<int:num>')
api.add_resource(info,'/info')