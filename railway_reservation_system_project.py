from numpy import source
import pandas as pd
import mysql.connector as sql
conn = sql.connect(host='localhost',user = 'root',passwd='Swetha@2002',auth_plugin='mysql_native_password',database = 'railway_reservation')
if conn.is_connected():
    print('Mysql successfully connected')


def menu():
    print()
    print("*****************************************************************************")
    print("                             RAILWAY RESERVATION SYSTEM")
    print("1.CRETAE TABLE PASSENGERS")
    print("2.ADD PASSENGERS DETAILS")
    print("3.CREATE TABLE TRAIN DETAILS")
    print("4.ADD NEW TRAIN DETAILS")
    print("5.SHOW ALL TRAIN DETAILS")
    print("6.SHOW ALL PASSENGERS DETAILS")
    print("7.SHOW PNRNO")
    print("8.RESERVATION OF TICKET")
    print("9.CANCELLATION OF TICKET")    
    print("10.DELETE PASSENGERS DETAILS")
    print("11.DELETE TRAINS DETAILS")
menu()

def create_passengers():
    c1=conn.cursor()
    c1.execute('create table if not exists passengers(pname varchar(30),age varchar(25),train_no varchar(30),noof_pass varchar(25),clas varchar(25),destination varchar(30),amt varchar(20),status varchar(25),pnrno varchar(25))')
    print('Passengers Table created')
    
    
def add_passengers():
    c1=conn.cursor()
    l=[]
    pname = input("Enter Name :")
    l.append(pname)
    age = input("Enter Age :")
    l.append(age)
    train_no = input("Enter train number :")
    l.append(train_no)
    noof_pass = input("Enter number of passengers :")
    l.append(noof_pass)
    clas = input("Enter Class :")
    l.append(clas)
    destination = input("Enter Destination :")
    l.append(destination)
    amt = input("Enter fare :")
    l.append(amt)
    status = input("Enter status :")
    l.append(status)
    pnrno = input("Enter pnr number :")
    l.append(pnrno)
    pas = (l)
    sql = "insert into passengers(pname,age,train_no,noof_pass,clas,destination,amt,status,pnrno) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    c1.execute(sql,pas)
    conn.commit()
    print('RECORD OF PASSENGERS INSERTED')
    df = pd.read_sql("SELECT * FROM passengers",conn)
    print(df)
    
def create_trainsdetail():
    c1 = conn.cursor()
    c1.execute('create table if not exists trainsdetail(tname varchar(30),tnum varchar(25),source varchar(30),destination varchar(30),fare varchar(20),ac1 varchar(25),ac2 varchar(30),slp varchar(25))')
    print('TABLE FOR TRAINS DETAILS CREATED')
    
def add_trainsdetail():
   
    c1=conn.cursor()
    l=[]
    tname = input("Enter train name:")
    l.append(tname)
    tnum=input("Enter train number:")
    l.append(tnum)
    source = input("Enter source train:")
    l.append(source)
    destination=input("Enter destination of train:")
    l.append(destination)
    fare=input("Enter fare:")
    l.append(fare)
    ac1=input("Enter no.of seats for Ac1:")
    l.append(ac1)
    ac2=input("Enter no.of seats for AC2:")
    l.append(ac2)
    slp = input("Enter no.of seats for sleeper:")
    l.append(slp)
    f=(l)
    sql= "insert into trainsdetail(tname,tnum,source,destination,fare,ac1,ac2,slp) values(%s,%s,%s,%s,%s,%s,%s,%s)"
    c1.execute(sql,f)
    conn.commit()
    print('Record inserted in trainsdetails')
    df = pd.read_sql("select * from trainsdetail",conn)
    print(df)

def show_traindetail():
    print("ALL TRAIN DETAILS")
    df = pd.read_sql("SELECT * FROM trainsdetail",conn)
    print(df)
    
def show_passengers_detail():
   
    print("ALL PASSENGER DETAIL")
    df = pd.read_sql("SELECT * FROM passengers",conn)
    print(df)
    
    
def display_pnrno():

    c1 = conn.cursor()
    a=input("Enter PNR Number:")
    qry="""SELECT*FROM passengers where pnrno="%s" """ %(a)
    c1.execute(qry)
    rows = c1.fetchall()
    for i in rows:
            print(i)

def ticket_reservation():
    c1 = conn.cursor()
    tnum = int(input("Enter your choice of train number please->"))
    qry ="""select * from trainsdetail where tnum="%s" """%(tnum)
    c1.execute(qry)
    rows = c1.fetchall()
    for i in rows:
        print(i)
    if(tnum==12703):
        x = int(input("Enter your choice 0f ticket please->"))
        n = int(input("How many Tickets:"))
        if(x==1):
            print("you have chosen first class Ac ticket")
            s=700*n
        elif(x==2):
            print("you have chosen second class Ac ticket")
            s=600*n
        elif(x==3):
            print("you have chosen sleeper class ticket")
            s=450*n
        else:
            print("Invalid option")
        print("your total ticket price is = ",s,"\n")
    
    if tnum==17015:
        x = int(input("Enter your choice f ticket please->"))
        n = int(input("How many Tickets:"))
        if(x==1):
            print("you have chosen first class Ac ticket")
            s=560*n
        elif(x==2):
            print("you have chosen second class Ac ticket")
            s=450*n
        elif(x==3):
            print("you have chosen sleeper class ticket")
            s=320*n
        else:
            print("Invalid option")
        print("your total ticket price is = ",s,"\n")
    
    if tnum==12419 :
        x = int(input("Enter your choice f ticket please->"))
        n = int(input("How many Tickets:"))
        if(x==1):
            print("you have chosen first class Ac ticket")
            s=1100*n
        elif(x==2):
            print("you have chosen second class Ac ticket")
            s=890*n
        elif(x==3):
            print("you have chosen sleeper class ticket")
            s=750*n
        else:
            print("Invalid option")
        print("your total ticket price is = ",s,"\n")

    if tnum==22034 :
        x = int(input("Enter your choice f ticket please->"))
        n = int(input("How many Tickets:"))
        if(x==1):
            print("you have chosen first class Ac ticket")
            s=1000*n
        elif(x==2):
            print("you have chosen second class Ac ticket")
            s=800*n
        elif(x==3):
            print("you have chosen sleeper class ticket")
            s=650*n
        else:
            print("Invalid option")
        print("your total ticket price is = ",s,"\n") 

    if tnum==12009:
        x = int(input("Enter your choice f ticket please->"))
        n = int(input("How many Tickets:"))
        if(x==1):
            print("you have chosen first class Ac ticket")
            s=1000*n
        elif(x==2):
            print("you have chosen second class Ac ticket")
            s=800*n
        elif(x==3):
            print("you have chosen sleeper class ticket")
            s=550*n
        else:
            print("Invalid option")
        print("your total ticket price is = ",s,"\n")

   
    

def cancel():
   c1 = conn.cursor()
   prno = input("Enter PNR Number:")
   qry = """update passengers set status='CANCELLED' where pnrno = "%s" """%(prno)
   c1.execute(qry)
   conn.commit()
   q = pd.read_sql("Select * from passengers",conn)
   
   print(q)


def delete_passengers_details():
    print("**********Before changes in the database*************")
    df = pd.read_sql("SELECT*FROM passengers",conn)
    print(df)
    c1=conn.cursor()
    prno=input("Enter PNR Number:")
    qry = """delete from passengers where pnrno="%s" """%(prno)
    c1.execute(qry)
    conn.commit()
    print("***********After changes in the database**************")
    q = pd.read_sql("Select*From passengers",conn)
    print(q)



def delete_trains_details():
    print("**********Before changes in the database*************")
    df = pd.read_sql("SELECT*FROM trainsdetail",conn)
    print(df)
    c1 = conn.cursor()
    tnum=input("Enter Train Number:")
    qry = """delete from trainsdetail where tnum="%s" """%(tnum)
    c1.execute(qry)
    conn.commit()
    print("***********After changes in the database**************")
    q = pd.read_sql("Select*From trainsdetail",conn)
    print(q)



opt = int(input("Enter you choice:"))

while opt != 0:
    if opt==1:
        create_passengers()
    elif opt==2:
        add_passengers()
    elif opt==3:
        create_trainsdetail()
    elif opt==4:
        add_trainsdetail()
    elif opt==5:
        show_traindetail()
    elif opt==6:
        show_passengers_detail()
    elif opt==7:
        display_pnrno()
    elif opt==8:
        ticket_reservation()
    elif opt==9:
        cancel()
    elif opt==10:
        delete_passengers_details()
    elif opt==11:
        delete_trains_details()
    else:
        print("Invalid Option")

    opt = int(input("Enter you choice:"))
