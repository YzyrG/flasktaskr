import sqlite3
from called_config import DATABASE_PATH

with sqlite3.connect(DATABASE_PATH) as connection:
	# 创建一个cursor实例，用于执行sql命令
	c = connection.cursor()

	# 创建新表
	c.execute("""CREATE TABLE tasks 
			(
				task_id INTEGER PRIMARY KEY AUTOINCREMENT,
				name TEXT NOT NULL,
				due_date TEXT NOT NULL,
				priority INTEGER NOT NULL,
				status INTEGER NOT NULL
			)

		""")

	#插入虚拟数据
	c.execute(
		'INSERT INTO tasks(name, due_date, priority, status)'
		'VALUES("Finish this tutorial", "06/14/2021", 10, 1)'
		)
	c.execute(
		'INSERT INTO tasks(name, due_date, priority, status)'
		'VALUES("Finish BBC learning english lower-intermediate course", "09/20/2021", 8, 1)'
		)
