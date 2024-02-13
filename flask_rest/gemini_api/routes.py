# new_module/routes.py
from flask import Blueprint
from flask_restful import Api, Resource



gemini_blueprint = Blueprint('gemini_api', __name__)

class GeminiAPI(Resource):
    def get(self):
        return {'message': 'Hello from gemini!'}


api = Api(gemini_blueprint)

api.add_resource(GeminiAPI, '/gemini_api')
