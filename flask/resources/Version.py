from flask_restful import Resource
from flask import Flask, request, current_app as app
import os
import stat
import subprocess
import io
import json
import time
import datetime

class Version(Resource):
    def get(self):
        
        return {"Version":"""        (  ( (  ( (        (  (         (  (    )  (        (
 /(_)) (   )\))()\))()\  (    )\))(   (   ))\ )(  /(( )\  (   ))\
 (_))   )\ ((_))((_))((_) )\ )((_))\   )\ /((_|()\(_))((_) )\ /((_)
 | |   ((_) (()(_|()(_|_)_(_/( (()(_) ((_|_))  ((_))((_|_)((_|_))
 | |__/ _ \/ _` / _` || | ' \)) _` |  (_-< -_)| '_\ V /| / _|/ -_)
 |____\___/\__, \__, ||_|_||_|\__, |  /__|___||_|  \_/ |_\__|\___|
          |___/|___/         |___/
---------------------------------------------------
V 1.1  AGL Logging service
---------------------------------------------------"""}