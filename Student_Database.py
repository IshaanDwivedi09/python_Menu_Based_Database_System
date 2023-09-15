import menu
import Student_Database
import Admission_Data
import mysql.connector as co
def STU_DATA():
    while True:
        print("\n\n\t\t===========================================================")
        print("\t\t########=============Student Database==============########")
        print("\t\t===========================================================")
        print("\n\n\t\t1: Add a Student Record")
        print("\t\t2: Show Student Details")
        print("\t\t3: Search Student Records")
        print("\t\t4: Delete a Student Record")
        print("\t\t5: Edit Student Records")
        print("\t\t6: Back to HomePage")
        print("\t\t___________________________________________________________")
        choice=int(input("\n\t\tEnter your choice = "))
        if choice==1:
            Student_Database.Add_Records()
        elif choice==2:
            Student_Database.Show_Stu_Details()
        elif choice==3:
            Student_Database.Search_Stu_Details()
        elif choice==4:
            Student_Database.Delete_Stu_Details()
        elif choice==5:
            Student_Database.Edit_Stu_Details()
        elif choice==6:
            return
        else:
            print("\t\tError: Invalid Choice try again.....")
            conti="\t\tPress any key to return to Main Menu"
def Add_Records():
    try:
        mycon=co.connect(host="localhost", user="root", passwd="", database="Alpha")
        cursor=mycon.cursor()
        session=input('\t\tEnter Academic Session(eg,2019-20) = ')
        stname=input('\t\tEnter Student Name = ')
        stclass=input('\t\tEnter class = ')
        stsec=input('\t\tEnter section = ')
        stroll=input('\t\tEnter Roll No. = ')
        sub1=input('\t\tEnter Subject1 = ')
        sub2=input('\t\tEnter Subject2 = ')
        sub3=input('\t\tEnter Subject3 = ')
        sub4=input('\t\tEnter Subject4 = ')
        sub5=input('\t\tEnter Subject5 = ')

        query="insert into Student_Database(session,stname,stclass,stsec,stroll,sub1,sub2,sub3,sub4,sub5)values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(session,stname,stclass,stsec,stroll,sub1,sub2,sub3,sub4,sub5)
        cursor.execute(query)
        mycon.commit()
        mycon.close()
        cursor.close()
        print('\t\tNew Record added to the Student Database')
    except:
        print('\t\tError')
def Show_Stu_Details():
    mycon=co.connect(host="localhost", user="root", passwd="", database="Alpha")
    cursor=mycon.cursor()
    cursor.execute("select * from Student_Database" )
    data = cursor.fetchall()
    for row in data:
        print(row)
def Search_Stu_Details():
    mycon=co.connect(host="localhost", user="root", passwd="", database="Alpha")
    cursor=mycon.cursor()
    ac=input('\t\tEnter Roll No. = ')
    st= "select * from Student_Database where stroll='%s'"%(ac) 
    cursor.execute(st)
    data = cursor.fetchall()
    print (data)
def Delete_Stu_Details():
    mycon=co.connect(host="localhost", user="root", passwd="", database="Alpha")
    cursor=mycon.cursor()
    ac=input('\t\tEnetr Roll No.= ')
    st= "delete from Student_Database where stroll='%s'"%(ac) 
    cursor.execute(st)
    mycon.commit()
    print ('\t\tData Deleted successfully')
def Edit_Stu_Details():
    mycon=co.connect(host="localhost", user="root", passwd="", database="Alpha")
    cursor=mycon.cursor()
    print("\t\t1: Edit Session = ")
    print("\t\t2: Edit Name = ")
    print("\t\t3: Edit Class = ")
    print("\t\t4: Edit Section = ")
    print("\t\t5: Edit Roll No. = ")
    print("\t\t6: Edit Subject1 = ")
    print("\t\t7: Edit Subject2 = ")
    print("\t\t8: Edit Subject3 = ")
    print("\t\t9: Edit Subject4 = ")
    print("\t\t10: Edit Subject5 = ") 
    print("\t\t11: Return = ")
    print("\t\t______________________________________________________________________")
    choice=int(input("\t\tEnter your choice"))
    if choice==1:
        Student_Database.edit_session()
    elif choice==2:
        Student_Database.edit_name()
    elif choice==3:
        Student_Database.edit_class()
    elif choice==4:
        Student_Database.edit_section()
    elif choice==5:
        Student_Database.edit_rno()
    elif choice==6:
        Student_Database.edit_sub1()
    elif choice==7:
        Student_Database.edit_sub2()
    elif choice==8:
        Student_Database.edit_sub3()
    elif choice==9:
        Student_Database.edit_sub4()
    elif choice==10:
        Student_Database.edit_sub5()
    elif choice==11:
            return
    else:
        print("\t\tError: Invalid Choice. Please Try again.....")
        conti="\t\tPress any key to Return"
def edit_session():
    mycon=co.connect(host="localhost", user="root", passwd="", database="Alpha")
    cursor=mycon.cursor()
    ac=input('\t\tEnter Roll No. = ')
    nm=input('\t\tEnter Correct Session = ')
    st= "update Student_Database set session='%s' where stroll='%s'"%(nm,ac) 
    cursor.execute(st)
    mycon.commit()
    print ('\t\tData Updated Successfully')
def edit_name():
    mycon=co.connect(host="localhost", user="root", passwd="", database="Alpha")
    cursor=mycon.cursor()
    ac=input('\t\tEnter Roll No. = ')
    nm=input('\t\tEnter Correct Name = ')
    st= "update Student_Database set stname='%s' where stroll='%s'"%(nm,ac) 
    cursor.execute(st)
    mycon.commit()
    print ('\t\tData Updated Successfully')
def edit_class():
    mycon=co.connect(host="localhost", user="root", passwd="", database="Alpha")
    cursor=mycon.cursor()
    ac=input('\t\tEnter Roll No. = ')
    nm=input('\t\tEnter Correct Class')
    st= "update Student_Database set stclass='%s' where stroll='%s'"%(nm,ac) 
    cursor.execute(st)
    mycon.commit()
    print ('\t\tData Updated Successfully')
def edit_section():
    mycon=co.connect(host="localhost", user="root", passwd="", database="Alpha")
    cursor=mycon.cursor()
    ac=input('\t\tEnter Roll No. = ')
    nm=input('\t\tEnter Correct Section = ')
    st= "update Student_Database set stsec='%s' where stroll='%s'"%(nm,ac) 
    cursor.execute(st)
    mycon.commit()
    print ('\t\tData Updated Successfully')
def edit_rno():
    mycon=co.connect(host="localhost", user="root", passwd="", database="Alpha")
    cursor=mycon.cursor()
    ac=input('\t\tEnter Current Roll No. = ')
    nm=input('\t\tEnter Correct Roll No. = ')
    st= "update Student_Database set stroll='%s' where stroll='%s'"%(nm,ac) 
    cursor.execute(st)
    mycon.commit()
    print ('\t\tData Updated Successfully')
def edit_sub1():
    mycon=co.connect(host="localhost", user="root", passwd="", database="Alpha")
    cursor=mycon.cursor()
    ac=input('\t\tEnter Roll No. = ')
    nm=input('\t\tEnter Correct Subject1 = ')
    st= "update Student_Database set sub1='%s' where stroll='%s'"%(nm,ac) 
    cursor.execute(st)
    mycon.commit()
    print ('\t\tData Updated Successfully')
def edit_sub2():
    mycon=co.connect(host="localhost", user="root", passwd="", database="Alpha")
    cursor=mycon.cursor()
    ac=input('\t\tEnter Roll No. = ')
    nm=input('\t\tEnter Correct Subject2 = ')
    st= "update Student_Database set sub2='%s' where stroll='%s'"%(nm,ac) 
    cursor.execute(st)
    mycon.commit()
    print ('\t\tData Updated Successfully')
def edit_sub3():
    mycon=co.connect(host="localhost", user="root", passwd="", database="Alpha")
    cursor=mycon.cursor()
    ac=input('\t\tEnter Roll No. = ')
    nm=input('\t\tEnter Correct Subject3 = ')
    st= "update Student_Database set sub3='%s' where stroll='%s'"%(nm,ac) 
    cursor.execute(st)
    mycon.commit()
    print ('\t\tData Updated Successfully')
def edit_sub4():
    mycon=co.connect(host="localhost", user="root", passwd="", database="Alpha")
    cursor=mycon.cursor()
    ac=input('\t\tEnter Roll No. = ')
    nm=input('\t\tEnter Correct Subject4 = ')
    st= "update Student_Database set sub4='%s' where stroll='%s'"%(nm,ac) 
    cursor.execute(st)
    mycon.commit()
    print ('\t\tData Updated Successfully')
def edit_sub5():
    mycon=co.connect(host="localhost", user="root", passwd="", database="Alpha")
    cursor=mycon.cursor()
    ac=input('\t\tEnter Roll No. = ')
    nm=input('\t\tEnter Correct Subject5 = ')
    st= "update Student_Database set sub5='%s' where stroll='%s'"%(nm,ac) 
    cursor.execute(st)
    mycon.commit()
    print ('\t\tData Updated Successfully')
    
    
    
