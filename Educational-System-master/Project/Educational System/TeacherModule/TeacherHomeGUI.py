from tkinter import *
from PIL import Image, ImageTk
import sqlite3
from tkinter import messagebox
from tkinter import ttk

root = Tk()
root.title('USER ACCOUNT')
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
root.geometry(f'{w}x{h}')
root.resizable(False, False)

# creation of left frame
co = '#1e2627'

f_left = Frame(root, height=h, width=w // 6, bg=co)
f_left.grid(row=0, column=0)

# reading image and convert it to photo image
Icon = Image.open(r"..\Assets\Icons\profile.png")
Icon = Icon.resize((80, 80))
I_tk = ImageTk.PhotoImage(Icon)

# create Button which has the icon of upload photo
btn = Button(f_left, image=I_tk, relief='flat', bg=co)
btn.place(x=f_left['width'] // 3, y=70)
# label for showing
lbl = Label(f_left, text='System Administrator', relief='flat', fg='white', bg=co, font=('tahoma', 14, 'italic'))
lbl.place(x=30, y=170)

# creation of icons
font = ('tahoma', 12)
# -------------------------DASHBOARD----------------------------------
I_dash = Image.open(r"..\Assets\Icons\dashboard.png")
I_dash = I_dash.resize((30, 30))
I_dash_tk = ImageTk.PhotoImage(I_dash)
btn_dashBoard = Button(f_left, image=I_dash_tk, bg=co, relief='flat', text='  DASHBOARD', compound='left',
                       fg='white', font=font)
btn_dashBoard.place(x=10, y=240)
# ---------------------------LECTURES----------------------------------
I_lec = Image.open(r"..\Assets\Icons\lectures.png")
I_lec = I_lec.resize((30, 30))
I_lec_tk = ImageTk.PhotoImage(I_lec)
btn_I_quiz = Button(f_left, image=I_lec_tk, bg=co, relief='flat', text='  LECTURES', compound='left',
                    fg='white', font=font)
btn_I_quiz.place(x=10, y=310)
# -------------------------QUIZZES----------------------------------
I_quiz = Image.open(r"..\Assets\Icons\quiz.png")
I_quiz = I_quiz.resize((30, 30))
I_quiz_tk = ImageTk.PhotoImage(I_quiz)
btn_I_quiz = Button(f_left, image=I_quiz_tk, bg=co, relief='flat', text='  QUIZZES', compound='left',
                    fg='white', font=font)
btn_I_quiz.place(x=10, y=380)
# -------------------------STUDENTS----------------------------------
I_stu = Image.open(r"..\Assets\Icons\students.png")
I_stu = I_stu.resize((30, 30))
I_stu_tk = ImageTk.PhotoImage(I_stu)
btn_I_quiz = Button(f_left, image=I_stu_tk, bg=co, relief='flat', text='  STUDENTS', compound='left',
                    fg='white', font=font)
btn_I_quiz.place(x=10, y=450)
# ---------------------------USER SETTINGS----------------------------------
I_user = Image.open(r"..\Assets\Icons\user.png")
I_user = I_user.resize((30, 30))
I_user_tk = ImageTk.PhotoImage(I_user)
btn_I_quiz = Button(f_left, image=I_user_tk, bg=co, relief='flat', text='  USER SETTINGS', compound='left',
                    fg='white', font=font)
btn_I_quiz.place(x=10, y=520)
# ---------------------------LOGOUT----------------------------------
I_logout = Image.open(r"..\Assets\Icons\log-out.png")
I_logout = I_logout.resize((30, 30))
I_logout_tk = ImageTk.PhotoImage(I_logout)
btn_I_quiz = Button(f_left, image=I_logout_tk, bg=co, relief='flat', text='  LOGOUT', compound='left',
                    fg='white', font=font)
btn_I_quiz.place(x=10, y=590)

# creation of right frame
f_right = Frame(root, width=w - f_left['width'], height=h )
f_right.grid(row=0, column=1)
# Quiz name with entry
QuizName = Label(f_right, text='Quiz Name',font=font)
QuizName.place(x=10,y=20)
QuizNameEnt = Entry(f_right,width=20,font=font)
QuizNameEnt.place(x=100,y=20)
# Number of questions with entry
Qnumlbl=Label(f_right,text='Enter number of questions',font=font)
Qnumlbl.place(x=300,y=20)
Qnum=Spinbox(f_right,values=["1","2","3","4","5"],state='readonly')
Qnum.place(x=500,y=25)
# Creating question text field corresponding to number of questions
Qlbl = Label(f_right, text="Q1) ", font=font)
Qlbl.place(x=10,y=60)
Qtxt=Text(f_right,width=w//22,height=2)
Qtxt.place(x=50,y=60)
# Specifying the Options for Question 1 and the Question Result
rbtn_var=IntVar()
rbtn1=Radiobutton(f_right,text='A) ',font=font,value=1,variable=rbtn_var)
rbtn2=Radiobutton(f_right,text='B) ',font=font,value=2,variable=rbtn_var)
rbtn3=Radiobutton(f_right,text='C) ',font=font,value=3,variable=rbtn_var)
rbtn4=Radiobutton(f_right,text='D) ',font=font,value=4,variable=rbtn_var)
rbtn1.place(x=10,y=110)
rbtn2.place(x=10,y=150)
rbtn3.place(x=10,y=190)
rbtn4.place(x=10,y=230)

op1Ent=Entry(f_right,width=20,font=font)
op2Ent=Entry(f_right,width=20,font=font)
op3Ent=Entry(f_right,width=20,font=font)
op4Ent=Entry(f_right,width=20,font=font)
op1Ent.place(x=60,y=115)
op2Ent.place(x=60,y=155)
op3Ent.place(x=60,y=195)
op4Ent.place(x=60,y=235)
# Insert Function
# QuizNameEnt.get() || Qnum.get() || Qtxt.get(1.0,'end').rstrip().lstrip() || rbtn_var.get()
def AddQ():
    # connection queries into the database
    try:
        conn = sqlite3.connect('..\\Educational_System_Db.db')
        cur = conn.cursor()
        id=5
        if QuizNameEnt.get():
             cur.execute(
                 "INSERT INTO Quizzes (Name, Question_Numbers, Question_Mark, Total_Time, Teacher_Id) Values(?,?,?,?,?)"
                 ,[QuizNameEnt.get(),int(Qnum.get()),1,10,2])
             conn.commit()

        cur.execute("Select Id from Quizzes Where Name=?", [QuizNameEnt.get()])
        results = cur.fetchall()
        id=results[0][0]
        if Qtxt.get(1.0,'end').rstrip().lstrip() and QuizNameEnt.get() and op1Ent.get() and op2Ent.get()  and op3Ent.get()  and op4Ent.get() and rbtn_var.get():
            cur.execute("INSERT INTO Questions(Header,Choose_1,Choose_2,Choose_3,Choose_4,Correct_Answer,Quiz_Id) Values(?,?,?,?,?,?,?)"
                        ,[Qtxt.get(1.0,'end').rstrip().lstrip(),op1Ent.get(),op2Ent.get(),op3Ent.get(),op4Ent.get(),rbtn_var.get(),id])
            conn.commit()
        conn.close()
        displayButton()
        messagebox.showinfo(title='Success',message="Question Added Succesfully")
    except:
        messagebox.showerror(title="DB Error", message="Make sure the queries you wrote is correct")


# ------------------Button-----------------
InsertBtn = Button(f_right,text='Add Question',font=font,width=25,command=AddQ)
InsertBtn.place(x=10,y=270)
#-------------------Quizz Table--------------------
Quizzes=ttk.Treeview(f_right,columns=('Id','Name','Question_Numbers','Question_Mark','Total_Time','Edit','Delete'),show='headings')
Quizzes.heading('Id',text='ID')
Quizzes.heading('Name',text='Quiz Name')
Quizzes.heading('Question_Numbers',text='Number of Questions')
Quizzes.heading('Question_Mark',text='Question Mark')
Quizzes.heading('Total_Time',text='Duration')
Quizzes.heading('Edit',text='Edit')
Quizzes.heading('Delete',text='Delete')

Quizzes.column('Id',width=200)
Quizzes.column('Name',width=200)
Quizzes.column('Question_Numbers',width=200)
Quizzes.column('Question_Mark',width=200)
Quizzes.column('Total_Time',width=200)
Quizzes.place(x=10,y=330,width=1200,height=500)

# ------------------- Display in table -----------------------
def showAll():
    con=sqlite3.connect('..\\Educational_System_Db.db')
    cursor=con.cursor()
    data=cursor.execute('select * from Quizzes')
    con.commit()
    return data

def displayButton():
    result = showAll()
    # remove tree view from other display
    Quizzes.delete(*Quizzes.get_children())
    for row in result:
        Quizzes.insert('', END, values=row)


root.mainloop()
