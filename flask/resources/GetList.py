from flask_restful import Resource
from flask import Flask, request, Response
from flask import current_app as app
import os


class GetList(Resource):

    def get(self):
        # Return 404 if path doesn't exist
        logpath = app.config["LOGDIR"]
        if not os.path.exists(logpath):
            return {"response":"Directory not existent"}

        # Check if path is a file and serve
        if os.path.isfile(logpath):
            return {"response":"Not a Directory"}

        # Show directory contents
        output = "<html><body><p>Available Logs: <br>"
        files = os.listdir(logpath)
        for file in files:
            output += str(file) + "<br>"
        
        output += "</p></body></html>"
        
        return Response(output, mimetype="text/html")

    def post(self):
        return {"response":"POST not allowed!"}

