#Import Libraries
import sqlite3

#Connect to the database
conn = sqlite3.connect('DATABASE.db') 
c = conn.cursor() 


def create_table(): 
	c.execute('CREATE TABLE IF NOT EXISTS Employee (ID INT(6) primary key, Name varchar(20) not null)')

def Insert_Data():
    #number=1
    id1 = input("Enter the ID : ")
    name = input("Enter the Name : ")
    c.execute("INSERT INTO Employee (ID,  Name) VALUES(?, ?)", (id1, name)) 
    conn.commit()

def Display_All_Data():
        c.execute("SELECT * FROM Employee")
        data = c.fetchall()
        for i in data:
                print(i)

def Display_By_ID(id1):
        c.execute("SELECT * FROM Employee WHERE ID=={}".format(id1))
        data = c.fetchall()
        for i in data:
                print(i)
                

if __name__ == "__main__":
        print("Choose from following : -")
        print("1. Add Record \n 2. Show All Record \n 3. Fetch By ID")
        option = input("Enter Choice : ")
        if(option == '1'):
                Insert_Data()
        elif(option == '2'):
             Display_All_Data()
        elif(option == '3'):
                id2 = input("Enter ID : ")
                Display_By_ID(id2)
        else:
                print("Invalid Input !")
