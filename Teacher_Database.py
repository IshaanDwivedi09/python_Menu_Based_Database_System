import menu
import Teacher_Database
import mysql.connector as co
def TEA_DATA():
    while True:
        print("\n\n\t\t===========================================================")
        print("\t\t########=============Teacher Database==============########")
        print("\t\t===========================================================")
        print("\n\n\t\t1: Add a Teacher's Record")
        print("\t\t2: Show Teachers Details")
        print("\t\t3: Search Teacher Records")
        print("\t\t4: Delete a Teacher's Record")
        print("\t\t5: Edit Teacher Records")
        print("\t\t6: Back to HomePage")
        print("\t\t___________________________________________________________")
        choice=int(input("\n\t\tEnter your choice = "))
        if choice==1:
            Teacher_Database.Add_Tea_Records()
        elif choice==2:
            Teacher_Database.Show_Tea_Details()
        elif choice==3:
            Teacher_Database.Search_Tea_Details()
        elif choice==4:
            Teacher_Database.Delete_Tea_Details()
        elif choice==5:
            Teacher_Database.Edit_Tea_Details()
        elif choice==6:
            return
        else:
            print("\t\tError: Invalid Choice. Please Try again.....")
            conti="\t\tPress any key to return to Main Menu"
def Add_Tea_Records():
    try:
        mycon=co.connect(host="localhost", user="root", passwd="", database="Alpha")
        cursor=mycon.cursor()
        year=input('\t\tEnter Joining Year = ')
        tename=input("\t\tEnter Teacher's Name = ")
        teclass=input('\t\tEnter Class alloted= ')
        tesalary=input('\t\tEnter Salary = ')
        teid=input("\t\tEnter Teacher's ID = ")
        sub=input('\t\tEnter Subject alloted = ')

        query="insert into Teacher_Database(year,tename,teclass,tesalary,teid,sub)values('{}','{}','{}','{}','{}','{}')".format(year,tename,teclass,tesalary,teid,sub)
        cursor.execute(query)
        mycon.commit()
        mycon.close()
        cursor.close()
        print('\t\tNew Record added to the Database')
    except:
        print('\t\tError')
def Show_Tea_Details():
    mycon=co.connect(host="localhost", user="root", passwd="", database="Alpha")
    cursor=mycon.cursor()
    cursor.execute("select * from Teacher_Database" )
    data = cursor.fetchall()
    for row in data:
        print(row)
def Search_Tea_Details():
    mycon=co.connect(host="localhost", user="root", passwd="", database="Alpha")
    cursor=mycon.cursor()
    ac=input("\t\tEnter Teacher's ID = ")
    st= "select * from Teacher_Database where teid='%s'"%(ac) 
    cursor.execute(st)
    data = cursor.fetchall()
    print (data)
def Delete_Tea_Details():
    mycon=co.connect(host="localhost", user="root", passwd="", database="Alpha")
    cursor=mycon.cursor()
    ac=input("\t\tEnter Teacher's ID = ")
    st= "delete from Teacher_Database where teid='%s'"%(ac) 
    cursor.execute(st)
    mycon.commit()
    print ('\t\tData Deleted Successfully')
def Edit_Tea_Details():
    mycon=co.connect(host="localhost", user="root", passwd="", database="Alpha")
    cursor=mycon.cursor()
    print("\t\t1: Edit Year")
    print("\t\t2: Edit Name")
    print("\t\t3: Edit Class alloted")
    print("\t\t4: Edit Salary Paid")
    print("\t\t5: Edit Teacher's ID")
    print("\t\t6: Edit Subject alloted") 
    print("\t\t7: Return")
    print("\t\t______________________________________________________________________")
    choice=int(input("\n\t\tEnter your choice"))
    if choice==1:
        Teacher_Database.edit_year()
    elif choice==2:
        Teacher_Database.edit_tename()
    elif choice==3:
        Teacher_Database.edit_teclass()
    elif choice==4:
        Teacher_Database.edit_tesalary()
    elif choice==5:
        Teacher_Database.edit_teid()
    elif choice==6:
        Student_Database.edit_sub()
    elif choice==11:
            return
    else:
        print("\t\tError: Invalid Choice. Please Try again.....")
        conti="\t\tPress any key to Return"
def edit_year():
    mycon=co.connect(host="localhost", user="root", passwd="", database="Alpha")
    cursor=mycon.cursor()
    ac=input("\t\tEnter Teacher's ID = ")
    nm=input('\t\tEnter Correct Year = ')
    st= "update Teacher_Database set year='%s' where teid='%s'"%(nm,ac) 
    cursor.execute(st)
    mycon.commit()
    print ('\t\tData Updated Successfully')
def edit_tename():
    mycon=co.connect(host="localhost", user="root", passwd="", database="Alpha")
    cursor=mycon.cursor()
    ac=input("\t\tEnter Teacher's ID = ")
    nm=input('\t\tEnter Correct Name = ')
    st= "update Teacher_Database set tename='%s' where teid='%s'"%(nm,ac) 
    cursor.execute(st)
    mycon.commit()
    print ('\t\tData Updated Successfully')
def edit_teclass():
    mycon=co.connect(host="localhost", user="root", passwd="", database="Alpha")
    cursor=mycon.cursor()
    ac=input("\t\tEnter Teacher's ID = ")
    nm=input('\t\tEnter Correct Class alloted = ')
    st= "update Teacher_Database set teclass='%s' where teid='%s'"%(nm,ac) 
    cursor.execute(st)
    mycon.commit()
    print ('\t\tData Updated Successfully')
def edit_tesalary():
    mycon=co.connect(host="localhost", user="root", passwd="", database="Alpha")
    cursor=mycon.cursor()
    ac=input("\t\tEnter Teacher's ID = ")
    nm=input('\t\tEnter Correct Salary = ')
    st= "update Teacher_Database set tesalary='%s' where teid='%s'"%(nm,ac) 
    cursor.execute(st)
    mycon.commit()
    print ('\t\tData Updated Successfully')
def edit_teid():
    mycon=co.connect(host="localhost", user="root", passwd="", database="Alpha")
    cursor=mycon.cursor()
    ac=input("\t\tEnter Current Teacher's ID = ")
    nm=input("\t\tEnter Correct Teacher's ID = ")
    st= "update Teacher_Database set teid='%s' where teid='%s'"%(nm,ac) 
    cursor.execute(st)
    mycon.commit()
    print ('\t\tData Updated Successfully')
def edit_sub():
    mycon=co.connect(host="localhost", user="root", passwd="", database="Alpha")
    cursor=mycon.cursor()
    ac=input("\t\tEnter Teacher's ID = ")
    nm=input('\t\tEnter New Subject alloted = ')
    st= "update Teacher_Database set sub='%s' where teid='%s'"%(nm,ac) 
    cursor.execute(st)
    mycon.commit()
    print ('\t\tData Updated Successfully')

    
    
    
