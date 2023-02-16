from flask import Blueprint
from flask_restful import Api
from resources.Version import Version
from resources.Log import Log


api_bp = Blueprint('api', __name__)
api = Api(api_bp)

#Route
api.add_resource(Version,'/')
api.add_resource(Log,'/log')
