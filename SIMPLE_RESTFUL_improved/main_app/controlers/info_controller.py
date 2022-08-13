from unittest import result
from flask import jsonify,request
from flask_restful import Resource,reqparse
from main_app.service.info_service import InfoService


class Info(Resource):   
    def get(self):
        return jsonify({"message":"It works"})   

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('mobile_number', type=str, help='mobile_number should not be blank', required=True)
        parser.add_argument('first_name', type=str)
        parser.add_argument('last_name', type=str)
        args = parser.parse_args()
        result = InfoService.create_name(args["first_name"],args["last_name"])
        data = {"name":result,"mobile_number":args["mobile_number"]}
        print('hello....',data)
        return jsonify({'data':data})
