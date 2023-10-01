from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from  tkinter.ttk import Combobox
from tkinter import messagebox
import sqlite3
import time
import datetime

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
f_right = Frame(root, width=w - f_left['width'], height=h)
f_right.grid(row=0, column=1)

question_frame = Frame(f_right, width=w - f_left['width'], height=h, bg='white')
question_frame.grid_propagate(True)
question_frame.grid(row=0, column=1)

# -------------------- Buttons Functions--------------------------------------
rd_ans=StringVar()
preview_ques_num = 0
preview_max_qes = 4
answers = [""] * preview_max_qes
##############################################################################
def Back_Btn_Click():
    global preview_ques_num
    if (preview_ques_num == 0):
        messagebox.showerror("showerror", "Error")
    else:
        # Clear The Fields
        ques_title.delete(0, END)
        op1_text.delete(0, END)
        op2_text.delete(0, END)
        op3_text.delete(0, END)
        op4_text.delete(0, END)

        preview_ques_num -= 1
        # Set The Fields Again
        set_title(new_res[preview_ques_num][1])
        set_op1(new_res[preview_ques_num][2])
        set_op2(new_res[preview_ques_num][3])
        set_op3(new_res[preview_ques_num][4])
        set_op4(new_res[preview_ques_num][5])
        ques_lbl.config(text="Question " + str(preview_ques_num + 1))


# ------------------------LABELS AND TEXTBOX CREATION-------------------------------------------
Home_lbl=Label(question_frame,text="QUIZES",bg="white",font=font)
quiz_lbl = Label(question_frame, text="Quiz Title", font=font, fg='black', bg='white', anchor='w')
quiz_title2 = Label(question_frame, height=1, font=font, fg='black', border=1, relief='solid')
ques_title = Entry(question_frame, font=font, width=80, fg='black', border=1, relief='solid')
ques_lbl = Label(question_frame, text="Question " + str(1), font=font, fg='black', bg='white', anchor='w')
timer_lbl = Label(question_frame, text="Timer",font=("Arial", 18, ""), fg='black', bg='white', anchor='w',justify=CENTER)
totalMarks_lbl=Label(question_frame, text="Total Marks :",font=("Arial", 18, ""), fg='black', bg='white', anchor='w',justify=CENTER)
totalMarks_num=Label(question_frame,font=("Arial", 18, ""), fg='black', bg='white', anchor='w',justify=CENTER)
# ---------------------------Qestions Options----------------------------------
op1_text = Entry(question_frame, font=font, fg='black',bg="White", border=1, relief='solid',width=80)
op2_text = Entry(question_frame, font=font, fg='black',bg="White", border=1, relief='solid',width=80)
op3_text = Entry(question_frame, font=font, fg='black',bg="White", border=1, relief='solid',width=80)
op4_text = Entry(question_frame, font=font, fg='black',bg="White", border=1, relief='solid',width=80)

# ---------------------------OPTIONS ANS RADIO BUTTONS----------------------------------
op1_rd = Radiobutton(question_frame, font=font, bg='white',value="A)",variable=rd_ans)
op2_rd = Radiobutton(question_frame, font=font, bg='white',value="B)",variable=rd_ans)
op3_rd = Radiobutton(question_frame, font=font, bg='white',value="C)",variable=rd_ans)
op4_rd = Radiobutton(question_frame, font=font, bg='white',value="D)",variable=rd_ans)

op1_rd_lbl=Label(question_frame,text='A)', font=font, bg='white')
op2_rd_lbl=Label(question_frame,text='B)', font=font, bg='white')
op3_rd_lbl=Label(question_frame,text='C)', font=font, bg='white')
op4_rd_lbl=Label(question_frame,text='D)', font=font, bg='white')

rd_ans.set("A)")
# ---------------------------Ans List RADIO BUTTONS----------------------------------

##########################################################

def set_title(text):
    ques_title['state']='normal'

    ques_title.delete(0, END)
    ques_title.insert(0,text)
    ques_title['state']='readonly'

    return
def set_op1(text):
    op1_text['state']='normal'
    op1_text.delete(0, END)
    op1_text.insert(0,text)
    op1_text['state']='readonly'
    return
def set_op2(text):
    op2_text['state']='normal'
    op2_text.delete(0, END)
    op2_text.insert(0,text)
    op2_text['state']='readonly'
    return
def set_op3(text):
    op3_text['state']='normal'
    op3_text.delete(0, END)
    op3_text.insert(0,text)
    op3_text['state']='readonly'
    return
def set_op4(text):
    op4_text['state']='normal'
    op4_text.delete(0, END)
    op4_text.insert(0,text)
    op4_text['state']='readonly'
    return
##########################################################
try:
    conn=sqlite3.connect("..\\Educational_System_Db.db")
    cur=conn.cursor()
    cur.execute("select * from Questions Where Quiz_Id = ?",[24]) #### Quiz_F
    new_res=cur.fetchall()
    print(new_res)
    set_title(str(new_res[0][1]).rstrip().lstrip())
    set_op1(new_res[0][2])
    set_op2(new_res[0][3])
    set_op3(new_res[0][4])
    set_op4(new_res[0][5])
    conn.close()
except:
    messagebox.showerror(message="239")
try:
    conn=sqlite3.connect("..\\Educational_System_Db.db")
    arr=conn.cursor()
    arr.execute("select * from Quizzes where Id=?",[24]) #### Quiz_F
    global Qlst
    Qlst=arr.fetchone()
    totalMarks_num['text']=Qlst[2] * Qlst[3]
    conn.close()
except:
    messagebox.showerror(message="select from quizzes")
def Next_Btn_Click():
    # Add The Question To The List
    global new_res
    global preview_ques_num
    global rd_ans
    answers[preview_ques_num] = rd_ans.get()

    # Clear The Text Fields
    ques_title.delete(0, END)
    op1_text.delete(0, END)
    op2_text.delete(0, END)
    op3_text.delete(0, END)
    op4_text.delete(0, END)
    if (preview_ques_num == preview_max_qes - 2):
        next_ques_btn.config(text="Submit")
    if (preview_ques_num == preview_max_qes - 1):
        student_score=0
        Stop_Timer()
        cur_time=(int(hourEntry.cget("text"))*60)+int(minuteEntry.cget("text"))
        Elapsed_Time=Qlst[4]-cur_time - 1
        for i in range(0,preview_max_qes):
            conn = sqlite3.connect("..\\Educational_System_Db.db")
            arrow=conn.cursor()
            arrow.execute("Select Correct_Answer from Questions where Quiz_Id = ?",[24]) #### Ques_F
            correction=arrow.fetchall()
            if(answers[i]==correction[i][0]):
                student_score+=Qlst[3]
            ##############################
            #### Warning Brain Damage ####
            ##############################
            conn.commit()
            conn.close()
        conn=sqlite3.connect("..\\Educational_System_Db.db")
        stdarrow=conn.cursor()
        var_std=7
        stdarrow.execute("Insert into Student_Quizzes(Score,Elapsed_Time,Submitted_Date,Student_Id,Quiz_Id) values(?,?,?,?,?)"
                         ,[student_score,Elapsed_Time,datetime.date.today(),8,24])#### Quiz_F
        conn.commit()
        var_std+=1
        messagebox.showinfo(message="Quiz Submitted Succeffully!")
    else:
        preview_ques_num += 1
        set_title(new_res[preview_ques_num][1])
        set_op1(new_res[preview_ques_num][2])
        set_op2(new_res[preview_ques_num][3])
        set_op3(new_res[preview_ques_num][4])
        set_op4(new_res[preview_ques_num][5])
        ques_lbl.config(text="Question " + str(preview_ques_num + 1))
# ---------------------ADDITION VARIBALES-------------------------------------
# inialize List
doTick=True
global quiz_timer
quiz_timer=Qlst[4]

##########################################################
#--------------------------TIMER------------------------
# Declaration of variables
hour = StringVar()
minute =StringVar()
second = StringVar()
# setting the default value as 0
hour.set("{:02d}".format(int(quiz_timer / 60)))
minute.set("{:02d}".format(quiz_timer%60))
second.set("00")

# Use of Entry class to take input from the user
hourEntry = Label(question_frame,border=1,bg="white", width=3, font=("Arial", 18, ""),
                  textvariable=hour)
hourEntry.place(x=450,y=150)

minuteEntry = Label(question_frame,border=1,bg="white", width=3, font=("Arial", 18, ""),
                    textvariable=minute)
minuteEntry.place(x=500,y=150)

secondEntry = Label(question_frame,border=1,bg="white", width=3, font=("Arial", 18, ""),
                    textvariable=second)
secondEntry.place(x=550,y=150)

def Timer():
    try:
        # the input provided by the user is
        # stored in here :temp
        temp = int(hour.get()) * 3600 + int(minute.get()) * 60 + int(second.get())
    except:
        print("Please input the right value")
    while temp > -1:

        # divmod(firstvalue = temp//60, secondvalue = temp%60)
        mins, secs = divmod(temp, 60)

        # Converting the input entered in mins or secs to hours,
        # mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr :
        # 50min: 0sec)
        hours = 0
        if mins > 60:
            # divmod(firstvalue = temp//60, secondvalue
            # = temp%60)
            hours, mins = divmod(mins, 60)

        # using format () method to store the value up to
        # two decimal places
        hour.set("{:02d}".format(hours))
        minute.set("{:02d}".format(mins))
        second.set("{:02d}".format(secs))

        # updating the GUI window after decrementing the
        # temp value every time
        question_frame.update()
        time.sleep(1)

        # when temp value = 0; then a messagebox pop's up
        # with a message:"Time's up"
        if (temp == 0):
            messagebox.showinfo("Time Countdown", "Time's up ")

        # after every one sec the value of temp will be decremented
        # by one
        temp -= 1

def Stop_Timer():
    global doTick
    doTick=False
#-------------------------END_TIMER---------------------


# ---------------------------Buttons---------------------------------
next_ques_btn = Button(question_frame, text="Next", width=15, height=1, bg=co, fg='white', font=font, relief="flat",
                      command=Next_Btn_Click)
back_btn = Button(question_frame, text="Back", width=15, height=1, bg=co, fg='white', font=font, relief="flat",
                  command=Back_Btn_Click)
# ---------------------------PLACING----------------------------------
Home_lbl.place(x=50,y=50)
ques_lbl.place(x=50, y=250)
ques_title.place(x=250, y=250)
op1_rd.place(x=190, y=300)
op1_text.place(x=250, y=300)
op1_rd_lbl.place(x=220,y=300)

op2_text.place(x=250, y=350)
op2_rd.place(x=190, y=350)
op2_rd_lbl.place(x=220,y=350)

op3_text.place(x=250, y=400)
op3_rd.place(x=190, y=400)
op3_rd_lbl.place(x=220,y=400)

op4_text.place(x=250, y=450)
op4_rd.place(x=190, y=450)
op4_rd_lbl.place(x=220,y=450)

next_ques_btn.place(x=825, y=500)
back_btn.place(x=250, y=500)
timer_lbl.place(x=300,y=150)
totalMarks_lbl.place(x=800,y=150)
totalMarks_num.place(x=960,y=150)
Timer()
root.mainloop()