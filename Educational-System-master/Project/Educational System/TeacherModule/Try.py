from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from  tkinter.ttk import Combobox
from tkinter import messagebox
import sqlite3

from pip._internal.metadata import Backend

root = Tk()
root.title('USER ACCOUNT')
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
root.attributes('-fullscreen', True)
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
                    fg='white', font=font,command=lambda :quizHome_frame.tkraise())
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
f_right = Frame(root, width=w - f_left['width'], height=h)
f_right.grid(row=0, column=1)

#-------------------Edit CREATION--------------------------
quiz_frame=Frame(f_right, width=w - f_left['width'], height=h,bg='white')
quiz_frame.grid(row=0,column=1)
question_frame = Frame(f_right, width=w - f_left['width'], height=h, bg='white')
question_frame.grid_propagate(True)
question_frame.grid(row=0, column=1)
quiz_frame_update=Frame(f_right, width=w - f_left['width'], height=h,bg='white')
quiz_frame_update.grid(row=0,column=1)
question_frame_edt = Frame(f_right, width=w - f_left['width'], height=h,bg='white')
question_frame_edt.grid_propagate(True)
question_frame_edt.grid(row=0, column=1)
quizHome_frame = Frame(f_right, width=w - f_left['width'], height=h, bg='white')
quizHome_frame.grid_propagate(True)
quizHome_frame.grid(row=0, column=1)
#----------------------Hoooooooome----------------------------------
#--------------------QUIZES HOME PAGE------------------------
#--------------------Labels-----------------------
#------------------- Display in table -----------------------


Quizzes=ttk.Treeview(quizHome_frame,columns=('Id','Name','Question_Numbers','Question_Mark','Total_Time'),show='headings')
Quizzes.heading('Id',text='ID')
Quizzes.heading('Name',text='Quiz Name')
Quizzes.heading('Question_Numbers',text='Number of Questions')
Quizzes.heading('Question_Mark',text='Question Mark')
Quizzes.heading('Total_Time',text='Duration')


Quizzes.column('Id',width=50)
Quizzes.column('Name',width=50)
Quizzes.column('Question_Numbers',width=50)
Quizzes.column('Question_Mark',width=50)
Quizzes.column('Total_Time',width=50)
Quizzes.place(x=10,y=330,width=1000,height=300)

# ------------------- Display in table -----------------------
def showAll():
    con=sqlite3.connect('..\\Educational_System_Db.db')
    cursor=con.cursor()
    data=cursor.execute('select Id,Name,Question_Numbers,Question_Mark,Total_Time from Quizzes')
    con.commit()
    return data

def displayButton():
    result = showAll()
    lst = []
    # remove tree view from other display
    Quizzes.delete(*Quizzes.get_children())
    for row in result:
        Quizzes.insert('', END,values=row)
    try:
        conn = sqlite3.connect("..\\Educational_System_Db.db")
        curr = conn.cursor()
        curr.execute("Select Id from Quizzes")
        Idd = curr.fetchall()
        conn.close()
        for i in range(0, len(Idd)):
            lst.append(Idd[i][0])
    except:
        messagebox.showerror(title='error', message="Error in combobox")
    return lst
# Edit and Delete Functions

def Edittt():
    try:
        conn = sqlite3.connect('..\\Educational_System_Db.db')
        cur = conn.cursor()
        cur.execute("select * from Quizzes where Id=?", [Id_var.get()])

        result_update = cur.fetchone()
        set_title_update(result_update[1])
        t_update.set(str(result_update[2]))
        set_points_update(result_update[3])
        set_time_update(result_update[4])
        lst = displayButton()
        quiz_frame_update.tkraise()
    except:
        messagebox.showerror(title="Set Error", message="Set Error")

def Delete():
    try:
        conn=sqlite3.connect("..\\Educational_System_Db.db")
        curr=conn.cursor()
        curr.execute("Delete From Quizzes where Id=?",[Id_var.get()])
        conn.commit()
        curr.execute("Delete From Questions where Quiz_Id=?", [Id_var.get()])
        conn.commit()
        conn.close()
        lst = displayButton()
        displayButton()
        messagebox.showinfo(title="Success",message="Quiz Deleted Successfully")
    except:
        messagebox.showerror(title="Error",message="Something went wrong DELETE Failed")
# Edit and Delete Icons
lst=displayButton()
I_Edit = Image.open("..\\Assets\\Icons\\icons8-edit-15.png")
I_Edit = I_Edit.resize((15, 15))
I_Edit_tk = ImageTk.PhotoImage(I_Edit)
btn_Edit = Button(quizHome_frame, image=I_Edit_tk, bg='white', relief='flat',text="Edit By Id", compound='left',
                       fg='black', font=font,borderwidth=0,border=0,command=Edittt)

# -------------------------
I_Delete = Image.open("..\\Assets\\Icons\\icons8-trash-26.png")
I_Delete = I_Delete.resize((15, 15))
I_Delete_tk = ImageTk.PhotoImage(I_Delete)
btn_Delete = Button(quizHome_frame, image=I_Delete_tk, bg='white', relief='flat',text="Delete By Id", compound='left',
                       fg='black', font=font,borderwidth=0,border=0,command=Delete)

#-------Combo Box -------
Id_var=IntVar()
Id_cmbox = Combobox(quizHome_frame, width=80,state='readonly',values=lst,textvariable=Id_var)
Id_lbl = Label(quizHome_frame, text="Select ID", font=font, fg='black', bg='white', anchor='w')
Id_lbl.place(x=10,y=647)
Id_cmbox.place(x=95,y=650)
#--------------------------
# InsertBtn = Button(f_right,text='Refresh',font=font,width=25,command=displayButton)
# InsertBtn.place(x=10,y=270)
addQuiz_btn=Button(quizHome_frame,text="ADD",font=font,bg=co,fg="white",width=15, height=1,relief="flat",command=lambda :quiz_frame.tkraise())
Home_lbl = Label(quizHome_frame, text="QUIZES", bg="white", font=font)
Home_lbl.place(x=50, y=50)
addQuiz_btn.place(x=850, y=650)
btn_Delete.place(x=710, y=645)
btn_Edit.place(x=610, y=645)

# Create Question Frame

# ---------------------ADDITION VARIBALES-------------------------------------
ques_num = 0
max_qes = 5
# inialize List
questions = []
for i in range(0, max_qes):
    questions.append([])
for i in range(0, max_qes):
    for j in range(0, 6):
        questions[i].append(j)
        questions[i][j] = 0


# -------------------- Buttons Functions--------------------------------------
def Add_Btn_Click():
    # Add The Question To The List
    global ques_num
    global num
    questions[ques_num][0] = ques_title.get()
    questions[ques_num][1] = op1_text.get('1.0', END)
    questions[ques_num][2] = op2_text.get('1.0', END)
    questions[ques_num][3] = op3_text.get('1.0', END)
    questions[ques_num][4] = op4_text.get('1.0', END)
    questions[ques_num][5] = ans_var.get()
    # Clear The Text Fields
    ques_title.delete(0, END)
    op1_text.delete('1.0', END)
    op2_text.delete('1.0', END)
    op3_text.delete('1.0', END)
    op4_text.delete('1.0', END)
    try:
        conn = sqlite3.connect("..\\Educational_System_Db.db")
        cur = conn.cursor()
        cur.execute(
            "Select Id from Quizzes Where Name=?,Question_Numbers=?,Question_Mark=?,Total_Time=?,Teacher_Id=?",
            [[get_title().rstrip().lstrip(), get_Qnum(), get_points(),get_time(), 2]])
        output = cur.fetchall()
        print(output)
        output = output[0][0]
        conn.close()
    except:
        messagebox.showerror("title=69",message="250")
    if (ques_num == max_qes - 1):
        try:
            for i in range(0,max_qes):
                conn = sqlite3.connect("..\\Educational_System_Db.db")
                conn.execute(
                    'Insert into Questions(Header,Choose_1,Choose_2,Choose_3,Choose_4,Correct_Answer,Quiz_Id) values(?,?,?,?,?,?,?)'
                    , [questions[i][0],questions[i][1],questions[i][2],questions[i][3],questions[i][4],questions[i][5],output])
                conn.commit()
                conn.close()
            messagebox.showinfo("Success", "Quiz Added Succeffully!")
        except:
            messagebox.showerror("showerror", "260")
    else:
        ques_num += 1
        ques_lbl.config(text="Question " + str(ques_num + 1))


def Back_Btn_Click():
    global ques_num
    if (ques_num == 0):
        messagebox.showerror("showerror", "Error")
    else:
        # Clear The Fields
        ques_title.delete(0, END)
        op1_text.delete('1.0', END)
        op2_text.delete('1.0', END)
        op3_text.delete('1.0', END)
        op4_text.delete('1.0', END)

        ques_num -= 1
        # Set The Fields Again
        ques_title.insert(0, questions[ques_num][0])
        op1_text.insert('1.0', questions[ques_num][1])
        op2_text.insert('1.0', questions[ques_num][2])
        op3_text.insert('1.0', questions[ques_num][3])
        op4_text.insert('1.0', questions[ques_num][4])
        ques_lbl.config(text="Question " + str(ques_num + 1))


# ------------------------LABELS AND TEXTBOX CREATION-------------------------------------------
Home_lbl=Label(question_frame,text="QUIZES",bg="white",font=font)
quiz_lbl = Label(question_frame, text="Quiz Title", font=font, fg='black', bg='white', anchor='w')
quiz_title2 = Text(question_frame, height=1, font=font, fg='black', border=1, relief='solid')
ques_title = Entry(question_frame, font=font, width=80, fg='black', border=1, relief='solid', )
ques_lbl = Label(question_frame, text="Question " + str(1), font=font, fg='black', bg='white', anchor='w')
# ---------------------------Qestion Options----------------------------------
op1_text = Text(question_frame, height=1, font=font, fg='black', border=1, relief='solid')
op2_text = Text(question_frame, height=1, font=font, fg='black', border=1, relief='solid')
op3_text = Text(question_frame, height=1, font=font, fg='black', border=1, relief='solid')
op4_text = Text(question_frame, height=1, font=font, fg='black', border=1, relief='solid')

# ---------------------------OPTIONS ANS RADIO BUTTONS----------------------------------
op1_lbl = Label(question_frame, text="A)", font=font, bg='white')
op2_lbl = Label(question_frame, text="B)", font=font, bg='white')
op3_lbl = Label(question_frame, text="C)", font=font, bg='white')
op4_lbl = Label(question_frame, text="D)", font=font, bg='white')

# ---------------------------Ans List RADIO BUTTONS----------------------------------
ans_var=StringVar()
ans_var.set('A)')
ans_cmbox = Combobox(question_frame, width=80, state='readonly',values=['A)','B)','C)','D)'],textvariable=ans_var)
ans_lbl = Label(question_frame, text="Answer", font=font, fg='black', bg='white', anchor='w')

# ---------------------------Buttons---------------------------------
add_ques_btn = Button(question_frame, text="ADD", width=15, height=1, bg=co, fg='white', font=font, relief="flat",
                      command=Add_Btn_Click)
back_btn = Button(question_frame, text="Back", width=15, height=1, bg=co, fg='white', font=font, relief="flat",
                  command=Back_Btn_Click)



# ---------------------------PLACING----------------------------------
Home_lbl.place(x=50,y=50)
ques_lbl.place(x=50, y=250)
ques_title.place(x=250, y=250)
op1_lbl.place(x=190, y=300)
op1_text.place(x=250, y=300)
op2_text.place(x=250, y=350)
op2_lbl.place(x=190, y=350)
op3_text.place(x=250, y=400)
op3_lbl.place(x=190, y=400)
op4_text.place(x=250, y=450)
op4_lbl.place(x=190, y=450)
ans_lbl.place(x=170, y=500)
ans_cmbox.place(x=250, y=500)
add_ques_btn.place(x=825, y=600)
back_btn.place(x=250, y=600)
#----------------------Update Quiz Page 1---------------------------
font1=('tahoma', 15)
t_update=StringVar()
quiz_title_update=Entry(quiz_frame_update,font=font1,fg='black',border=1,relief='solid',width=80)
Qnum_update=Spinbox(quiz_frame_update,values=["1","2","3","4","5"],state='readonly',bg="white",font=font1,width=80,textvariable=t_update)
ques_points_update=Entry(quiz_frame_update,font=font1,fg='black',border=1,relief='solid',width=80)
total_time_update=Entry(quiz_frame_update,font=font1,fg='black',border=1,relief='solid',width=80)
quiz_lbl_update=Label(quiz_frame_update,text="Quiz Title",bg="white",font=font1)
quesNum_lbl_update=Label(quiz_frame_update,text="Number of Questions ",bg="white",font=font1)
quesPoints_lbl_update=Label(quiz_frame_update,text="Question point",bg="white",font=font1)
Time_lbl_update=Label(quiz_frame_update,text="Total Time",bg="white",font=font1)
edit_page1_lbl=Label(quiz_frame_update,text="Edit Quiz",font=font1,bg="white")

def set_title_update(text):
    quiz_title_update.delete(0, END)
    quiz_title_update.insert(0,text)
    return
def set_points_update(text):
    ques_points_update.delete(0, END)
    ques_points_update.insert(0,text)
    return

def set_time_update(text):
    total_time_update.delete(0, END)
    total_time_update.insert(0,text)
    return



def Next_Btn_Update():

    try:
        conn = sqlite3.connect('..\\Educational_System_Db.db')
        cur = conn.cursor()
        cur.execute("select * from Quizzes where Id=?",[Id_var.get()])
        result_update=cur.fetchone()
        if(quiz_title_update.get() and ques_points_update.get() and total_time_update.get()):
            cur.execute("Update Quizzes Set Name=? , Question_Numbers=? , Question_Mark=? , Total_Time=? where Id=? and Name=? and Question_Numbers=? and Question_Mark=? and Total_Time=? and Teacher_Id=?"
                        ,[quiz_title_update.get().rstrip().lstrip(),int(Qnum_update.get()),int(ques_points_update.get()),int(total_time_update.get()),
                          result_update[0],result_update[1],result_update[2],result_update[3],result_update[4],result_update[5]])
            conn.commit()
            conn.close()
            try:
                conn = sqlite3.connect('..\\Educational_System_Db.db')
                cur = conn.cursor()
                cur.execute("select * from Questions where Quiz_Id=?", [Id_var.get()])
                result = cur.fetchall()
                result = result[0]
                ques_title_edt.insert(0, str(result[1]).rstrip().lstrip())
                op1_text_edt.insert("1.0", result[2])
                op2_text_edt.insert("1.0", result[3])
                op3_text_edt.insert("1.0", result[4])
                op4_text_edt.insert("1.0", result[5])
                ans_var_edt.set(result[6])
                conn.close()
            except:
                messagebox.showerror(title="Set Error", message="set wla ragel")
            question_frame_edt.tkraise()
    except:
        messagebox.showerror(title="DB Error", message="Make sure the queries you wrote is correct")

next_btn_update=Button(quiz_frame_update,text="Next",font=font,border=1,relief='flat',bg="gray",fg="white",width=20,command=Next_Btn_Update)
back_btn_update=Button(quiz_frame_update,text="Back",font=font,border=1,relief='flat',bg="gray",fg="white",width=20,command=lambda :quizHome_frame.tkraise())


#-------------Placing----------------
quiz_lbl_update.place(x=50,y=250)
quiz_title_update.place(x=250,y=250)
quesNum_lbl_update.place(x=50,y=300)
Qnum_update.place(x=250,y=300)
Time_lbl_update.place(x=50,y=350)
total_time_update.place(x=250,y=350)
quesPoints_lbl_update.place(x=50,y=400)
ques_points_update.place(x=250,y=400)
next_btn_update.place(x=700,y=500)
back_btn_update.place(x=500,y=500)
edit_page1_lbl.place(x=50,y=100)
#------------------------------------------------------------------

#----------------------Update Quiz Page 2---------------------------
#---------------------Edit Question -----------------------------------------
#---------------------ADDITION VARIBALES-------------------------------------
ques_num_edt = 0
max_qes_edt = 5
# inialize List
questionsEdt = []
for i in range(0, max_qes_edt):
    questionsEdt.append([])
for i in range(0, max_qes_edt):
    for j in range(0, 6):
        questionsEdt[i].append(j)
        questionsEdt[i][j] = 0


# -------------------- Buttons Functions--------------------------------------


def Add_Btn_Click_edt():
    # Add The Question To The List
    global ques_num_edt
    questionsEdt[ques_num_edt][0] = ques_title_edt.get().rstrip().lstrip()
    questionsEdt[ques_num_edt][1] = op1_text_edt.get('1.0', END).rstrip().lstrip()
    questionsEdt[ques_num_edt][2] = op2_text_edt.get('1.0', END).rstrip().lstrip()
    questionsEdt[ques_num_edt][3] = op3_text_edt.get('1.0', END).rstrip().lstrip()
    questionsEdt[ques_num_edt][4] = op4_text_edt.get('1.0', END).rstrip().lstrip()
    questionsEdt[ques_num_edt][5] = ans_var_edt.get()
    #Delete All Fields
    ques_title_edt.delete(0, END)
    op1_text_edt.delete('1.0', END)
    op2_text_edt.delete('1.0', END)
    op3_text_edt.delete('1.0', END)
    op4_text_edt.delete('1.0', END)
    # Get All Text Fields
    try:
        conn = sqlite3.connect('..\\Educational_System_Db.db')
        cur = conn.cursor()
        cur.execute("select * from Questions where Quiz_Id=?", [6])
        result = cur.fetchall()
        if(ques_num_edt+1 != max_qes_edt):
            ques_title_edt.insert(0, str(result[ques_num_edt+1][1]).rstrip().lstrip())
            op1_text_edt.insert("1.0", result[ques_num_edt+1][2])
            op2_text_edt.insert("1.0", result[ques_num_edt+1][3])
            op3_text_edt.insert("1.0", result[ques_num_edt+1][4])
            op4_text_edt.insert("1.0", result[ques_num_edt+1][5])
            ans_var_edt.set(result[ques_num_edt+1][6])
        conn.close()
    except:
        messagebox.showerror(title="Error",message="Error returning data from database")
    if (ques_num_edt == max_qes_edt - 1):
        for i in range(0,max_qes_edt):
            conn = sqlite3.connect("..\\Educational_System_Db.db")
            conn.execute(
                'Update Questions Set Header=?,Choose_1=?,Choose_2=?,Choose_3=?,Choose_4=?,Correct_Answer=? Where Quiz_id=? and Id=?'
                ,[questionsEdt[i][0],questionsEdt[i][1],questionsEdt[i][2],questionsEdt[i][3],questionsEdt[i][4],questionsEdt[i][5],6,result[i][0]])
            conn.commit()
            conn.close()
        messagebox.showinfo("Success", "Quiz Added Succeffully!")
    else:
        ques_num_edt += 1
        ques_lbl_edt.config(text="Question " + str(ques_num_edt + 1))


def Back_Btn_edt():
    global ques_num_edt
    if(ques_num_edt==0):
        quiz_frame_update.tkraise()

    else:
        #Clear The Fields
        ques_title_edt.delete(0, END)
        op1_text_edt.delete('1.0', END)
        op2_text_edt.delete('1.0', END)
        op3_text_edt.delete('1.0', END)
        op4_text_edt.delete('1.0', END)

        ques_num_edt-=1
        #Set The Fields Again
        ques_title_edt.insert(0,questionsEdt[ques_num_edt][0])
        op1_text_edt.insert('1.0',questionsEdt[ques_num_edt][1])
        op2_text_edt.insert('1.0',questionsEdt[ques_num_edt][2])
        op3_text_edt.insert('1.0',questionsEdt[ques_num_edt][3])
        op4_text_edt.insert('1.0',questionsEdt[ques_num_edt][4])
        ques_lbl_edt.config(text="Question " + str(ques_num_edt + 1))


#------------------------LABELS AND TEXTBOX CREATION-------------------------------------------

# quiz_lbl2=Label(question_frame_edt,text="Quiz Title",font=font,fg='black',bg='white',anchor='w')
# quiz_title2=Text(question_frame_edt,height=1,font=font,fg='black',border=1,relief='solid')
ques_title_edt = Entry(question_frame_edt, font=font, width=80, fg='black', border=1, relief='solid', )
ques_lbl_edt = Label(question_frame_edt, text="Question "+str(1), font=font, fg='black', bg='white', anchor='w')
updt_edt=Label(question_frame_edt,text="Edit",width=20)
updt_edt.place(x=50,y=10)
# ---------------------------Qestion Options----------------------------------
op1_text_edt = Text(question_frame_edt, height=1, font=font, fg='black', border=1, relief='solid')
op2_text_edt = Text(question_frame_edt, height=1, font=font, fg='black', border=1, relief='solid')
op3_text_edt = Text(question_frame_edt, height=1, font=font, fg='black', border=1, relief='solid')
op4_text_edt = Text(question_frame_edt, height=1, font=font, fg='black', border=1, relief='solid')

# ---------------------------OPTIONS ANS RADIO BUTTONS----------------------------------
op1_lbl_edt = Label(question_frame_edt, text="A)", font=font, bg='white')
op2_lbl_edt = Label(question_frame_edt, text="B)", font=font, bg='white')
op3_lbl_edt = Label(question_frame_edt, text="C)", font=font, bg='white')
op4_lbl_edt = Label(question_frame_edt, text="D)", font=font, bg='white')

# ---------------------------Ans List RADIO BUTTONS----------------------------------
ans_var_edt=StringVar()
ans_var_edt.set('A)')
ans_cmbox_edt = Combobox(question_frame_edt, width=80,state='readonly',values=['A)','B)','C)','D)'],textvariable=ans_var_edt)
ans_lbl_edt = Label(question_frame_edt, text="Answer", font=font, fg='black', bg='white', anchor='w')

# ---------------------------Buttons---------------------------------
add_ques_btn_edt=Button(question_frame_edt,text="ADD",width=15,height=1,bg=co,fg='white',font=font,relief="flat",command=Add_Btn_Click_edt)
back_btn_edt=Button(question_frame_edt,text="Back",width=15,height=1,bg=co,fg='white',font=font,relief="flat",command=Back_Btn_edt)


# ---------------------------PLACING----------------------------------

# --------------------------------------------------------------------
ques_lbl_edt.place(x=50, y=250)
ques_title_edt.place(x=250, y=250)
op1_lbl_edt.place(x=190, y=300)
op1_text_edt.place(x=250, y=300)
op2_text_edt.place(x=250, y=350)
op2_lbl_edt.place(x=190, y=350)
op3_text_edt.place(x=250, y=400)
op3_lbl_edt.place(x=190, y=400)
op4_text_edt.place(x=250, y=450)
op4_lbl_edt.place(x=190, y=450)
ans_lbl_edt.place(x=170, y=500)
ans_cmbox_edt.place(x=250, y=500)
add_ques_btn_edt.place(x=825,y=600)
back_btn_edt.place(x=250,y=600)

#------------------------------------------------------------------


#-------------------------Create Quiz page1--------------------

font1=('tahoma', 15)
quiz_title=Entry(quiz_frame,font=font1,fg='black',border=1,relief='solid',width=80)
Qnum=Spinbox(quiz_frame,values=["1","2","3","4","5"],state='readonly',bg="white",font=font1,width=80)
ques_points=Entry(quiz_frame,font=font1,fg='black',border=1,relief='solid',width=80)
total_time=Entry(quiz_frame,font=font1,fg='black',border=1,relief='solid',width=80)
quiz_lbl=Label(quiz_frame,text="Quiz Title",bg="white",font=font1)
quesNum_lbl=Label(quiz_frame,text="Number of Questions ",bg="white",font=font1)
quesPoints_lbl=Label(quiz_frame,text="Question point",bg="white",font=font1)
Time_lbl=Label(quiz_frame,text="Total Time",bg="white",font=font1)
addNew_quizLbl=Label(quiz_frame,font=font,fg='black',bg="white",text="CreateNewQuiz")
addNew_quizLbl.place(x=50,y=50)
# def Id_var(res):
#     return res
def get_title():
    return quiz_title.get()
def get_points():
    return int(ques_points.get())
def get_time():
    return int(total_time.get())
def get_Qnum():
    return int(Qnum.get())
def Next_Btn_Click():
    try:
        conn = sqlite3.connect('..\\Educational_System_Db.db')
        cur = conn.cursor()
        if(quiz_title.get() and ques_points.get() and total_time.get()):
            cur.execute("Insert into Quizzes(Name,Question_Numbers,Question_Mark,Total_Time,Teacher_Id) Values(?,?,?,?,?)"
                        ,[quiz_title.get().rstrip().lstrip(),int(Qnum.get()),int(ques_points.get()),int(total_time.get()),2])
            conn.commit()
            conn.close()
            question_frame.tkraise()
        else:
            messagebox.showerror(message="Make sure to insert data correctly")
    except:
        messagebox.showerror(title="DB Error", message="Make sure the queries you wrote is correct line 577")

def Back_Btn_Click():
    quizHome_frame.tkraise()
next_btn=Button(quiz_frame,text="Next",font=font,border=1,relief='flat',bg=co,fg="white",width=20,command=Next_Btn_Click)
back_btn=Button(quiz_frame,text="Back",font=font,border=1,relief='flat',bg=co,fg="white",width=20,command=Back_Btn_Click)


#-------------Placing----------------
quiz_lbl.place(x=50,y=250)
quiz_title.place(x=250,y=250)
quesNum_lbl.place(x=50,y=300)
Qnum.place(x=250,y=300)
Time_lbl.place(x=50,y=350)
total_time.place(x=250,y=350)
quesPoints_lbl.place(x=50,y=400)
ques_points.place(x=250,y=400)
next_btn.place(x=700,y=500)
back_btn.place(x=500,y=500)


root.mainloop()