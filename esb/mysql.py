
import pymysql

class DBHelper():
    
    def __init__(self):
        self.host='localhost'
        self.user='root'
        self.passwd='root'
        self.db='esb'
        self.charset='utf8mb4'

    def connectDatabase(self):
        conn=pymysql.connect(host=self.host,
                             user=self.user,
                             passwd=self.passwd,
                             db=self.db,#不指定数据库名
                             charset='utf8') #要指定编码，否则中文可能乱码
        return conn
    
    def dbVersion(self):
        conn=self.connectDatabase()
        cur=conn.cursor()
        cur.execute("SELECT VERSION()")
        print(cur.fetchone())
        cur.close()
        conn.close()

class TestDBHelper():
    def __init__(self):
        self.dbHelper=DBHelper()

    def testVersion(self):
        self.dbHelper.dbVersion() 

if __name__=="__main__":
    testDBHelper=TestDBHelper()
    testDBHelper.testVersion()



# # 打开数据库连接
# db = pymysql.connect(host='localhost',
#                              user='root',
#                              password='root',
#                              database='esb',
#                              charset='utf8mb4')

# # 使用cursor()方法获取操作游标 
# cursor = db.cursor()

# # 使用execute方法执行SQL语句
# cursor.execute("SELECT VERSION()")

# # 使用 fetchone() 方法获取一条数据
# data = cursor.fetchone()



# # 关闭数据库连接
# db.close()