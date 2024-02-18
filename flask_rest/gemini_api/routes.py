# new_module/routes.py
from flask import Blueprint
from flask_restful import Api, Resource, reqparse

# import gemini engine
from .engine import Engine



gemini_blueprint = Blueprint('gemini_api', __name__)

class GeminiAPI(Resource):
    def __init__(self):
        self.engine = Engine()
        self.engine.load_model('gemini-pro')

        self.parser = reqparse.RequestParser()
        # Add argument parsing for each input feature
        self.parser.add_argument('prompt', type=str)
        self.parser.add_argument('format', type=str)

    def get(self):
        return {'message': 'Hello from gemini!'}

    def post(self):
        # get data
        args = self.parser.parse_args()
        prompt = args['prompt']
        format = args['format']
        if format == None or format == '':
            format = 'markdown'
        response = self.engine.generate_text(prompt, format=format)

        # return response
        return {'response': response}



api = Api(gemini_blueprint)

api.add_resource(GeminiAPI, '/gemini_api')
