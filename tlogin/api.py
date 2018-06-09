from flask import Flask,request,render_template
import socket
import json
from com.utils.DBConnection import DBConnection
from com.utils.LoginUtil import LoginUtil
import pymysql

import logging
app = Flask(__name__)

@app.route('/')
def index():
    return 'Iam from RDS App'

@app.route('/v1/login/football')
def football():
    return json.dumps({'message': 'Football Club Barca', 'host': socket.gethostname()})

@app.route('/v1/login/cricket')
def cricket():
    return json.dumps({'message': 'Royal Chalangers Bangalore', 'host': socket.gethostname()})


@app.route("/v1/login/name/filter/<id>")
def do_ge_name(id):
    print "Id........."+id
    if int(id) == 1:
        return "Messi"
    elif int(id) == 2:
        return "Ronaldo"
    elif int(id) == 3:
        return "Neymar"
    else:
        return "nil"

@app.route('/v1/login/signup',methods=['POST','GET'])
def signup():
    try:
        conn =DBConnection.getConnection()
        cursor = conn.cursor()
        sel_cur = conn.cursor(pymysql.cursors.DictCursor)
        data =request.get_json()
        if data is None:
            return json.dumps({'message': 'Data none!'})
        print "data====",data
        sql = "SELECT id FROM user WHERE login_id =%s"
        sel_cur.execute(sql,(data['login_id']))
        row = sel_cur.fetchone()
        if row is not None:
            return json.dumps({'message': 'User Exist!'})

        id = LoginUtil.genGuid()
        sql = "insert into user(id,login_id,name) values(%s,%s,%s)"
        cursor.execute(sql,(id,data['login_id'],data['name']))
        return json.dumps({'message': 'User created successfully !', 'id': id})
    except Exception as e:
        err_msg =  repr(e)
        return json.dumps({'message': err_msg})

@app.route('/v1/login/simplesignup')
def simplesignup():
    try:
        conn =DBConnection.getConnection()
        cursor = conn.cursor()
        id = LoginUtil.genGuid()
        sql = "insert into user(id,login_id,name) values(%s,%s,%s)"
        cursor.execute(sql,(id,'reji','rejeesh'))
        return json.dumps({'message': 'User created successfully !', 'id': id})
    except Exception as e:
        err_msg =  repr(e)
        return json.dumps({'message': err_msg})


@app.route('/name')
def name():
    return 'HelloRds 1.8 Rajeesh Host ='+socket.gethostname()


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=80)