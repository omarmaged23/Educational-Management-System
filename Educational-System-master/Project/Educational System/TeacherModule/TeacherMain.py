from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from  tkinter.ttk import Combobox
from tkinter import messagebox

import sqlite3
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
f_right = Frame(root, width=w - f_left['width'], height=h)
f_right.grid(row=0, column=1)
#--------------------QUIZES HOME PAGE------------------------
quizHome_frame = Frame(f_right, width=w - f_left['width'], height=h, bg='white')
quizHome_frame.grid_propagate(True)
quizHome_frame.grid(row=0, column=1)
#--------------------Labels-----------------------
Home_lbl=Label(f_right,text="QUIZES",bg="white",font=font)
#--------------------BUTTONS------------------------
addQuiz_btn=Button(quizHome_frame,text="ADD",font=font,bg=co,fg="white",width=15, height=1,relief="flat")
# ------------------- Display in table -----------------------
#-------------------Quizz Table--------------------
#with Image.open("..\\Assets\\Icons\\icons8-edit-15.png") as edit_img:

Quizzes=ttk.Treeview(f_right,columns=('Id','Name','Question_Numbers','Question_Mark','Total_Time'),show='headings')
Quizzes.heading('Id',text='ID')
Quizzes.heading('Name',text='Quiz Name')
Quizzes.heading('Question_Numbers',text='Number of Questions')
Quizzes.heading('Question_Mark',text='Question Mark')
Quizzes.heading('Total_Time',text='Duration')

#Quizzes.insert(parent="",index=END,text="",image=PhotoImage(file="..\\Assets\\Icons\\icons8-edit-15.png"))
#image=PhotoImage(file="..\\Assets\\Icons\\icons8-trash-26.png")

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
def Delete():
    try:
        conn=sqlite3.connect("..\\Educational_System_Db.db")
        curr=conn.cursor()
        curr.execute("Delete From Quizzes where Id=?",[Id_var.get()])
        conn.commit()
        curr.execute("Delete From Questions where Quiz_Id=?", [Id_var.get()])
        conn.commit()
        conn.close()
        displayButton()
        messagebox.showinfo(title="Success",message="Quiz Deleted Successfully")
    except:
        messagebox.showerror(title="Error",message="Something went wrong DELETE Failed")
def Edit():
    pass
# Edit and Delete Icons
lst=displayButton()
I_Edit = Image.open(r"..\Assets\Icons\icons8-edit-15.png")
I_Edit = I_Edit.resize((15, 15))
I_Edit_tk = ImageTk.PhotoImage(I_Edit)
btn_Edit = Button(f_right, image=I_Edit_tk, bg='white', relief='flat',text="Edit By Id", compound='left',
                       fg='black', font=font,borderwidth=0,border=0)
btn_Edit.place(x=610, y=645)
# -------------------------
I_Delete = Image.open(r"..\\Assets\\Icons\\icons8-trash-26.png")
I_Delete = I_Delete.resize((15, 15))
I_Delete_tk = ImageTk.PhotoImage(I_Delete)
btn_Delete = Button(f_right, image=I_Delete_tk, bg='white', relief='flat',text="Delete By Id", compound='left',
                       fg='black', font=font,borderwidth=0,border=0,command=Delete)
btn_Delete.place(x=710, y=645)
#-------Combo Box -------
Id_var=IntVar()
Id_cmbox = Combobox(f_right, width=80,state='readonly',values=lst,textvariable=Id_var)
Id_lbl = Label(f_right, text="Select ID", font=font, fg='black', bg='white', anchor='w')
Id_lbl.place(x=10,y=647)
Id_cmbox.place(x=95,y=650)
#--------------------------
# InsertBtn = Button(f_right,text='Refresh',font=font,width=25,command=displayButton)
# InsertBtn.place(x=10,y=270)
addQuiz_btn=Button(quizHome_frame,text="ADD",font=font,bg=co,fg="white",width=15, height=1,relief="flat")
addQuiz_btn.place(x=10, y=200)
root.mainloop()