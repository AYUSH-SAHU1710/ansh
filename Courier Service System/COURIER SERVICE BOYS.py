import mysql.connector as  sql
conn=sql.connect(host= 'localhost' ,user= 'root' ,passwd= '1234', database='courier' )
cust1=conn.cursor()

#cust1.execute("insert into couriers3 values('Meerut' ,'Sahil' ,'8749834543')")
#cust1.execute("insert into couriers3 values('ghaziabad', 'dinesh', '8749845783')")
#cust1.execute("insert into couriers3 values('noida' , 'krishna', '8756904543')")
#cust1.execute("insert into couriers3 values('delhi', 'Sahil', '9587498343')")
#cust1.execute("insert into couriers3 values('chennai', 'ganesh', '9049834543')")
#cust1.execute("insert into couriers3 values('mumbai','yash', '9809834543')")
#cust1.execute("insert into couriers3 values('bangalore', 'naitik', '8746784503')")
#cust1.execute("insert into couriers3 values('jaipur', 'gaurav' ,'8749838943')")
#cust1.execute("insert into couriers3 values('amritsar', 'shahjahan', '8749838793')")
#cust1.execute("insert into couriers3 values('muzzafarnagar','ajay', '9587498343')")
#cust1.execute("insert into couriers3 values('jammu', 'ankit','8749889743')")
#cust1.execute("insert into couriers3 values('mirzapur', 'faizal' , '8659834543')")
#cust1.execute("insert into couriers3 values('agra', 'pawan' , '8749836753')")
#cust1.execute("insert into couriers3 values('sahranpur', 'lakshay', '8749890423')")
#cust1.execute("insert into couriers3 values('indore', 'bavesh', '7699834543')")
#cust1.execute("insert into couriers3 values('hyderabad' ,'akshay' ,'8749867583')")
#cust1.execute("insert into couriers3 values('noida' , 'ravi', '9756904543')")
#cust1.execute("insert into couriers3 values('Meerut' ,'rohan' ,'8790734543')")
conn.commit()