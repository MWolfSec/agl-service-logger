from flask_restful import Resource
from flask import Flask, request, Response
from flask import current_app as app
import os

class GetLog(Resource):

    def get(self):
        logname = request.args.get('file', type=str)
        print(logname)
        try:
            src = os.path.join(app.config["LOGDIR"], logname)
            content = open(src).read()
        except IOError as exc:
            content = str(exc)
        
        return Response(content, mimetype="text/html")

    def post(self):
        return {"response":"POST not allowed!"}