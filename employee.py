import pymysql

def CreateConnection():
    return pymysql.connect(host="localhost", database="core",user="root",password="",port=3306)


def createTable():
    conn = CreateConnection()
    cursor = conn.cursor()
    cursor.execute("create table emp(email varchar(20),password varchar(20),phone bigint(10),city varchar(20), address varchar(20))")
    conn.commit()
    print("Table Created...")
    conn.close()


def insertData(email,password,phone,city,address):
    conn = CreateConnection()
    query = "insert into emp(email,password,phone,city,address)values(%s,%s,%s,%s,%s)"
    args = (email,password,phone,city,address)
    cursor = conn.cursor()
    cursor.execute(query,args)
    conn.commit()
    print("Data Inserted")
    conn.close()


def getAllEmp():
    conn = CreateConnection()
    cursor = conn.cursor()
    cursor.execute("select * from emp")
    row = cursor.fetchall()
    for i in row:
        print(i)
    conn.close()

def update_table(email,password,phone,city,address):
    query="update emp set password=%s,phone=%s, city=%s, address=%s where email=%s"
    args=(email,password,phone,city,address)
    conn=CreateConnection()
    cursor=conn.cursor()
    cursor.execute(query,args)
    conn.commit()
    conn.close()

def delete_table(email):
    query="delete from emp where email=%s"
    args = (email)
    conn=CreateConnection()
    cursor=conn.cursor()
    cursor.execute(query,args)
    conn.commit()
    conn.close()

# # createTable()
# e = input("Email :")
# p = input("Password :")
# ph = int(input("Phone :"))
# c = input("City :")
# a = input("Address :")

# insertData(e,p,ph,c,a)
getAllEmp()
# update_table(p,ph,c,a,e)
# delete_table(e)

