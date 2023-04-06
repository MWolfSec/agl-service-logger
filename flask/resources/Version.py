from flask_restful import Resource
from flask import Flask, request, Response, current_app as app

class Version(Resource):
    def get(self):
        output ="""<html><body><p>
---------------------------------------------------<br>
V 1.1 AGL Logging service<br>
---------------------------------------------------<br>
Usage:<br>
Display available logs:<br>
/logs<br>
Display a single log:<br>
/log?file=&lt;filename&gt;<br>
</p></body></html>"""
        return Response(output, mimetype="text/html")