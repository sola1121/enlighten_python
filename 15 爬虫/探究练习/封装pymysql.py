import pymysql
import logging
import datetime

db_settings = {"user": "root", "password": "123456", "host": "176.209.103.77", "port": 3306, "db" : "maoyandb"}

logger = logging.getLogger("pymysql")
format_log = logging.Formatter("%(asctime)s %()")
file_handler = logging.FileHandler("mysql")


class DBConnect:
    def __init__(self, user, password, db="sys", host="127.0.0.1", port=3306):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db
    
    def connect_db(self):
        try:
            self.db = pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.password, db=self.db, charset="utf8")
        except:
            print("Connect Error")
            return False
        self.cursor = self.db.cursor()
        return True
    
    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.db:
            self.db.close()

    def execute_select(self, sql, params=None):
        if self.connect_db() == False:
            return False
        try:
            if self.db and self.cursor:
                self.cursor.execute(sql, params)
                data = self.cursor.fetchall()
                return data
        except:
            logger.error("Error sql " + sql)
            logger.error("Error params " + params)
            return False

    def execute_insert(self, sql, params=None):
        if self.connect_db() == False:
            return False
        try:
            if self.db and self.cursor:
                self.cursor.execute(sql, params)
                self.db.commit()
        except:
            logger.error("Error sql " + sql)
            logger.error("Error params " + params)
            return False
        return True


if __name__ == "__main__":

    conn = DBConnect(**db_settings)

    insert_sql = "insert into maoyandb.movie_info(movie_name, author, show_time) value(%s,%s,%s)"
    params = ("我不是药神", "徐峥", "2018-07-05")

    conn.execute_insert(insert_sql, params=params)

    conn.close()
