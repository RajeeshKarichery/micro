import pymysql
import os
class DBConnection:

    @staticmethod
    def getConnection():
        print "connn----->"
        db = os.getenv('RDS_HOST')
        print "conn2----->",db
        return pymysql.connect(host=db, user="",passwd="", db="tenkube", autocommit=True, charset='utf8')