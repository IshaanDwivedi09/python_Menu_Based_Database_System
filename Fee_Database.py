import menu
import Admission_Data
import Student_Database
import Fee_Database
import mysql.connector as co
def FEE_DATA():
    while True:
        #fee_details.clrScreen()
        print("\t\t==================================================================")
        print("\t\t########===============Student Fee Database===============########")
        print("\t\t==================================================================")
        print("\n\n\t\t1: Fee Deposit")
        print("\t\t2: Fee Details")
        print("\t\t3: Fee details of particular student")
        print("\t\t4: Return to Main Menu")
        print("\t\t__________________________________________________________________")
        choice=int(input("\n\t\tEnter Your Choice = "))
        if choice==1:
            Fee_Database.fees_deposit()
        elif choice==2:
            Fee_Database.fdetails()
        elif choice==3:
            Fee_Database.fee_particular()
        elif choice==4:
            return
        else:
            print("\t\tError: Invalid Choice. Please Try again.....")
            conti="\t\tPress any key to return to Main Menu"
def fees_deposit():
    try:
        mycon=co.connect(host="localhost", user="root", passwd="", database="Alpha")
        cursor=mycon.cursor()
        session=input('\t\tEnter Academic Session(eg,2019-20) = ')
        stclass=input('\t\tEnter Class = ')
        stsec=input('\t\tEnter Section = ')
        stroll=input('\t\tEnter Roll No. = ')
        paymenttype=input('\t\tEnter type of Payment(Tution/ Renewal /Travel /Other )\n\t\t--')
        amount=input('\t\tEnter Deposited Amount = ')
        dat=input('\t\tEnter Date(YYYY/MM/DD) = ')

        query="insert into Fee_Database(session,stclass,stsec,stroll,paymenttype,amount,dat)values('{}','{}','{}','{}','{}','{}','{}')".format(session,stclass,stsec,stroll,paymenttype,amount,dat)
        cursor.execute(query)
        mycon.commit()
        mycon.close()
        cursor.close()
        print('\t\t\tRecord has been saved in the Database')
    except:
        print('\t\tError')
    
def fdetails():
    mycon=co.connect(host="localhost", user="root", passwd="", database="Alpha")
    cursor=mycon.cursor()
    cursor.execute("select * from Fee_Database" )
    data = cursor.fetchall()
    for row in data:
        print(row)
def fee_particular():
    mycon=co.connect(host="localhost", user="root", passwd="", database="Alpha")
    cursor=mycon.cursor()
    ac=input('\t\tEnter Roll No. = ')
    cl=input('\t\tEnter Class = ')
    sc=input('\t\tEnter Section = ')
    st= "select * from Fee_Database where stroll='%s' and stclass='%s' and stsec='%s'"%(ac,cl,sc) 
    cursor.execute(st)
    data = cursor.fetchall()
    print (data)
    
