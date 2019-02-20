import pymysql

class MySql_PY:
    def __init__(self, host, port, db, user, passwd, charset="utf8"):
        self.host = host
        self.port = port
        self.db = db
        self.user = user
        self.passwd = passwd
        self.charset = charset
    
    def link(self):
        self.conn = pymysql.connect(host=self.host, port=self.port, db=self.db, user=self.user, passwd=self.passwd, charset=self.charset)
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def exe_sql(self, sql):
        self.link()
        self.cursor.execute(sql)
        self.conn.commit()
        self.close()
        print("OJBK")

    def __enter__(self):
        self.link()
    
    def __exit__(self):
        self.close()
