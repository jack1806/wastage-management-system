import sqlite3
from datetime import datetime as dt

class servicesDB:

    def addFeedback(self,data):
        conn = sqlite3.connect('database.db')
        query = "INSERT INTO FEEDBACK VALUES('%s')"%(data)
        conn.execute(query)
        conn.commit()
        conn.close()

    def viewFeedback(self):
        conn = sqlite3.connect('database.db')
        query = "SELECT * FROM FEEDBACK"
        csr = conn.cursor()
        csr.execute(query)
        rows = csr.fetchall()
        conn.close()
        return rows

    def doSignUp(self,name,pwd,email,typ,phone,eid):
        conn = sqlite3.connect('database.db')
        query = "INSERT INTO USERS VALUES('%s','%s','%s','%s','%s','%s')"%(name,eid,email,pwd,phone,typ)
        print(query)
        conn.execute(query)
        conn.commit()
        print("Success")
        conn.close()

    def login(self,e,p):
        conn = sqlite3.connect('database.db')
        csr = conn.cursor()
        query = "SELECT * FROM USERS WHERE EMAIL = '%s' and PASSWORD = '%s'"%(e,p)
        csr.execute(query)
        rows = csr.fetchall()
        conn.close()
        return rows

    def addWaste(self,quan,food):
        t = ((str(dt.today())).split(" ")[0]).split('-')
        time = t[1]+'/'+t[2]+'/'+t[0]
        query = "INSERT INTO WASTE VALUES('%s','%s','%s')"%(quan,food,time)
        conn = sqlite3.connect('database.db')
        print(query)
        conn.execute(query)
        conn.commit()
        print("Success")
    
    def getWaste(self):
        query = "SELECT * FROM WASTE"
        conn = sqlite3.connect('database.db')
        csr = conn.cursor()
        csr.execute(query)
        row = csr.fetchall()
        conn.close()
        return row
        
