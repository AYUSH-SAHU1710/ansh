import mysql.connector as  sql
conn=sql.connect(host= 'localhost' ,user= 'root' ,passwd= '1234', database='courier' )
cust1=conn.cursor()
#cust1.execute("insert into couriers2 values(' 1kg' ,' 50Rs' )")
#cust1.execute("insert into couriers2 values('2kg','75Rs')")
#cust1.execute("insert into couriers2 values('3kg','100Rs')")
#cust1.execute("insert into couriers2 values('4kg','125Rs')")
#cust1.execute("insert into couriers2 values('5kg','150Rs')")
#cust1.execute("insert into couriers2 values('10kg','275Rs')")
#cust1.execute("insert into couriers2 values('20kg','525Rs')")
#cust1.execute("insert into couriers2 values('30kg','775Rs')")
#cust1.execute("insert into couriers2 values('40kg','1025Rs')")
#cust1.execute("insert into couriers2 values('50kg','1275Rs')")
#cust1.execute("insert into couriers2 values('100kg','2520Rs')")
#cust1.execute("insert into couriers2 values('150kg','3770Rs')")
#cust1.execute("insert into couriers2 values('200kg','5020Rs')")
#cust1.execute("insert into couriers2 values('250kg','6270Rs')")
#cust1.execute("insert into couriers2 values('300kg','7520Rs')")
#cust1.execute("insert into couriers2 values('350kg','8770Rs')")
#cust1.execute("insert into couriers2 values('400kg','10020Rs')")
#cust1.execute("insert into couriers2 values('450kg','11270Rs')")
#cust1.execute("insert into couriers2 values('500kg','12520Rs')")
conn.commit()
