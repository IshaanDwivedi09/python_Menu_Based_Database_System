import menu
import Student_Database
import Admission_Data
import mysql.connector as co
def ADM_DATA():
    while True:
        print ("\n\n\t\t====================================================")
        print ("\t\t########===========Admission Data===========########")
        print ("\t\t====================================================")
        print ("\n\t\t1: Create Student Admission Form")
        print ("\t\t2: Show Admission Details")
        print ("\t\t3: Search For Admission Details")
        print ("\t\t4: Delete a Record")
        print ("\t\t5: Update a Admission Form")
        print ("\t\t6: Back to HomePage")
        print ("\t\t____________________________________________________")
        choice=int(input("\t\tEnter Your Choice = "))
        if choice==1:
            Admission_Data.admin_details()
        elif choice==2:
            Admission_Data.show_admin_details()
        elif choice==3:
            Admission_Data.search_admin_details()
        elif choice==4:
            Admission_Data.delete_admin_details()
        elif choice==5:
            Admission_Data.edit_admin_details()
        elif choice==6:
            return
        else:
            print("\t\tError: Invalid Choice. Please Try again.....")
            conti="\t\tPress any key to Return to the HomePage"
def admin_details():
    try:
        mycon=co.connect(host="localhost", user="root", passwd="", database="Alpha")
        cursor=mycon.cursor() 
        adno=input('\t\tEnter Admission No. = ')
        rno=int(input('\t\tEnter Roll No. = '))
        sname=input('\t\tEnter Student Name = ')
        address=input('\t\tEnter Address = ')
        phon=input('\t\tEnter Phone No. = ')
        clas=input('\t\tEnter Class = ')
        sec=input('\t\tEnter Sec = ')

        query="insert into Admission_Data(adno,rno,sname,address,phon,clas,sec)values('{}','{}','{}','{}','{}','{}','{}')".format(adno,rno,sname,address,phon,clas,sec)
        cursor.execute(query)
        mycon.commit()
        mycon.close()
        cursor.close()
        print('\t\tNew Record has been added in the Admission Data')
    except:
        print('\t\tError')
    #except co.error as err:
        #if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
         #   print("Something is invalid....Re.Check User name or password")
        #if err.errno==errorcode.ER_BAD_DB_ERROR:
         #   print("Admission_Data:DATABASE does not exist..")
        #else:
            #print(err)
def show_admin_details():
    mycon=co.connect(host="localhost", user="root", passwd="", database="Alpha")
    cursor=mycon.cursor()
    cursor.execute("select * from Admission_Data" )
    data = cursor.fetchall()
    for row in data:
        print(row)
def search_admin_details():
    mycon=co.connect(host="localhost", user="root", passwd="", database="Alpha")
    cursor=mycon.cursor()
    ac=input('\t\tEnter Admission No. = ')
    st= "select * from Admission_Data where adno='%s'"%(ac) 
    cursor.execute(st)
    data = cursor.fetchall()
    print (data)
def delete_admin_details():
    mycon=co.connect(host="localhost", user="root", passwd="", database="Alpha")
    cursor=mycon.cursor()
    ac=input('\t\tEnter Admission No = ')
    st= "delete from Admission_Data where adno='%s'"%(ac) 
    cursor.execute(st)
    mycon.commit()
    print ('\t\t\t\tData Deleted Successfully')
def edit_admin_details():
    mycon=co.connect(host="localhost", user="root", passwd="", database="Alpha")
    cursor=mycon.cursor()


    print("\t\t1: Edit Name = ")
    print("\t\t2: Edit Address = ")
    print("\t\t3: Phone No.")
    print("\t\t4: Go Back")
    print("\t\t_________________________________________________")
    choice=int(input("Enter your choice"))
    if choice==1:
        Admission_Data.edit_name()
    elif choice==2:
        Admission_Data.edit_address()
    elif choice==3:
        Admission_Data.edit_phno()
    elif choice==4:
            return
    else:
        print("\t\tError: Invalid Choice try again.....")
        conti="\t\tPress any key to return to "
def edit_name():
    mycon=co.connect(host="localhost", user="root", passwd="", database="Alpha")
    cursor=mycon.cursor()
    ac=input('\t\tEnter Admission No. = ')
    nm=input('\t\tEnter Correct Name = ')
    st= "update Admission_Data set sname='%s' where adno='%s'"%(nm,ac) 
    cursor.execute(st)
    mycon.commit()
    print ('\t\t\t\tData Updated Successfully')
def edit_address():
    mycon=co.connect(host="localhost", user="root", passwd="", database="Alpha")
    cursor=mycon.cursor()
    ac=input('\t\tEnter Admission No. = ')
    nm=input('\t\tEnter Correct Address = ')
    st= "update Admission_Data set address='%s' where adno='%s'"%(nm,ac) 
    cursor.execute(st)
    mycon.commit()
    print ('\t\t\t\tData updated successfully')
def edit_phno():
    mycon=co.connect(host="localhost", user="root", passwd="", database="Alpha")
    cursor=mycon.cursor()
    ac=input('\t\tEnter Admission No. = ')
    nm=input('\t\tEnter Correct Phone No. = ')
    st= "update Admission_Data set phon='%s' where adno='%s'"%(nm,ac) 
    cursor.execute(st)
    mycon.commit()
    print ('\t\t\t\tData Updated Successfully')
        
