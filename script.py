import os
import oracledb
import traceback


oracledb.init_oracle_client(lib_dir=str(os.environ.get("HOMEPATH"))+"/Desktop/instantclient_21_7")
oracledb.clientversion()
connection = oracledb.connect(
    user="mxp4295",
    password="Fdssbd3s4drTy",
    dsn="acaddbprod.uta.edu:1523/pcse1p.data.uta.edu")

cursor = connection.cursor()
from tabulate import tabulate

task=-1
try:
    while(task != 0):
            print("\n\n-------------------------------------- ACTIONABLE ITEMS --------------------------------")
            print("1.  List of All Databse Tables")
            print("2.  Get information of a selected table ")
            print("3.  Change the Last Name of Cutomer ")
            print("4.  View Customer detais with Customer ID")             
            print("5.  Add new Location   ")
            print("6.  Which pickup location has the highest number of bookings?")
            print("7.  Which drop location has the highest number of bookings?")
            print("8.  Which Category of car has the highest demand in terms of bookings? ")
            print("9.  Retrieve  customer ID, Pass ID and total amount spent by given range of customer for  highest revenue generating customers")
            print("10. Retrieve vehicle _id, pickup and drop locations and sum total of revenue  for range of given V_ID for them.")
            print("11. View Customer list with total number of particular zipcode ")
            print("0. Enter 0 to exit")

            task=int(input("\nEnter your option: "))

            if task==1:
                rows=cursor.execute("select table_name from user_tables")
                print(tabulate(rows))
            
            if task==2:
                tablename=input("enter the relation name to see contents:   ")
                rows=cursor.execute(f"select * from {tablename}")
                connection.commit()
                print(tabulate(rows))

            
            if task==3: 
                print("----------ENTER FOLLOWING DETAILS OF CUSTOMER TO CHANGE THE LAST NAME---------")
                CUSTOMER_ID = input("Enter customer id: ")
                LAST_NAME = input("Enter new Last name: ")
                cursor.execute(f"update Fall22_S003_10_Customer SET Lname = \'{LAST_NAME}\' where C_ID =\'{CUSTOMER_ID}\'")       
                rows =cursor.execute(f"select Lname, Fname from Fall22_S003_10_Customer where C_ID={CUSTOMER_ID}")   
                connection.commit()
                print("Last Name Changed.")  

            if task==4:
                CUSTOMER_ID =input("Enter Customer ID to get all the details:  ")
                rows =cursor.execute(f"select * from Fall22_S003_10_Customer where C_ID={CUSTOMER_ID}")
                print("\nCustomer Details:")
                print(tabulate(rows,headers=["Customer Id","First Name","Last Name", "Account Start Date", "DOB"]))
                

            if task==5:
                print("----------ENTER FOLLOWING DETAILS TO ADD NEW LOCATION---------")
                ZIPCODE = input("Enter Zipcode: ")
                LOCATIPN_TYPE = input("Enter Location Type: ")
                cursor.execute(f"insert into Fall22_S003_10_Location (Zipcode, L_Type) values (\'{ZIPCODE}\', \'{LOCATIPN_TYPE}\')")
                connection.commit()
                print("NEW LOCATION Added")                

            if task==6:
                rows=cursor.execute('''SELECT Zipcode, L_Type
                                    FROM Fall22_S003_10_Location
                                    WHERE Zipcode IN
                                        (SELECT Pickup_L
                                        FROM Fall22_S003_10_Books_Details
                                        GROUP BY Pickup_L
                                        HAVING COUNT(Pickup_L)>=ALL
                                                            (SELECT COUNT(Pickup_L)
                                                            FROM Fall22_S003_10_Books_Details
                                                            GROUP BY Pickup_L))''')
                connection.commit()
                print(tabulate(rows,headers=["Zip Code","Location Type"]))

            
            if task==7:
                rows=cursor.execute('''SELECT Zipcode, L_Type
                            FROM Fall22_S003_10_Location
                            WHERE Zipcode IN
                                        (SELECT Drop_L
                                        FROM Fall22_S003_10_Books_Details
                                        GROUP BY Drop_L
                                        HAVING COUNT(Drop_L)>=ALL
                                            (SELECT COUNT(Drop_L)
                                            FROM Fall22_S003_10_Books_Details
                                            GROUP BY Drop_L))''')
                print(tabulate(rows,headers=["Zipcode","Location Type"]))


            if task==8:
                rows = cursor.execute('''SELECT CATEGORY 
                        FROM  Fall22_S003_10_Vehicle
                        WHERE V_ID IN
                                    ( SELECT V_Id
                                    FROM Fall22_S003_10_Books_Details
                                    GROUP BY V_ID
                                    HAVING  COUNT(V_Id) >= ALL
                                                    (SELECT COUNT(V_Id)
                                                    FROM Fall22_S003_10_Books_Details
                                                    GROUP BY V_Id))''')
                print(tabulate(rows,headers=["Popular Car Category"]))



            if task==9:
                print("Enter the Range of customer id")
                C_ID1 = input("Start ID: ")
                C_ID2 = input("End ID: ")
                rows=cursor.execute(f'''SELECT C.C_ID, P.Pass_ID, SUM(B.Price) 
                                    FROM Fall22_S003_10_Customer C, Fall22_S003_10_Pass P, Fall22_S003_10_Books_Details B 
                                    WHERE C.C_ID=P.C_ID and C.C_ID=B.C_ID 
                                    AND C.C_ID BETWEEN \'{C_ID1}\'  AND \'{C_ID2}\' 
                                    GROUP BY ROLLUP (C.C_ID, Pass_ID)''')
                print(tabulate(rows,headers=["Customer ID","Pass ID","Total Price"]))

            if task==10:
                print("Enter the Range of vehicle id")
                V_ID1 = input("Enter First VEhicle Id: ")
                V_ID2 = input("Enter second Vehicle Id: ")
                rows=cursor.execute(f'''SELECT V.V_ID, Pickup_L,Drop_L, SUM(Price)
                                    FROM Fall22_S003_10_Vehicle V, Fall22_S003_10_Books_Details B
                                    WHERE V.V_ID=B.V_ID AND V.V_ID BETWEEN \'{V_ID1}\'  AND \'{V_ID2}\'
                                    GROUP BY CUBE(V.V_ID, Pickup_L, Drop_L)''')
                print(tabulate(rows,headers=["Vehicle ID","Pickup Location","Drop Loction", "Price"]))


            if task ==11:     
                PZIPCODE=input("enter the pick up location: ")                
                rows=cursor.execute(f'''SELECT b.C_ID, count(b.C_ID) as Number_of_Rides
                                FROM Fall22_S003_10_Books_Details b, Fall22_S003_10_Customer c
                                WHERE b.C_ID=c.C_ID and Pickup_L= \'{PZIPCODE}\'
                                GROUP BY b.C_ID
                                ORDER BY count(b.C_ID)
                                FETCH first 5 rows only''')
                print(tabulate(rows,headers=["Customer Id","Number of Rides"]))          
            
            if task>11 or task<0:
                print("!!! Oops.... !!!")
                print("!!! You enterd wrong option !!!")
                print("!!! Check Menu for the available options")

except:
    traceback.print_exc()


connection.commit()

connection.close()
