from pymysql import *


def main():
	# 创建connect连接对象
	conn = connect(host="localhost", user="root", password="mysql", database="jing_dong_test")
	
	#开启自动提交事务
	conn.autocommit(1)

	# 创建cursor游标对象
	cs = conn.cursor()

	sql = "insert into money values (0, 222)"
	cs.execute(sql)
	# conn.commit()

	# 关闭游标对象
	cs.close()
	# 关闭连接对象
	conn.close()

if __name__ == "__main__":
	main()