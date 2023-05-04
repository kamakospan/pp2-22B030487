import csv
import psycopg2


connection=psycopg2.connect(host="localhost", dbname="postgres", user="postgres", 
                         password="12345", port=5432)
cursor=connection.cursor()
# locale default
cursor.execute("""CREATE TABLE IF NOT EXISTS PhoneBook (
    surname VARCHAR(255),
    name VARCHAR(255),
    number INT
);
""")

def update(sn, mode, newv):
    cursor.execute("""UPDATE PhoneBook
    SET {} = '{}'
    WHERE surname = '{}'
    """.format(mode,newv,sn))

def delete(sn):
    cursor.execute("""DELETE FROM Phonebook
    WHERE surname='{}'
    """.format(sn))

#INSERTING DATA

mode="enter";
while True:
    print("Type 'enter' if you want to add more data and type 'stop' to break")
    mode=input()
    if mode=="stop":
        break
    mytuple=[]
    print("enter surname:")
    mytuple.append(input())
    print("enter name:")
    mytuple.append(input())
    print("enter number:")
    mytuple.append(input())
    mytuple=tuple(mytuple)
    cursor.execute("""INSERT INTO PhoneBook (surname, name ,number) VALUES
    {};
    """.format(mytuple))

while True:
    print("Want to insert data from csv file? yes/no:")
    mode=input()
    if mode=="no":
        break
    print("Enter the name of the file")
    mode=input()
    with open(mode+'.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            cursor.execute("INSERT INTO PhoneBook VALUES (%s,%s,%s)",row)

#UPDATING DATA---------
while True:
    print("Type 'Update' to update some data or 'Stop' to break. Any other spelling won't work so type in exactly what i asked")
    mode=input()
    if mode=="Stop":
        break
    cursor.execute("""SELECT * FROM PhoneBook""")
    print(cursor.fetchall())
    print("Enter surname")
    idtochange=input()
    print("What you want to change? name/number")
    mode=input()
    print("Enter new name/number")
    newvalue=input()
    update(idtochange, mode, newvalue)

#DELETING DATA-----------
while True:
    print("Do you want to delete data? Yes/No")
    mode=input()
    if mode=="No":
        break
    cursor.execute("""SELECT * FROM PhoneBook""")
    print(cursor.fetchall())
    print("Enter surname")
    idtodelete=input()
    delete(idtodelete)


connection.commit()
cursor.close()
connection.close()