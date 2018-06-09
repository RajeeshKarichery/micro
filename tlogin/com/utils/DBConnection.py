import pymysql
import os
from flask import request
class DBConnection:

    @staticmethod
    def get_instance_id():
        if request.referrer is None:
            url = request.host
        else:
            url = request.referrer
        url = url.replace('http://', '')
        url = url.replace('https://', '')
        url = url.split("/")
        url = url[0]
        dic_url = url.split(":")
        return dic_url[0]

    @staticmethod
    def getConnection():
        print "connn start----->"
        url = DBConnection.get_instance_id()
        print "Url ----->",url
        os.environ['BARCA'] = 'MESSI'
        host = os.getenv('RDS_HOST')
        user = os.getenv('RDS_USER')
        passwd = os.getenv('RDS_PASSWORD')
        db = os.getenv('RDS_DB')
        port = os.getenv('RDS_PORT')
        print "conn2----->",db,host,user,passwd,port
        map_db = os.getenv(url)
        print "url mapped db--->",map_db
        port = int(port)
        return pymysql.connect(host=host,port=port, user=user,passwd=passwd, db=map_db, autocommit=True, charset='utf8')