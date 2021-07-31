import sqlite3
# TO ESTABLISH A CONNECTION     
conn = sqlite3.connect("Contact_Book.db")     
cursor = conn.cursor()
cursor.execute( "DROP TABLE IF EXISTS Contact_Details ")
print("======CONNECTION CREATED=========")
# CREATING CONTACT_DETAILS TABLE                                                                           
s= """CREATE TABLE Contact_Details ( C_ID INT NOT NULL,
                                     Name Varchar(20),
                                     Address Varchar(20),
                                     Email Varchar(30),
                                     Phone_Number REAL) """
cursor.execute(s)
print()
print()
print("CONTACT_DETAILS TABLE CREATED SUCCESSFULLY")
# INSERTING VALUES INTO CONTACT_DETAILS TABLE
cursor.execute(""" INSERT INTO Contact_Details ( C_ID, Name,Address, Email, Phone_Number) VALUES
                                                                                 (1,"Krishna","Milwaukee", "doddakrishnasindhureddy@gmail.com",8074084850),
                                                                                 (2,"Sindhu","Florida","kdodda@uwm.edu",3345871567),
                                                                                 (3,"raghu","Delhi","naraha2@uwm.edu",6547987652),
                                                                                 (4,"vipula","United Kingdom","vipulareddy123@gmail.com",8074786253),
                                                                                 (5,"rakesh","Carolina","rakeshb@uwm.edu",8734561234),
                                                                                 (6,"mohith","Bangalore","mohithramesh@uwm.edu",4142897654),
                                                                                 (7,"sumanth","Vizag","sumanthsharma@gmail.com",9963637201),
                                                                                 (8,"Dhanam","Mumbai","dhanalakshmi6543@gmail.com",7789654278),
                                                                                 (9,"Pranaya","Hyderabad","pkotha@uwm.edu",5432789654),
                                                                                 (10,"Ram","Pakisthan","ramereddy@gmail.com",9876376549) """)
conn.commit()
# TO RETRIEVE ALL VALUES FROM CONTACT_DETAILS TABLE
cursor.execute(""" SELECT * FROM Contact_Details """)
print(cursor.fetchall())
print()
print()
print()
# TO SELECT TOP 5 NAMES, PHONE_NUMS FROM TABLE IN SORTED ORDER
cursor.execute(""" SELECT Name,Phone_Number FROM Contact_Details ORDER BY NAME """)
conn.commit()
print(cursor.fetchmany(5))
print()
print()
# UPDATE C_ID by incrementing
cursor.execute(""" UPDATE Contact_Details SET C_ID = C_ID+1 """)
conn.commit()
# insert VALUES INTO C_ID=1 AND SELECT TOP ROW AFTER SORTING IN TERMS OF C_ID
cursor.execute(""" INSERT INTO Contact_Details(C_ID,Name,Address,Email,Phone_Number) VALUES
                                                                                  (1,"Jack","California","rosejack@gmail.com",5623176530) """)
conn.commit()
cursor.execute(""" SELECT C_ID,Name,Address FROM Contact_Details ORDER BY C_ID LIMIT 5 """)
conn.commit()
print(cursor.fetchmany(6))
print(cursor.fetchone())
print()
print()
print()
# DELETING A RECORD WITH Email = "kdodda@uwm.edu"
cursor.execute(""" DELETE FROM Contact_Details WHERE Email = "kdodda@uwm.edu" and Address="California" """)
conn.commit()
cursor.execute(""" SELECT Email,Name FROM Contact_Details """)
print()
print()
# IF WANTS TO DELETE WHOLE TABLE PERMANENTLY
cursor.execute("""DROP TABLE Contact_Details""")
conn.commit()
print(" Contact_Details table dropped successfully")
# CHECK WHETHER DROPPED OR NOT
cursor.execute(""" SELECT * FROM Contact_Details """)
print(cursor.fetchall())
conn.close()


    
