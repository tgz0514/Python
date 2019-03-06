from pymongo import MongoClient

# 建立连接
client = MongoClient(host="127.0.0.1",port=27017)
collection = client["test1"]["t251"] #第一个参数test1是要连接的数据库名，第二个参数是集合名

#插入一条数据
ret1 = collection.insert({"name":"向明","age":18}) #这里python字典键的引号不能省略
# print(ret1) #5b6e86b6569e3e2098f80cbb 打印的是id号

# 插入多条数据
data_list= [{"name":"test{}".format(i)} for i in range(10)]
ret2 = collection.insert_many(data_list)
# print(ret2)

#查询一个记录
# t = collection.find_one({"name":"向明"})
# print(t)
# 查询所有记录

t = collection.find({"name":"向明"})
print(t)  #<pymongo.cursor.Cursor object at 0x0000000000B0B908> 游标对象

# for i in t:
#     print(i)

# 游标对象，只能遍历一次
# for j in t:
#     print(j,"*"*100)
print(list(t))