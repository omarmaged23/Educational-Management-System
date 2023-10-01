from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter.ttk import Combobox
from tkinter.ttk import Style
from tkinter.ttk import Scrollbar
from tkinter import messagebox
import sqlite3

from pip._internal.metadata import Backend

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
######################### Collection
student_quiz=Frame(f_right, width=w - f_left['width'], height=h,bg='white')
student_quiz.grid(row=0,column=1)
lbl_show = Label(student_quiz, text='Quizzes', compound='left', fg='Black',font=('tahoma', 20, 'bold'),bg='white')
lbl_show.place(x=20, y=30)
# Table Methods ####################
def showAllQ():
    con=sqlite3.connect('..\\Educational_System_Db.db')
    cursor=con.cursor()
    data=cursor.execute('select * from Quizzes')
    con.commit()
    return data

def displayButtonQ():
    result = showAllQ()
    # remove tree view from other display
    Student_Quizzes.delete(*Student_Quizzes.get_children())
    lst = []
    for row in result:
        Student_Quizzes.insert('', END, values=row)
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
# Table for showing all quizzes of registered student
Student_Quizzes=ttk.Treeview(student_quiz,columns=('Id','Name','Question_Numbers','Question_Mark','Total_Time'),show='headings', selectmode=BROWSE)
st =Style()
st.theme_use('clam')
st.configure('Treeview', font=('arial', 16), rowheight=33, foreground='black', background='white')
st.map('Treeview', foreground=[('selected', '#000000')], background=[('selected', '#fca311')])
st.theme_use('clam')
st.configure('Treeview.Heading', font=('tahoma', 18, 'bold'), foreground='white', background='#012a05')
Student_Quizzes.heading('Id',text='ID')
Student_Quizzes.heading('Name',text='Quiz Name')
Student_Quizzes.heading('Question_Numbers',text='Number of Questions')
Student_Quizzes.heading('Question_Mark',text='Question Mark')
Student_Quizzes.heading('Total_Time',text='Duration')

Student_Quizzes.column('Id',width=100)
Student_Quizzes.column('Name',width=150)
Student_Quizzes.column('Question_Numbers',width=220)
Student_Quizzes.column('Question_Mark',width=220)
Student_Quizzes.column('Total_Time',width=100)
Student_Quizzes.place(x=10,y=110,width=1200,height=500)
displayButtonQ()
startQuiz_btn=Button(student_quiz,text="START QUIZ",font=font,bg=co,fg="white",width=15, height=1,relief="flat",command="")
startQuiz_btn.place(x=1050, y=645)
################ Buttons
preview_btn_img = Image.open("..\\Assets\\Icons\\icons8-edit-15.png")
preview_btn_img = preview_btn_img.resize((15, 15))
preview_btn_img_tk = ImageTk.PhotoImage(preview_btn_img)
preview_btn = Button(student_quiz, image=preview_btn_img_tk, bg='white', relief='flat',text=" Preview By Id  ", compound='right',fg='black', font=font,borderwidth=0,border=0,command="")
preview_btn.place(x=610, y=645)

#-------Combo Box -------
stdlst=displayButtonQ()
Q_Id_var=IntVar()
Std_Id_cmbox = Combobox(student_quiz, width=80,state='readonly',values=stdlst,textvariable=Q_Id_var)
Std_Id_lbl = Label(student_quiz, text="Select ID", font=font, fg='black', bg='white', anchor='w')
Std_Id_lbl.place(x=10,y=647)
Std_Id_cmbox.place(x=95,y=650)
root.mainloop()