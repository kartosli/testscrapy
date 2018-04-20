from pymongo import MongoClient



class mongo(object) :

    def __init__(self):
        host = "127.0.0.1"
        port = 27017
        dbname = "mymango"
        sheetname ="test2"
        # 创建MONGODB数据库链接
        client = MongoClient(host=host, port=port)
        # 指定数据库
        mydb = client[dbname]
        # 存放数据的数据库表名
        self.post = mydb[sheetname]

    def insert_dd_name(self,data):
        try:
            self.post.insert(data)
        except Exception as e:
            print('发生了异常：',e)