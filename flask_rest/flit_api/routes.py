# new_module/routes.py
from flask import Blueprint
from flask_restful import Api, Resource, reqparse

from .engine import ChatProcessor

# Create a new blueprint for the Flit Api
flit_bp = Blueprint('flit_api', __name__)


class FlitAPI(Resource):
    def __init__(self):
        self.chat_processor = ChatProcessor()
        self.rag_chain = self.chat_processor.initialize_rag_chain()
        
        self.parser = reqparse.RequestParser()
        # Add argument parsing for each input feature
        self.parser.add_argument('question', type=str)
        self.parser.add_argument('history', type=str)

    def get(self):
        return {'message': 'Hello from flit!'}

    def post(self):
        # get data
        args = self.parser.parse_args()
        question = args['question']
        history = args['history']

        chat_history = self.chat_processor.generate_history(history)
        ai_message = self.rag_chain.invoke({"question": question, "chat_history": chat_history})


        # return response
        return {'response': ai_message.content}


# Create a new Api for the new blueprint
api = Api(flit_bp)
api.add_resource(FlitAPI, '/flit_api')