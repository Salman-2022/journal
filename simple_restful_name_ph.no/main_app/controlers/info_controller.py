from unittest import result
from flask import jsonify,request
from flask_restful import Resource,reqparse

from main_app.service.info_service import InfoService


class info(Resource):
    def get(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.name = str(self.first_name +' '+ self.last_name)
        self.age = age
        return jsonify({'name':self.name,'age':self.age})
       
    def post(self):
        parser = reqparse.RequestParser()
        # first = 
        parser.add_argument('mobile_number', type=str, help='mobile_number should not be blank', required=True)
        parser.add_argument('first_name', type=str)
        parser.add_argument('last_name', type=str)
        args = parser.parse_args()
        # InfoService()
        # return InfoService(args)
        # class info(InfoService):
        #     def action():
        #         print('hello')
        result = InfoService.create_name(args)
        print('hello....')
        return jsonify(result)
        # print('salma......',args)
        # return jsonify(first) ,201