# This is a simple Appointment Tracker system using SQLite.
# This program allows the user to input client information regarding their appointment and can be edited for each user's preference.

''' This Verison of the Appointment Tracker is meant to be used for a local tattoo shop in Marietta who needs an easier way to track their information regarding clients'''
   
# Importing all information required from SQLite.
import sqlite3
from sqlite3 import Error 
import datetime

# Database connection being established to 'myinventory.db' where all appointment information is stored.
database_file_path = "myinventory.db"
def create_connection(db_file):
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except Error as e:
        print(e)
        return None


def insert_data():
    name = input("Enter client's full legal name: ")
    ndc = input("Enter contact information: ")
    location = input ("Enter appointment date MM/DD/YY: ")
    availability = input("Enter appointment time: ")
    arrivaldate = input("Enter designed tattoo artist: ")
    expirationdate = input("Enter tattoo design and location: ")
    changemade = str(now.year) +"/"+str(now.month) +"/"+str(now.day)
    try:      
        sqlresult = conn.execute("INSERT INTO vaccines (name,ndc,location,availability,arrivaldate,expirationdate,changemade)\
            values("+"'"+ str(name) +"'" + ",'"+ str(ndc) +"', '"+ str(location) +"','"+ str (availability)+"','"+str(arrivaldate)+"','"+ str (expirationdate)+"','"+str(changemade)+"')")
        result = conn.commit() #this actually runs the SQL and inserts the data into the database
        if result == None:
            print("*** Data saved to database. ***")
    except Error as e:
        print ("*** Insert error: ",e)
        pass


#                                 
def view_data():
    try:
        cursor = conn.execute ("SELECT id,name, ndc,location,availability,arrivaldate, expirationdate,changemade FROM vaccines" )
        alldata = []
        alldata.append(["Client","Contact Info","Appointment Date","Time","Artist","Design/Location"])
        for row in cursor:
            thisrow=[]
            for x in range(8):
                thisrow.append(row[x])
            alldata.append(thisrow)
        return alldata
    except Error as e:
        print (e)
        pass



def update_data():
    for row in view_data():
            thisrow = "  --> "
            for item in row:
                thisrow += str(item) + "  "
            print (thisrow)
    update_ID = input("Enter the ID of the data record to edit: ")
    print('''
        1 = edit Client name
        2 = edit contact information
        3 = edit appointment date MM/DD/YY
        4 = edit appointment time
        5 = edit tattoo artist
        6 = edit tattoo design and location''')

    feature = input("Enter the numerical value of the data you want to edit: ")
    update_value = input ("Editing "+feature+ ": Please enter the updated information: ")

    if(feature == "1"):
        sql = "UPDATE vaccines set name = ? where id =  ?"
    elif (feature == "2"):
       sql = "UPDATE vaccines set ndc = ? where id =  ?" 
    elif (feature == "3"):
       sql = "UPDATE vaccines set location  = ? where id =  ?"
    elif (feature == "4"):
       sql = "UPDATE vaccines set availability  = ? where id =  ?"
    elif (feature == "5"):
       sql = "UPDATE vaccines set arrivaldate  = ? where id =  ?"
    elif (feature == "6"):
       sql = "UPDATE vaccines set expirationdate = ? where id =  ?"  
        
    try:
        #if we call the connection execute method it invisibly creates a cursor for us
        conn.execute(sql, (update_value,update_ID))
        #update the change made date log
        sql = "UPDATE vaccines set changemade = ? where id =  ?"
        changemade = str(now.year) +"/"+str(now.month) +"/"+str(now.day)
        conn.execute(sql, (changemade,update_ID))
        conn.commit() 
        
    except Error as e:
        print(e)
        pass

def delete_data():
    id_  =  input("Enter the ID for the data record to delete:")
    cursor = conn.cursor() #This sets a spot in the database connection (cursor) for targeted retrieval
    cursor.execute("select name from vaccines where ID = "+id_) #create an object referencing the data
    delete_item = cursor.fetchall() # get the data
    confirm = input("Are you sure you want to delete " + id_ + " " + str(delete_item[0]) + "? (Enter 'y' to confirm.)")
    if confirm.lower() == "y":
        try:
            delete_sql = "DELETE FROM vaccines WHERE id = ?"
            conn.execute(delete_sql,id_)
            result = conn.commit() #capture the result of the commit and use it to check the result
            if result == None:
                print (id_ + " " + str(delete_item[0]) + " deleted.")
            else:
                print ("Deletion failed during SQL execution.")
        except Error as e:
            print (e)
            pass
    else:
        print("Deletion aborted.")

conn = create_connection(database_file_path)
now = datetime.datetime.now()

if conn:
    print ("Connected to database: ",conn)  
else:
    print("Error connecting to database.")

while True:
    print("Welcome to the Vaccine Management System!")
    print("1 to view the data")
    print("2 to insert a new data record")
    print("3 to update a data record")
    print("4 to delete a data record")
    print("X to exit")
    name = input ("Choose an operation to perform: ")
    if (name =="1"):
        for row in view_data():
            thisrow = "  --> "
            for item in row:
                thisrow += str(item) + "  "
            print (thisrow)
    elif(name == "2"):
        insert_data()
    elif(name == "3"):
        update_data()
    elif(name == "4"):
        delete_data()
    elif(name == "X"):
        conn.close()
        break