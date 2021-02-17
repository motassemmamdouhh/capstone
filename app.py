import os
from flask import Flask, json,abort
from flask_cors import CORS
from models import setup_db

def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    CORS(app)
    return app
app = create_app()
if __name__ == '__main__':
    app.run()