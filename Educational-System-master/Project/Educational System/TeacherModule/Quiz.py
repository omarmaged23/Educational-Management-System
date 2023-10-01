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
question_frame = Frame(root, width=w - f_left['width'], height=h,bg='white')
question_frame.grid_propagate(True)
question_frame.grid(row=0, column=1)
#---------------------ADDITION VARIBALES-------------------------------------
ques_num = 0
max_qes = 5
num=5
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
    if (ques_num == max_qes - 1):
        for i in range(0,max_qes):
            conn = sqlite3.connect("..\\Educational_System_Db.db")
            conn.execute(
                'Insert into Questions(Header,Choose_1,Choose_2,Choose_3,Choose_4,Correct_Answer,Quiz_Id) values(?,?,?,?,?,?,?)'
                , [questions[i][0],questions[i][1],questions[i][2],questions[i][3],questions[i][4],questions[i][5],6])
            conn.commit()
            conn.close()
        messagebox.showinfo("Success", "Quiz Added Succeffully!")
    else:
        ques_num += 1
        ques_lbl.config(text="Question " + str(ques_num + 1))

def Insert_Btn_Click():
    global questions
    print(questions)

def Back_Btn_Click():
    global ques_num
    if(ques_num==0):
        messagebox.showerror("showerror", "Error")
    else:
        #Clear The Fields
        ques_title.delete(0, END)
        op1_text.delete('1.0', END)
        op2_text.delete('1.0', END)
        op3_text.delete('1.0', END)
        op4_text.delete('1.0', END)

        ques_num-=1
        #Set The Fields Again
        ques_title.insert(0,questions[ques_num][0])
        op1_text.insert('1.0',questions[ques_num][1])
        op2_text.insert('1.0',questions[ques_num][2])
        op3_text.insert('1.0',questions[ques_num][3])
        op4_text.insert('1.0',questions[ques_num][4])
        ques_lbl.config(text="Question " + str(ques_num + 1))


#------------------------LABELS AND TEXTBOX CREATION-------------------------------------------

quiz_lbl=Label(question_frame,text="Quiz Title",font=font,fg='black',bg='white',anchor='w')
quiz_title=Text(question_frame,height=1,font=font,fg='black',border=1,relief='solid')
ques_title = Entry(question_frame, font=font, width=80, fg='black', border=1, relief='solid', )
ques_lbl = Label(question_frame, text="Question "+str(1), font=font, fg='black', bg='white', anchor='w')
# ---------------------------Qestion Options----------------------------------
op1_text = Text(question_frame, height=1, font=font, fg='black', border=1, relief='solid')
op2_text = Text(question_frame, height=1, font=font, fg='black', border=1, relief='solid')
op3_text = Text(question_frame, height=1, font=font, fg='black', border=1, relief='solid')
op4_text = Text(question_frame, height=1, font=font, fg='black', border=1, relief='solid')

# ---------------------------OPTIONS ANS RADIO BUTTONS----------------------------------
ans = IntVar()
op1_lbl = Label(question_frame, text="A)", font=font, bg='white')
op2_lbl = Label(question_frame, text="B)", font=font, bg='white')
op3_lbl = Label(question_frame, text="C)", font=font, bg='white')
op4_lbl = Label(question_frame, text="D)", font=font, bg='white')

# ---------------------------Ans List RADIO BUTTONS----------------------------------
ans_var=StringVar()
ans_var.set('A)')
ans_cmbox = Combobox(question_frame, width=80,state='readonly',values=['A)','B)','C)','D)'],textvariable=ans_var)
ans_lbl = Label(question_frame, text="Answer", font=font, fg='black', bg='white', anchor='w')

# ---------------------------Buttons---------------------------------
add_ques_btn=Button(question_frame,text="ADD",width=15,height=1,bg=co,fg='white',font=font,relief="flat",command=Add_Btn_Click)
back_btn=Button(question_frame,text="Back",width=15,height=1,bg=co,fg='white',font=font,relief="flat",command=Back_Btn_Click)
insert_btn=Button(question_frame,text="insert",width=15,height=1,bg=co,fg='white',font=font,relief="flat",command=Insert_Btn_Click)

# ---------------------------PLACING----------------------------------
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
add_ques_btn.place(x=825,y=600)
back_btn.place(x=250,y=600)
insert_btn.place(x=250,y=800)
root.mainloop()