import pymysql
db = pymysql.connect(user="root",passwd="",host='localhost',port=3306,database='demo')
cursor = db.cursor()
print("connected")                     

sql = "INSERT INTO emp(id,name,age) VALUES(7,'john',34)"

cursor.execute(sql)
db.commit()
