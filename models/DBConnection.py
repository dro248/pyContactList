# using pymysql
# installed with: pip3 install pymysql

import pymysql

class DBConnection:
    def __init__(self):
        print("DBConnection created!")
        
        try:
            self.connection = pymysql.connect(
                        db='contact_list', 
                        user='root', 
                        passwd='asdfjkl;', 
                        unix_socket="/var/run/mysqld/mysqld.sock")
        except:
            raise Error("Could not connect to DB")
            
    def executeSQL(self, sql):
        # attempt to execute the sql
        print("DBConnection.executeSQL entered...") 
        print(sql)

        result = None
        try:
            with self.connection.cursor() as cursor:
                result = cursor.execute(sql)
                print(result)
            
            # connection is not autocommit by default
            x = self.connection.commit() 
            print(x)
            print("committed")

        except Exception as e:
            print("SQL ERROR: ----")
            print(e)

        except:
            print("DBConnection Default ExecuteSQL error...")
