# new_module/routes.py
from flask import Blueprint
from flask_restful import Api, Resource, reqparse



# Create a new blueprint for the Flit Api
flit_bp = Blueprint('flit_api', __name__)


class FlitAPI(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        # Add argument parsing for each input feature
        self.parser.add_argument('prompt', type=str)
        self.parser.add_argument('format', type=str)

    def get(self):
        return {'message': 'Hello from flit!'}

    def post(self):
        # get data
        args = self.parser.parse_args()
        prompt = args['prompt']
        format = args['format']
        if format == None or format == '':
            format = 'markdown'
        response = f'Flit says: {prompt}'

        # return response
        return {'response': response}


# Create a new Api for the new blueprint
api = Api(flit_bp)
api.add_resource(FlitAPI, '/flit_api')