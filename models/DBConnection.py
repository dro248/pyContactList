# using pymysql
# installed with: pip3 install pymysql

import pymysql

class DBConnection:
    def __init__(self):
        print("DBConnection created!")
        self.connection = pymysql.connect(
                        db='contact_list', 
                        user='root', 
                        passwd='asdfjkl;', 
                        unix_socket="/var/run/mysqld/mysqld.sock")

    def executeSQL(self, sql):
        # attempt to execute the sql
        print("DBConnection.executeSQL entered...")
    
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql)
           
            # connection is not autocommit by default
            self.connection.commit() 

        except:
            print("SQLERROR: Something broke in DBConnection.executeSQL().")
        
        finally:
            self.connection.close()
