import pymongo


def test_1():
    # 实现 pymongo 数据库的增删改查
    # 连接数据库
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    # 创建/使用数据库（有数据插入才会被创建）
    mydb = myclient["stark"]
    # 创建/使用集合（有数据插入才会被创建）
    mycol = mydb["sites"]
    try:
        # 插入一条数据
        data = {"name": "stark", "email": "starktan@163.com", "sn": 1}
        x = mycol.insert_one(data)
        # 插入的id
        print(x.inserted_id)
        # 插入多条数据
        data_list = [
            {"name": "stark", "email": "starktan@163.com", "sn": 2},
            {"_id": "my_id", "name": "stark", "email": "starktan@163.com", "sn": 3},
        ]
        x = mycol.insert_many(data_list)
        # 输出插入的所有文档对应的 _id 值
        print(x.inserted_ids)
        # 查询所有数据
        for x in mycol.find():
            print(x)
        print("*"*100)
        # 查询指定数据 （支持正则表达式）
        for x in mycol.find({"name": "stark", "sn": 3}):
            print(x)
        print("*" * 100)
        # 查询指定数据,获取指定字段 （除了 _id 你不能在一个对象中同时指定 0 和 1，如果你设置了一个字段为 0，则其他都为 1，反之亦然。）
        for x in mycol.find({"name": "stark", "sn": 3}, {"_id": 0, "name": 1}):
            print(x)
        print("*" * 100)
        # 修改第一条匹配数据
        myquery = {"sn": 1}
        newvalues = {"$set": {"name": "starktan"}}
        mycol.update_one(myquery, newvalues)
        # 修改所有匹配数据
        myquery = {"name": {"$regex": "^stark$"}}
        newvalues = {"$set": {"alexa": "123"}}
        mycol.update_many(myquery, newvalues)
        for x in mycol.find():
            print(x)
        print("*" * 100)
        # 排序
        mydoc = mycol.find().sort("sn", -1)
        for x in mydoc:
            print(x)
        print("*" * 100)
        # 修改第一条匹配数据
        mycol.delete_one({"name": "starktan"})
        # 修改第一条匹配
        mycol.delete_many({"name": "stark"})
        for x in mycol.find():
            print(x)
        print("*" * 100)
    finally:
        # 数据库列表
        dblist = myclient.list_database_names()
        print(dblist)
        # 数据库中的集合列表
        collist = mydb.list_collection_names()
        print(collist)
        # 删除 集合
        mydb.drop_collection("sites")
        # 删除 数据库
        myclient.drop_database("stark")


test_1()
