from flask import Flask
from flask_cors import CORS, cross_origin

def create_app(config_filename):
    app = Flask(__name__)
    cors = CORS(app)
    app.config.from_pyfile('config.py')

    from app import api_bp
    app.register_blueprint(api_bp,url_prefix='/')
    return app

if __name__=="__main__":
    app = create_app("config")
    # TODO: Set last message timestamp in config to current time
    app.run(debug=True, port=5001, host='0.0.0.0')