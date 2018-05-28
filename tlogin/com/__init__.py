from flask import Flask,request,render_template
import socket
import pymysql
import json
from utils.DBConnection import DBConnection
from utils.LoginUtil import LoginUtil
import logging
app = Flask(__name__)

@app.route('/')
def index():
    return 'Iam from Login App'

@app.route('/v1/tlogin/football')
def football():
    return json.dumps({'message': 'Football Club Barca', 'host': socket.gethostname()})

@app.route('/v1/tlogin/cricket')
def cricket():
    return json.dumps({'message': 'Royal Chalangers Bangalore', 'host': socket.gethostname()})

@app.route('/name')
def name():
    return 'Hello Rajeesh Host ='+socket.gethostname()


