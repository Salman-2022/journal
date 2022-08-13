from flask import jsonify
from flask_restful import Resource,reqparse


class InfoService():
    def create_name(first_name,last_name):
        name = str(first_name + ' ' + last_name)
        return name