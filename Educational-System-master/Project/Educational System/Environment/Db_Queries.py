import sqlite3


# ------------------------------ Teacher Functions -------------------------------


def insert_teacher(name, age, email, password, phone_number, subject, date_created, imgurl=""):
    new_connection = sqlite3.connect("Educational_System_Db.db")
    cursor = new_connection.cursor()
    cursor.execute(
        f"insert into Teachers(Name,Age,Email,Password,Phone_Number,Subject,Date_Created,ImgUrl)values('{name}',{age},'{email}','{password}','{phone_number}','{subject}','{date_created}','{imgurl}')")
    new_connection.commit()
    new_connection.close()


def get_teacher(teacher_id):
    new_connection = sqlite3.connect("Educational_System_Db.db")
    cursor = new_connection.cursor()
    cursor.execute(
        f"select * from Teachers Where Teachers.Id = {teacher_id}")
    return cursor.fetchone()


# ------------------------------ Student Functions -------------------------------


def insert_student(name, age, email, password, phone_number, date_created, imgurl=""):
    new_connection = sqlite3.connect("Educational_System_Db.db")
    cursor = new_connection.cursor()
    cursor.execute(
        f"insert into Students(Name,Age,Email,Password,Phone_Number,Date_Created,ImgUrl)values('{name}',{age},'{email}','{password}','{phone_number}','{date_created}','{imgurl}')")
    new_connection.commit()
    new_connection.close()


# ---------------------------- Subscriptions Functions -----------------------------


def insert_subscription(teacher_id, student_id):
    new_connection = sqlite3.connect("Educational_System_Db.db")
    cursor = new_connection.cursor()
    cursor.execute(
        f"insert into Subscriptions(Teacher_Id,Student_ID)values({teacher_id}, {student_id})")
    new_connection.commit()
    new_connection.close()


def delete_Subscription(teacher_id, student_id):
    new_connection = sqlite3.connect("Educational_System_Db.db")
    cursor = new_connection.cursor()
    cursor.execute(
        f"delete from Subscriptions where Teacher_Id={teacher_id} and Student_Id={student_id}")
    new_connection.commit()
    new_connection.close()


# delete_Subscription(1, 1)


# ---------------------------- Lecture Functions -----------------------------

def insert_Lecture(Name, PDfUrl, VideoUrl, Upload_Date, thumbnail_URL, Teacher_Id, HasQuiz):
    new_connection = sqlite3.connect("Educational_System_Db.db")
    cursor = new_connection.cursor()
    cursor.execute(
        f"insert into Lectures(Name,PDfUrl,VideoUrl,Upload_Date,thumbnail_URL,Teacher_Id,HasQuiz)values('{Name}','{PDfUrl}','{VideoUrl}','{Upload_Date}','{thumbnail_URL}',{Teacher_Id},{HasQuiz})")
    new_connection.commit()
    new_connection.close()


# insert_Lecture("logic", "gg", "vv", "2020-10-5", "oo", "1", 1)

# ---------------------------- Quiz Functions -----------------------------


def insert_Quiz(Name, Question_Numbers, Question_mark, Total_Time, Teacher_Id):
    new_connection = sqlite3.connect("Educational_System_Db.db")
    cursor = new_connection.cursor()
    cursor.execute(
        f"insert into Quizzes(Name,Question_Numbers,Question_mark,Total_Time,Teacher_Id)values('{Name}',{Question_Numbers},{Question_mark},{Total_Time},{Teacher_Id})")
    new_connection.commit()
    new_connection.close()


def delete_Quiz(id):
    new_connection = sqlite3.connect("Educational_System_Db.db")
    cursor = new_connection.cursor()
    cursor.execute(f"delete from Quizzes where Id={id}")
    new_connection.commit()
    new_connection.close()


# insert_Quiz("logic", 10, 1, 10, 1)
# delete_Quiz(1)

# ---------------------------------- Student_Lectures Functions---------------------------------

def insert_Student_Lecture(Lecture_Id, Student_Id):
    new_connection = sqlite3.connect("Educational_System_Db.db")
    cursor = new_connection.cursor()
    cursor.execute(
        f"insert into Student_Lectures(Lecture_Id,Student_Id)values({Lecture_Id},{Student_Id})")
    new_connection.commit()
    new_connection.close()


# insert_Student_Lecture(1, 1)


# ---------------------------------- Student_Quiz Functions---------------------------------

def insert_Student_Quiz(Score, Elapsed_Time, Submitted_Date, Student_Id, Quiz_Id):
    new_connection = sqlite3.connect("Educational_System_Db.db")
    cursor = new_connection.cursor()
    cursor.execute(
        f"insert into Student_Quizzes(Score,Elapsed_Time,Submitted_Date, Student_Id,Quiz_Id)values({Score},'{Elapsed_Time}','{Submitted_Date}', {Student_Id},{Quiz_Id})")
    new_connection.commit()
    new_connection.close()


# insert_Student_Quiz(50, "15", "2020-5-6", 1, 1)


# ---------------------------------- Question Functions---------------------------------
def insert_Question(Header, Choose_1, Choose_2, Choose_3, Choose_4, Correct_Answer, Quiz_Id):
    new_connection = sqlite3.connect("Educational_System_Db.db")
    cursor = new_connection.cursor()
    cursor.execute(
        f"insert into Questions(Header,Choose_1,Choose_2, Choose_3,Choose_4,Correct_Answer,Quiz_Id)values('{Header}','{Choose_1}','{Choose_2}', '{Choose_3}','{Choose_4}','{Correct_Answer}',{Quiz_Id})")
    new_connection.commit()
    new_connection.close()


def delete_Question(id):
    new_connection = sqlite3.connect("Educational_System_Db.db")
    cursor = new_connection.cursor()
    cursor.execute(f"delete from Questions where Id={id}")
    new_connection.commit()
    new_connection.close()

# insert_Question("choose", "h", "k", "l", "s", "s", 1)
# delete_Question(1)

# ---------------------------------- Lecture Quiz Functions---------------------------------
def insert_Lecture_Quiz(Lecture_Id,Quiz_Id):
    new_connection = sqlite3.connect("Educational_System_Db.db")
    cursor = new_connection.cursor()
    cursor.execute(
        f"insert into Lecture_Quiz(Lecture_Id,Quiz_Id)values({Lecture_Id},{Quiz_Id})")
    new_connection.commit()
    new_connection.close()

# insert_Lecture_Quiz(1,1)
