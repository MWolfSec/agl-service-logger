from flask_restful import Resource
from flask import Flask, request
import os
import stat
import subprocess
import io

class Log(Resource):

    def log_command(self,command):
        return_code = subprocess.call(command, shell=True)
        #p = subprocess.Popen("echo test >> /home/kali/logging/log.txt", stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        #return io.TextIOWrapper(p.stdout,encoding="utf-8")
        return return_code

    def get(self):
        return {"response":"GET not allowed!"}

    def post(self):
        com = ""
        req = request.get_json()
        if 'command' in req:
            com = req['command']
        command= "echo "  + str(com) + " >> /home/agl-driver/logging/log.txt"
        print(command)
        forbiddenCommands = ["rm","su","sudo",":(){:|:&};:","mv","wget","apt-get",">","dd","shred","gunzip"]

        if not com in forbiddenCommands:
            code = self.log_command(command)
            if code == 0:
                return {"response":"command logged!"}
            else:
                {"response":"unexpected error!"}
        else: 
            return {"response":"forbidden command!"}

        return {"response":"unexpected error!"}

