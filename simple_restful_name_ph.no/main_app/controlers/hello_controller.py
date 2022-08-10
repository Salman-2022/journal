from flask import jsonify,request
from flask_restful import Resource,reqparse
from main_app.service.info_service import InfoService

class Hello(Resource):
    def get(self):
        return jsonify({'message':'hello world'})
    # def post(self):
    #     data = request.get_json()
    #     return jsonify({'data': data}),201
    def post(self):

        parser = reqparse.RequestParser()
        # first = 
        parser.add_argument('mobile_number', type=str, help='mobile_number should not be blank', required=True)
        # parser.add_argument('mobile_number', type=str, help='mobile_number should not be blank', required=True)
        # second = 
        parser.add_argument('first_name', type=str)
        # third = 
        parser.add_argument('last_name', type=str)
        parser.add_argument('first_name'+' '+'last_name')
        # args = (InfoService(first,second,third))
        parser.remove_argument('first_name','last_name')
        InfoService()
        args = parser.parse_args()
        # parser.parse_args()
        # print(create_name())
        print('salman......',args)
        return jsonify(args),201
        # args = InfoService()
        # return args



