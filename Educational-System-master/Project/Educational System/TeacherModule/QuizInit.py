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

# creation of fonts
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

#-------------------------Create Quiz--------------------

quiz_frame=Frame(root, width=w - f_left['width'], height=h,bg='white')
quiz_frame.grid(row=0,column=1)
font1=('tahoma', 15)
quiz_title=Entry(quiz_frame,font=font1,fg='black',border=1,relief='solid',width=80)
Qnum=Spinbox(quiz_frame,values=["1","2","3","4","5"],state='readonly',bg="white",font=font1,width=80)
ques_points=Entry(quiz_frame,font=font1,fg='black',border=1,relief='solid',width=80)
total_time=Entry(quiz_frame,font=font1,fg='black',border=1,relief='solid',width=80)
quiz_lbl=Label(quiz_frame,text="Quiz Title",bg="white",font=font1)
quesNum_lbl=Label(quiz_frame,text="Number of Questions ",bg="white",font=font1)
quesPoints_lbl=Label(quiz_frame,text="Question point",bg="white",font=font1)
Time_lbl=Label(quiz_frame,text="Total Time",bg="white",font=font1)
def Next_Btn_Click():
    try:
        conn = sqlite3.connect('..\\Educational_System_Db.db')
        cur = conn.cursor()
        if(quiz_title.get() and ques_points.get() and total_time.get()):
            cur.execute("Insert into Quizzes(Name,Question_Numbers,Question_Mark,Total_Time,Teacher_Id) Values(?,?,?,?,?)"
                        ,[quiz_title.get().rstrip().lstrip(),int(Qnum.get()),int(ques_points.get()),int(total_time.get()),2])
            conn.commit()
            conn.close()
            root.destroy()
            import Quiz
    except:
        messagebox.showerror(title="DB Error", message="Make sure the queries you wrote is correct")

next_btn=Button(quiz_frame,text="Next",font=font,border=1,relief='flat',bg="gray",fg="white",width=20,command=Next_Btn_Click)
back_btn=Button(quiz_frame,text="Back",font=font,border=1,relief='flat',bg="gray",fg="white",width=20)


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