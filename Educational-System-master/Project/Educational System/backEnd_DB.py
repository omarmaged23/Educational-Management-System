import sqlite3

def studentData():
    con=sqlite3.connect('student.db')
    cursor=con.cursor()
    cursor.execute("""  create table IF NOT EXISTS student(
            stdID INT PRIMARY KEY NOT NULL,
            fname TEXT,
            lname TEXT,
            age   INT,
            gender  TEXT,
            address TEXT,
            mobile  TEXT 
            ) """)
    con.commit()
    con.close()
    
    
def addStudent(stdID,fname,lname,age,gender,address,mobile):
    con=sqlite3.connect('student.db')
    cursor=con.cursor()
    cursor.execute('insert into student values (?,?,?,?,?,?,?)',(stdID,fname,lname,age,gender,address,mobile))
    con.commit()
    con.close()
  
    
def showAllStudent():
    con=sqlite3.connect('student.db')
    cursor=con.cursor()
    data=cursor.execute('select * from student')
    con.commit()
    return data

def deleteStudent(stdID):
    con=sqlite3.connect('student.db')
    cursor=con.cursor()
    cursor.execute(f'delete from student where stdID={stdID}')
    con.commit()
    con.close()
    
def updateStudent(stdID,fname,lname,age,gender,address,mobile):
    con=sqlite3.connect('student.db')
    cursor=con.cursor()
    cursor.execute('update student set fname=? ,lname=?,age=?,gender=?,address=?,mobile=? where stdID=? ',(fname,lname,age,gender,address,mobile,stdID))
    con.commit()
    con.close()
    
    
    
def logintable():
    con=sqlite3.connect('login.db')
    cursor=con.cursor()
    cursor.execute("""  create table IF NOT EXISTS login(
            username TEXT PRIMARY KEY NOT NULL,
            password TEXT NOT NULL
            ) """)
    con.commit()
    con.close()

def addUser(username,password):
    con=sqlite3.connect('login.db')
    cursor=con.cursor()
    cursor.execute('insert into login values(?,?)',(username,password))
    con.commit()
    con.close()
    
def showAllUsers():
    con=sqlite3.connect('login.db')
    cursor=con.cursor()
    data=cursor.execute('select * from login')
    con.commit()
    return data
    