def institution():
    while True:
        print("\t\t--------{WELCOME TO TUTION MANAGEMENT SYSTEM}--------")
        a=input("====PRESS [y] TO CONTINUE====")
        print("===================================================================")
        if a=='y':
            print("(1) TEACHER MANAGEMENT")
            print("(2) STUDENT MANAGEMENT")
            print("(3) WORKER MANGEMENT")
            print("(4) BOOK MANAGEMENT")                                                                 
            print("(5) QUIT")
            choice=int(input("\t\t----------------ENTER THE CHOICE OF THE MANAGEMENT{1,2,3,4}------------------------>"))
            if choice==1:
                TMANG()
            elif choice==2:
                SMANG()
            elif choice==3:
                WMANG()
            elif choice==4:
                BMANG()
            else:
                print("DON'T FORGET TO CHARGE THE BATTERY :-)")
                break
                
        else:
            print("PLEASE  INSERT  THE  CORRECT  CHARACTER")
def TMANG():
     print("\t\t-------------------[WELCOME TO TEACHER MANAGMENT SYSTEM]------------------------")
     while True:
         a=input("PRESS [y] TO CONTINUE-->")
         if a=='y':
             print("::::::::::::::::[PLEASE SELECT ONE OF THE OPTION GIVEN BELOW]::::::::::::::::::")
             print("(1.)ADD THE NEW TEACHER TO THE INSTITUION ")
             print("(2.)REMOVE THE TEACHER FROM INSTITUTION ")
             print("(3.)UPDATE THE TEACHER ")
             print("(4.)SEARCH THE TEACHER FROM THE INSTITUION")
             print("(5.)DISPLAY THE TEACHER DEATAILS")
             print("(6.)GO BACK TO THE STARTING PAGE")
             print("--------------------------------------------------------------")
             option=int(input("ENTER THE OPTION YOU WANT TO CHOOSE--->>>"))
             if option==1:
                 def ADD():
                     import mysql.connector
                     con=mysql.connector.connect(host='localhost',user='root',passwd='12345678',database="institution")
                     mycursor=con.cursor()
                     TNO=int(input("ENTER THE TEACHER CODE:"))
                     TNAME=input("ENTER THE NAME OF THE TEACHER:")
                     SUBJECT=input("ENTER THE SUBJECT TEACHED BY THE TEACHER:")
                     PHONE_NUMBER=int(input("ENTER THE PHONE NUMBER OF THE TEACHER:"))
                     SALARY=int(input("ENTER THE SALARY OF THE TEACHER:"))
                     F=("insert into Teacher values(%s,%s,%s,%s,%s)")
                     DAT=(TNO,TNAME,SUBJECT,PHONE_NUMBER,SALARY)
                     mycursor.execute(F,DAT)
                     con.commit()
                     print("\t--RECORD ENTERED--")
                 ADD()
                     
             elif option==2:
                def REMOVE():
                   import mysql.connector
                   con=mysql.connector.connect(host='localhost',user='root',passwd='12345678',database="institution")
                   mycursor=con.cursor()
                   Tn=int(input("ENTER THE TNO OF THE TEACHER TO BE DELETED--->>>"))
                   f=("delete from Teacher where TNO='{}'".format(Tn))
                   mycursor.execute(f)
                   con.commit()   
                   print(mycursor.rowcount,"RECORD(S) DELETED")
                   print("{NO record is present}")
                REMOVE()
             elif option==3:
               def UPDATE():
                      import mysql.connector
                      con=mysql.connector.connect(host='localhost',user='root',passwd='12345678',database="institution")
                      mycursor=con.cursor()
                      Tn=int(input("--ENTER THE TNO OF THE TEACHER TO BE UPDATED-->>>"))
                      print("--Enter the new data--")
                      TNAME=input("Enter the teacher name:")
                      SUBJECT=input("Enter the subject teached by the teacher:")
                      PHONE_NUMBER=int(input("Enter the phone number of the teacher:"))
                      SALARY=int(input("Enter the salary of the teacher"))
                      f=("update teacher set TNAME='%s',SUBJECT='%s',PHONE_NUMBER='%s',SALARY='%s' where TNO='%s'"%(TNAME,SUBJECT,PHONE_NUMBER,SALARY,Tn))
                      mycursor.execute(f)
                      con.commit()
                      print("****DATA HAS BEEN UPDATED****")
               UPDATE()
             elif option==4:
               def SEARCH():
                   import mysql.connector
                   con=mysql.connector.connect(host='localhost',user='root',passwd='12345678',database="institution")
                   mycursor=con.cursor()
                   TN=input("--Enter the TEACHER NAME to be searched from-->>>")
                   f=("select * from Teacher where TNAME='%s'")%(TN)
                   mycursor.execute(f)
                   myrec=mycursor.fetchall()
                   for i in myrec:
                       l,m,n,o,p=i
                       print("----------------------------")
                       print("TEACHER NUMBER:",l)
                       print("TEACHER NAME:",m)
                       print("SUBJECT OF THE TEACHER:",n)
                       print("PHONE_NUMBER:",o)
                       print("SALARY:",p)
                       print("-----------------------------")

               SEARCH()
             elif option==5:
               def DISPLAY():
                   import mysql.connector
                   con=mysql.connector.connect(host='localhost',user='root',passwd='12345678',database="institution")
                   mycursor=con.cursor()
                   mycursor.execute("select * from Teacher ")
                   for (TNO,TNAME,SUBJECT,PHONE_NUMBER,SALARY) in mycursor:
                       print("*****************************************")
                       print("TEACHER NUMBER-->>",TNO)
                       print("NAME OF THE TEACHER-->>",TNAME)
                       print("SUBJECT TEACHED BY THE TEACHER-->>",SUBJECT)
                       print("PHONE_NUMBER-->>",PHONE_NUMBER)
                       print("SALARY OF THE TEACHER",SALARY)
                       print("******************************************")
                   print("======ALL THE DETAILS HAS BEEN PRINTED=======")
               DISPLAY()    
             else:
                print(institution())
         else:
            print("you entered a wrong character")
                   
                   
#STAFF MANAGEMENT BY YASH(XII-A)
def WMANG():
    while True:
        print("\n\t\t\t STAFF RECORD MANAGEMENT\n")
        print("*************************************************************************************************")
        print("1.Add Staff Record")
        print("2.Display Staff Record")
        print("3.Search Staff Record")
        print("4.Delete Staff Record")
        print("5.Update Staff Record")
        print("6.Return to main menu")
        print("=**********************************************************************************************=") 
        choice=int(input("enter choice between 1 to 6----------->:"))
        if choice==1:
            def addstaff():
                    import mysql.connector
                    con=mysql.connector.connect(user='root',password='12345678',host='localhost',database='institution')
                    Cursor=con.cursor()
                    sno=input("Enter staff Code:")
                    sname=input("Enter staff  Name:")
                    mob=input("Enter staff  Mobile No.")
                    addr=input("Enter staff  Address:")
                    Qry=("INSERT INTO staff VALUES(%s,%s,%s,%s)")
                    data=(sno,sname,mob,addr)
                    Cursor.execute(Qry,data)
                    con.commit()
                    print("Record Inserted.........yes..")
            addstaff()
        elif choice==2:
            def displaystaff():
                      import mysql.connector
                      con=mysql.connector.connect(user='root',password='12345678',host='localhost',database='institution')
                      Cursor=con.cursor()
                      query=("SELECT * FROM staff")
                      Cursor.execute(query)
                      for (sno,sname,mob,addr)in Cursor:
                                   print("*****************************************************************")
                                   print("STAFF Code:",sno)
                                   print("STAFF Name:",sname)
                                   print("Mobile No. of STAFF:",mob) 
                                   print("Address:",addr)
                                   print("*****************************************************************")
                      print("****records are printed****")
            displaystaff()
        elif choice==3:  
               def SearchStaff():
                   try:
                       import mysql.connector
                       con=mysql.connector.connect(user='root',password='12345678',host='localhost',database='institution')
                       mycursor=con.cursor()
                       snm=input("Enter Staff Name to be Searched from the institution:")
                       query=("SELECT * FROM staff where staffname='%s'")%(snm)
                       mycursor.execute(query)
                       myrecords=mycursor.fetchall()
                       if myrecords==[]:
                           print("not found")
                       
                       for  x in myrecords:
                           a,b,c,d=x
                           print("*****************************************************************************")
                           print("Staff Code:",a)
                           print("Staff Name:",b)
                           print("Mobile No. of Staff:",c) 
                           print("Address:",d) 
                           print("*****************************************************************************")
                   except :
                       print("\n\t\tnothing found\n")
               SearchStaff()
                      
        elif choice==4:
               def deletestaff():
                   import mysql.connector
                   con=mysql.connector.connect(user='root',password='12345678',host='localhost',database='institution')
                   mycursor=con.cursor()
                   snm=input("Enter Staff Name to TERMINATE from the institution:")
                   Query=("DELETE FROM staff WHERE staffname='{}'".format(snm))
                   mycursor.execute(Query)
                   con.commit()
                   print(mycursor.rowcount,"Record(s) Deleted Successfully...........")
               deletestaff()          
        elif choice==5:
            def updatestaff():
                import mysql.connector
                con=mysql.connector.connect(user='root',password='12345678',host='localhost',database='institution')
                mycursor=con.cursor()
                sno=input("Enter Staff code to UPDATE from the institution:")
                print("Enter new data")
                sname=input("Enter member Name:" )
                mob=input("Enter mobile no:")
                addr=input("Enter address:")
                Qry=("UPDATE staff SET staffname='%s',mobileno='%s',staffaddress='%s' WHERE staffcode='%s'" %(sname,mob,addr,sno,))
                mycursor.execute(Qry)
                con.commit()
                print("successfully updated")
            updatestaff()
        elif choice==6:
            institution()




#STUDENT MANAGEMENT BY LAKSHEY(XII-A)
def SMANG():
    while True:
        print("\n\t\t\t STUDENT RECORD MANAGEMENT\n")
        print("========================================================================================")
        print("1.Add Student  Record")
        print("2.Display Student  Record")
        print("3.Search Student  Record")
        print("4.Delete Student  Record")
        print("5.Update Student  Record")
        print("6.Return to main menu")
        print("=======================================================================================") 
        choice=int(input("enter choice between 1 to 6----------->:"))
        if choice==1:
            def addStudent():
                    import mysql.connector
                    con=mysql.connector.connect(user='root',password='12345678',host='localhost',database='institution')
                    Cursor=con.cursor()
                    sno=input("Enter Student  Code:")
                    sname=input("Enter Student   Name:")
                    mob=input("Enter FATHER Mobile No.")
                    addr=input("Enter Student   Address:")
                    Qry=("INSERT INTO Student  VALUES(%s,%s,%s,%s)")
                    data=(sno,sname,mob,addr)
                    Cursor.execute(Qry,data)
                    con.commit()
                    print("Record Inserted.........yes..")
            addStudent()
        elif choice==2:
            def displayStudent():
                      import mysql.connector
                      con=mysql.connector.connect(user='root',password='12345678',host='localhost',database='institution')
                      Cursor=con.cursor()
                      query=("SELECT * FROM Student ")
                      Cursor.execute(query)
                      for (sno,sname,mob,addr)in Cursor:
                                   print("=============================================")
                                   print("Student  Code:",sno)
                                   print("Student  Name:",sname)
                                   print("Mobile No. of Father:",mob) 
                                   print("Address:",addr)
                                   print("=============================================")
                      print("****records are printed****")
            displayStudent()
        elif choice==3:  
               def SearchStudent():
                   try:
                       import mysql.connector
                       con=mysql.connector.connect(user='root',password='12345678',host='localhost',database='institution')
                       mycursor=con.cursor()
                       snm=input("Enter Student  Name to be Searched from the institution:")
                       query=("SELECT * FROM Student  where Student name='%s'")%(snm)
                       mycursor.execute(query)
                       myrecords=mycursor.fetchall()
                       if myrecords==[]:
                           print("not found")
                       
                       for  x in myrecords:
                           a,b,c,d=x
                           print("====================================================================")
                           print("Student  Code:",a)
                           print("Student  Name:",b)
                           print("Mobile No. of Father :",c) 
                           print("Address:",d) 
                           print("====================================================================")
                   except :
                       print("\n\t\tnothing found\n")
               SearchStudent()
                      
        elif choice==4:
               def deleteStudent():
                   import mysql.connector
                   con=mysql.connector.connect(user='root',password='12345678',host='localhost',database='institution')
                   mycursor=con.cursor()
                   snm=input("Enter Student  Name to TERMINATE from the institution:")
                   Query=("DELETE FROM Student  WHERE Student name='{}'".format(snm))
                   mycursor.execute(Query)
                   con.commit()
                   print(mycursor.rowcount,"Record(s) Deleted Successfully...........")
               deleteStudent()          
        elif choice==5:
            def updateStudent():
                import mysql.connector
                con=mysql.connector.connect(user='root',password='12345678',host='localhost',database='institution')
                mycursor=con.cursor()
                sno=input("Enter Student  code to UPDATE from the institution:")
                print("Enter new data")
                sname=input("Enter member Name:" )
                mob=input("Enter mobile no:")
                addr=input("Enter address:")
                Qry=("UPDATE Student  SET Student name='%s',mobileno='%s',Student address='%s' WHERE Sudent code='%s'" %(sname,mob,addr,sno,))
                mycursor.execute(Qry)
                con.commit()
                print("successfully updated")
            updateStudent()
        elif choice==6:
            institution()





#BOOK MANAGEMENT BY UTSAV(XII-A)
def BMANG():
    while True:
        print("\n\t\t\t BOOK RECORD MANAGEMENT\n")
        print("################################################################################################")
        print("1.Add book Record")
        print("2.Display book Record")
        print("3.Search book Record")
        print("4.Delete book Record")
        print("5.Update book Record")
        print("6.Return to main menu")
        print("################################################################################################") 
        choice=int(input("enter choice between 1 to 6----------->:"))
        if choice==1:
            def addbook():
                    import mysql.connector
                    con=mysql.connector.connect(user='root',password='12345678',host='localhost',database='institution')
                    Cursor=con.cursor()
                    bno=input("Enter book Code:")
                    bname=input("Enter book  Name:")
                    topic=input("Enter topic of book")
                    Qry=("INSERT INTO book VALUES(%s,%s,%s)")
                    data=(bno,bname,topic)
                    Cursor.execute(Qry,data)
                    con.commit()
                    print("Record Inserted.........yes..")
            addbook()
        elif choice==2:
            def displaybook():
                      import mysql.connector
                      con=mysql.connector.connect(user='root',password='12345678',host='localhost',database='institution')
                      Cursor=con.cursor()
                      query=("SELECT * FROM book")
                      Cursor.execute(query)
                      for (bno,bname,topic)in Cursor:
                                   print("#################################################################")
                                   print("BOOK Code:",bno)
                                   print("BOOK Name:",bname)
                                   print("TOPIC OF BOOK:",topic)
                                   print("#################################################################")
                      print("****records are printed****")
            displaybook()
        elif choice==3:  
               def Searchbook():
                   try:
                       import mysql.connector
                       con=mysql.connector.connect(user='root',password='12345678',host='localhost',database='institution')
                       mycursor=con.cursor()
                       bnm=input("Enter book Name to be Searched from the institution:")
                       query=("SELECT * FROM book where bookname='%s'")%(bnm)
                       mycursor.execute(query)
                       myrecords=mycursor.fetchall()
                       if myrecords==[]:
                           print("not found")
                       
                       for  x in myrecords:
                           a,b,c=x
                           print("#############################################################################")
                           print("book Code:",a)
                           print("book Name:",b)
                           print("topic of book:",c)  
                           print("#############################################################################")
                   except :
                       print("\n\t\tnothing found\n")
               Searchbook()
                      
        elif choice==4:
               def deletebook():
                   import mysql.connector
                   con=mysql.connector.connect(user='root',password='12345678',host='localhost',database='institution')
                   mycursor=con.cursor()
                   bnm=input("Enter book Name to TERMINATE from the institution:")
                   Query=("DELETE FROM book WHERE bookname='{}'".format(bnm))
                   mycursor.execute(Query)
                   con.commit()
                   print(mycursor.rowcount,"Record(s) Deleted Successfully...........")
               deletebook()          
        elif choice==5:
            def updatebook():
                import mysql.connector
                con=mysql.connector.connect(user='root',password='12345678',host='localhost',database='institution')
                mycursor=con.cursor()
                bno=input("Enter book code to UPDATE from the institution:")
                print("Enter new data")
                bname=input("Enter book Name:" )
                topic=input("Enter topic of book:")
                Qry=("UPDATE book SET bookname='%s',topic_of_book='%s' WHERE bookcode='%s'"%(bname,topic,bno))
                mycursor.execute(Qry)
                con.commit()
                print("successfully updated")
            updatebook()
        elif choice==6:
            institution()
institution()
