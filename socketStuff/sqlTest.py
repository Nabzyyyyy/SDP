import mysql.connector as mc

connection = mc.connect (host = "localhost",
			user = "pytester",
			passwd = "password",
			db = "company")
cursor = connection.cursor()
cursor.execute ("SELECT VERSION()")
row = cursor.fetchone()
print("server version:", row[0])
cursor.close()
connection.close()
