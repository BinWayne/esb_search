
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

    def insert(self,sql,*params):#注意这里params要加*,因为传递过来的是元组，*表示参数个数不定
        conn=self.connectDatabase()
        cur=conn.cursor()
        cur.execute(sql,params)
        conn.commit()#注意要commit
        cur.close()
        conn.close()

class TestDBHelper():
    def __init__(self):
        self.dbHelper=DBHelper()

    def testVersion(self):
        self.dbHelper.dbVersion() 
    #插入数据
    def testInsert(self):
        sql="INSERT INTO esb.overview \
(big_category, sub_category, svc_code, svc_name, scene_code, scene_name, trade_code, trade_name, consumer, provider, status) \
VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) "
        params=("test1","test2","test3",
        "test4","test5","test6","test7","test8","test9","test10","test")
        self.dbHelper.insert(sql,*params) #  *表示拆分元组，调用insert（*params）会重组成元组


if __name__=="__main__":
    testDBHelper=TestDBHelper()
    testDBHelper.testVersion()
    testDBHelper.testInsert()



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