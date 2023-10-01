from tkinter import *
from PIL import Image, ImageTk
from  tkinter.ttk import Combobox
from tkinter import messagebox
import sqlite3
#---------Labels Fonts----------#
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

#------------------------Quizes---------------------------------------------

# Create Quiz Frame
question_frame_edt = Frame(root, width=w - f_left['width'], height=h,bg='white')
question_frame_edt.grid_propagate(True)
question_frame_edt.grid(row=0, column=1)
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


def Add_Btn_Click():
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
        root.destroy()
        import TeacherMain
    else:
        ques_num_edt += 1
        ques_lbl_edt.config(text="Question " + str(ques_num_edt + 1))


def Back_Btn_edt():
    global ques_num_edt
    if(ques_num_edt==0):
        messagebox.showerror("showerror", "Error")
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
add_ques_btn_edt=Button(question_frame_edt,text="ADD",width=15,height=1,bg=co,fg='white',font=font,relief="flat",command=Add_Btn_Click)
back_btn_edt=Button(question_frame_edt,text="Back",width=15,height=1,bg=co,fg='white',font=font,relief="flat",command=Back_Btn_edt)


# ---------------------------PLACING----------------------------------
try:
    conn = sqlite3.connect('..\\Educational_System_Db.db')
    cur = conn.cursor()
    cur.execute("select * from Questions where Quiz_Id=?", [6])
    result = cur.fetchall()
    result=result[0]
    ques_title_edt.insert(0,str(result[1]).rstrip().lstrip())
    op1_text_edt.insert("1.0",result[2])
    op2_text_edt.insert("1.0", result[3])
    op3_text_edt.insert("1.0",result[4])
    op4_text_edt.insert("1.0",result[5])
    ans_var_edt.set(result[6])
    conn.close()
except:
    messagebox.showerror(title="Set Error", message="set wla ragel")
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
root.mainloop()