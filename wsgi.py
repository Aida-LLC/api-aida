# run.py
from flask_rest import app
from flask_cors import CORS


CORS(app, origins="*", allow_headers="*")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
