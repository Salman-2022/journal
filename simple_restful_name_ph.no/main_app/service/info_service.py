from flask import jsonify
from flask_restful import Resource,reqparse


class InfoService(Resource):
    def create_name(self,phone_number,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.name = str(self.first_name + ' ' + self.last_name)
        return (self.name , self.phone_number)