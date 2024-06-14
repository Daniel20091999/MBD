import pymysql

class conexion:

    def __init__(self):

        self.conn = pymysql.connect(
            host = 'localhost',
            user ='root',
            passwd='root',
            db='MBD')
        self.conn = self.conn.cursor()
        
    
