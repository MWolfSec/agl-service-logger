from flask import Blueprint
from flask_restful import Api
from resources.Version import Version
from resources.GetList import GetList
from resources.GetLog import GetLog

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

#Route
api.add_resource(Version,'/')
api.add_resource(GetLog,'/log')
api.add_resource(GetList,'/logs')