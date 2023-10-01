import sqlite3

def create_Teachers_Table():
    try:
        new_connection = sqlite3.connect("Educational_System_Db.db")
        cursor = new_connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS Teachers(
                Id INTEGER PRIMARY KEY AUTOINCREMENT,
                Name TEXT NOT NULL,
                Age INTEGER,
                Email TEXT NOT NULL,
                ImgUrl TEXT,
                Password TEXT NOT NULL,
                Phone_Number TEXT NOT NULL,
                Subject TEXT NOT NULL,
                Date_Created date)""")
        new_connection.commit()
        new_connection.close()
    except:
        print("An Error Occurred During Creating Teachers Table ")
#########################################################################


def create_Students_Table():
    try:
        new_connection = sqlite3.connect("Educational_System_Db.db")
        cursor = new_connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS Students(
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL,
            Age INTEGER,
            Email TEXT NOT NULL,
            ImgUrl TEXT,
            Password TEXT NOT NULL,
            Phone_Number TEXT NOT NULL,
            Date_Created date
            )""")
        new_connection.commit()
        new_connection.close()
    except:
        print("An Error Occurred During Creating Students Table ")

########################################################################


def create_Subscriptions_Table():
    try:
        new_connection = sqlite3.connect("Educational_System_Db.db")
        cursor = new_connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS Subscriptions(
        Teacher_Id INTEGER,
        Student_Id INTEGER,
        FOREIGN KEY(Teacher_Id) REFERENCES Teacher(Id),
        FOREIGN KEY(Student_Id) REFERENCES Student(Id),
        PRIMARY KEY(Teacher_Id, Student_Id)
        )""")
        new_connection.commit()
        new_connection.close()
    except:
        print("An Error Occurred During Creating Subscriptions Table ")

##########################################################################


def create_Lectures_Table():
    try:
        new_connection = sqlite3.connect("Educational_System_Db.db")
        cursor = new_connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS Lectures(
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL,
            PDfUrl TEXT,
            VideoUrl TEXT,
            Upload_Date date,
            thumbnail_URL TEXT,           
            Teacher_Id INTEGER,
            HasQuiz INTEGER,
            FOREIGN KEY(Teacher_Id) REFERENCES Teacher(Id)
            )""")
        new_connection.commit()
        new_connection.close()
    except:
        print("An Error Occurred During Creating Lectures Table ")

####################################################################


def create_Quizzes_Table():
    try:
        new_connection = sqlite3.connect("Educational_System_Db.db")
        cursor = new_connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS Quizzes(
            Id INTEGER PRIMARY KEY,
            Name TEXT NOT NULL,
            Question_Numbers INTEGER,
            Question_Mark INTEGER,
            Total_Time INTEGER,
            Teacher_Id INTEGER,
            FOREIGN KEY(Teacher_Id) REFERENCES Teacher(Id)
            )""")
        new_connection.commit()
        new_connection.close()
    except:
        print("An Error Occurred During Creating Quizzes Table ")

######################################################################


def create_Student_Lectures_Table():
    try:
        new_connection = sqlite3.connect("Educational_System_Db.db")
        cursor = new_connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS Student_Lectures(
            Lecture_Id INTEGER,
            Student_Id INTEGER,
            FOREIGN KEY(Lecture_Id) REFERENCES Lecture(Id),
            FOREIGN KEY(Student_Id) REFERENCES Student(Id),
            PRIMARY KEY(Lecture_Id, Student_Id)
            )""")
        new_connection.commit()
        new_connection.close()
    except:
        print("An Error Occurred During Creating Student_Lectures Table ")

###########################################################################


def create_Student_Quizzes_Table():
    try:
        new_connection = sqlite3.connect("Educational_System_Db.db")
        cursor = new_connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS Student_Quizzes(
            Score INTEGER NOT NULL,
            Elapsed_Time TEXT,
            Submitted_Date date,
            Student_Id INTEGER,
            Quiz_Id INTEGER,
            FOREIGN KEY(Student_Id) REFERENCES Student(Id),
            FOREIGN KEY(Quiz_Id) REFERENCES Quiz(Id),
            PRIMARY KEY(Student_Id, Quiz_Id)
            )""")
        new_connection.commit()
        new_connection.close()
    except:
        print("An Error Occurred During Creating Student_Quizzes Table ")

############################################################################


def create_Questions_Table():
    try:
        new_connection = sqlite3.connect("Educational_System_Db.db")
        cursor = new_connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS Questions(
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Header TEXT,
            Choose_1 TEXT NOT NULL,
            Choose_2 TEXT NOT NULL,
            Choose_3 TEXT,
            Choose_4 TEXT,
            Correct_Answer TEXT,
            Quiz_Id INTEGER,
            FOREIGN KEY(Quiz_Id) REFERENCES Quiz(Id)
            )""")
        new_connection.commit()
        new_connection.close()
    except:
        print("An Error Occurred During Creating Questions Table ")
#######################################################################

def create_Lecture_Quiz_Table():
    try:
        new_connection = sqlite3.connect("Educational_System_Db.db")
        cursor = new_connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS Lecture_Quiz(        
            Lecture_Id INTEGER,
            Quiz_Id INTEGER,
            FOREIGN KEY(Lecture_Id) REFERENCES Lectures(Id),
            FOREIGN KEY(Quiz_Id) REFERENCES Quiz(Id),
            PRIMARY KEY(Lecture_Id, Quiz_Id)
            )""")
        new_connection.commit()
        new_connection.close()
    except:
        print("An Error Occurred During Creating Lectures Quiz Table ")
#######################################################################

def create_All_Tables():
    create_Teachers_Table()
    create_Students_Table()
    create_Subscriptions_Table()
    create_Quizzes_Table()
    create_Lectures_Table()
    create_Student_Lectures_Table()
    create_Student_Quizzes_Table()
    create_Questions_Table()
    create_Lecture_Quiz_Table()

###################################################################