#db connection
import pymysql

db = pymysql.connect(user="root",host="localhost",port=3306,password="root",database="praveen")
cur = db.cursor()
# cur.execute(""" create database praveen """)
# cur.execute(""" create table info(name varchar(50),phone int, dept varchar(50))""")
# cur.execute(""" insert into info values("Praveen",98765,"Mech") """)
# cur.execute(""" insert into info values("Kumar",76543,"EEE") """)
# cur.execute(""" insert into info values("Vidya",78907,"ECO") """)
# cur.execute(""" insert into info values("Vishnu Priya",12378,"EEE") """)
# cur.execute(""" update info set dept="ECE" where name="Vidya" """)
# cur.execute(""" delete from info where name='Kumar' """)
# cur.execute("""alter table info add column id int """)
# cur.execute("""alter table info drop column id """)
# cur.execute("select * from info")
# data = cur.fetchall()
# cur.execute(""" select * from info where name="Praveen" """)
# data = cur.fetchone()
# cur.execute("select * from info")
# data = cur.fetchmany(3)
# print(data)
# db.commit()
# db.close()

print("Column removed")












