import menu
import Fee_Database
import Student_Database
import Teacher_Database
import Admission_Data
while True:
    #menu.clrscreen()
    print ("\t\t===================================================")
    print ("\t\t########======Welcome to the Database======########")
    print ("\t\t===================================================")
    print ("\n\n\t\t            SRM Institute of Technology           ")
    print ("\t\t           -----------------------------          ")
    print ("\n\t\t1.  Admission Data")
    print ("\t\t2.  Student Database")
    print ("\t\t3.  Teacher Database")
    print ("\t\t4.  Fee Database")
    print ("\t\t5.  Exit")
    print ("\t\t___________________________________________________")
    choice=int(input("\n\t\t Enter Your Choice = "))
    if choice==1:
        Admission_Data.ADM_DATA()
    elif choice==2:
        Student_Database.STU_DATA()
    elif choice==3:
        Teacher_Database.TEA_DATA()
    elif choice==4:
        Fee_Database.FEE_DATA()
    elif choice==5:
        break
    else:
        print("\t\tError: Invalid Choice try again..........")
        conti=input("\t\tPress any key to continue")


