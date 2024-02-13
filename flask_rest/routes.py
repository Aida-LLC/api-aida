# routes.py
from flask_rest import app
from flask_restful import Resource, Api


api = Api(app)
class ThisIsAida(Resource):
    def get(self):
        return {'key': 'Hi there welcome to aida!'}


api.add_resource(HelloWorld, '/')
