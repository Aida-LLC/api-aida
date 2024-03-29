# __init__.py
from flask import Flask

app = Flask(__name__)


from flask_rest import routes
from flask_rest.gemini_api.routes import gemini_blueprint
from flask_rest.flit_api.routes import flit_bp


# Register the new module blueprint
app.register_blueprint(gemini_blueprint)
app.register_blueprint(flit_bp)




