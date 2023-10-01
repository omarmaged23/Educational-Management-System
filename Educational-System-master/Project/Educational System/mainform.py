from tkinter import *
from tkinter import ttk
import backEnd_DB
import tkinter.messagebox


# center the main window according to screen
def centerWindow(root, width, height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    x = int((screenwidth - width)/2)
    y = int((screenheight - height)/2)
    root.geometry(f"{width}x{height}+{x}+{y}")



#*************** 1 - create main form called root  with no resizable ,centered window *******
root=Tk()
root_width=1300
root_height=600
blankspace=' '
root.title(200*blankspace +'Student Management System')
centerWindow(root,root_width,root_height)
root.resizable(False,False)
#************* create table of student for database****************
backEnd_DB.studentData()

#**************** 2- create main frames **********************************
mainframe=Frame(root,width=root_width,height=root_height,bg='cadet blue')
mainframe.grid()

#top frame for title
titleFrame=Frame(mainframe,bd=7,width=1300,height=100,relief=RIDGE)
titleFrame.grid(row=0,column=0)

#middle frame for entries and treeview
#topframe3
middleFrame=Frame(mainframe,bd=7,width=1300,height=400,relief=RIDGE,bg='cadet blue')
middleFrame.grid(row=1,column=0,pady=8)

#this middle separated into two frames
#1-Labels and entries
leftMiddleFrame=Frame(middleFrame,width=500,height=400)
leftMiddleFrame.grid(row=0,column=0,padx=10)
#2-treeView
RightMiddleFrame=Frame(middleFrame,width=750,height=400)
RightMiddleFrame.grid(row=0,column=1,padx=10)

#bottom frame for buttons
#topframe1
bottomFrame=Frame(mainframe,bd=7,width=1300,height=60,relief=RIDGE)
bottomFrame.grid(row=2,column=0,pady=8)


#**************** 3- make title **********************************
titleLabel=Label(titleFrame,font=('arial',45,'bold'),text='Student Management system')
titleLabel.grid(row=0,column=0,padx=225)


#**************** 4- make Labels and Entries **********************************
#student id
stdIDLabel=Label(leftMiddleFrame,font=('arial',12,'bold'),text='Student ID')
stdIDLabel.grid(row=0,column=0,padx=10,pady=10)
stdIDEntry=Entry(leftMiddleFrame,bd=5,font=('arial',12,'bold'),width=40)
stdIDEntry.grid(row=0,column=1,padx=10,pady=10)

#first name
fnameLabel=Label(leftMiddleFrame,font=('arial',12,'bold'),text='First Name')
fnameLabel.grid(row=1,column=0,padx=10,pady=10)
fnameEntry=Entry(leftMiddleFrame,bd=5,font=('arial',12,'bold'),width=40)
fnameEntry.grid(row=1,column=1,padx=10,pady=10)

#last name
lnameLabel=Label(leftMiddleFrame,font=('arial',12,'bold'),text='Last Name')
lnameLabel.grid(row=2,column=0,padx=10,pady=10)
lnameEntry=Entry(leftMiddleFrame,bd=5,font=('arial',12,'bold'),width=40)
lnameEntry.grid(row=2,column=1,padx=10,pady=10)

#age
ageLabel=Label(leftMiddleFrame,font=('arial',12,'bold'),text='Age')
ageLabel.grid(row=3,column=0,padx=10,pady=10)
ageEntry=Entry(leftMiddleFrame,bd=5,font=('arial',12,'bold'),width=40)
ageEntry.grid(row=3,column=1,padx=10,pady=10)

#gender
genderLabel=Label(leftMiddleFrame,font=('arial',12,'bold'),text='Gender')
genderLabel.grid(row=4,column=0,padx=10,pady=10)
gendercombobox=ttk.Combobox(leftMiddleFrame,font=('arial',12,'bold'),width=39,state='readonly',values=('','Femal','Male'))
gendercombobox.grid(row=4,column=1,padx=10,pady=10)

#address
addressLabel=Label(leftMiddleFrame,font=('arial',12,'bold'),text='Address')
addressLabel.grid(row=5,column=0,padx=10,pady=10)
addressEntry=Entry(leftMiddleFrame,bd=5,font=('arial',12,'bold'),width=40)
addressEntry.grid(row=5,column=1,padx=10,pady=10)

#mobile
mobileLabel=Label(leftMiddleFrame,font=('arial',12,'bold'),text='Mobile')
mobileLabel.grid(row=6,column=0,padx=10,pady=10)
mobileEntry=Entry(leftMiddleFrame,bd=5,font=('arial',12,'bold'),width=40)
mobileEntry.grid(row=6,column=1,padx=10,pady=10)


#**************** 5-  make TreeView to display data **********************************

#help to make capapbility of scrolling data
scroll_x=Scrollbar(RightMiddleFrame,orient=HORIZONTAL)
scroll_y=Scrollbar(RightMiddleFrame,orient=VERTICAL)

studentList=ttk.Treeview(RightMiddleFrame,height=12,columns=('stdID','fname','lname','age','gender','address','mobile'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

scroll_x.configure(command=studentList.xview)
scroll_y.configure(command=studentList.yview)

scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)

studentList.heading('stdID',text='Student ID')
studentList.heading('fname',text='First Name')
studentList.heading('lname',text='Last Name')
studentList.heading('age',text='Age')
studentList.heading('gender',text='Gender')
studentList.heading('address',text='Address')
studentList.heading('mobile',text='Mobile')

studentList['show']='headings'


studentList.column('stdID',width=70)
studentList.column('fname',width=100)
studentList.column('lname',width=100)
studentList.column('age',width=70)
studentList.column('gender',width=70)
studentList.column('address',width=150)
studentList.column('mobile',width=120)

studentList.pack(fill=BOTH,expand=True)

#**************** 7-  Buttons functions **********************************************
def exitButton():
    clear=tkinter.messagebox.askyesno('Student Management System','Confirm if you want to Exit')
    if clear>0:
        root.destroy()
        return 
    
def resetButton():
    stdIDEntry.delete(0,END)
    fnameEntry.delete(0,END)
    lnameEntry.delete(0,END)
    ageEntry.delete(0,END)
    gendercombobox.set('')
    addressEntry.delete(0,END)
    mobileEntry.delete(0,END)
    
def addButton():
    if stdIDEntry.get()==''or fnameEntry.get()==''or lnameEntry.get()=='' or ageEntry.get()=='' or gendercombobox.get()=='' or addressEntry.get()=='' or mobileEntry.get()=='':
    
        tkinter.messagebox.askokcancel('System','please fill all data required for student')
    else:
        backEnd_DB.addStudent(
                stdIDEntry.get(),
                fnameEntry.get(),
                lnameEntry.get(),
                ageEntry.get(),
                gendercombobox.get(),
                addressEntry.get(),
                mobileEntry.get()
                )
        studentList.insert('',END,values=(
                stdIDEntry.get(),
                fnameEntry.get(),
                lnameEntry.get(),
                ageEntry.get(),
                gendercombobox.get(),
                addressEntry.get(),
                mobileEntry.get()
                ))
    
def displayButton():
    result =backEnd_DB.showAllStudent()
    #remove tree view from other display
    studentList.delete(*studentList.get_children())
    for row in result:
        studentList.insert('',END,values=row)
        
        
def deleteButton():
    student_id=stdIDEntry.get()
    if len(student_id) != 0:
        backEnd_DB.deleteStudent(student_id)
        displayButton()
        tkinter.messagebox.showinfo('System','record sucessfully deleted')
    else:
        tkinter.messagebox.showinfo('System','you must enter student id first')
    
def updateButton():  
    if stdIDEntry.get()==''or fnameEntry.get()==''or lnameEntry.get()=='' or ageEntry.get()=='' or gendercombobox.get()=='' or addressEntry.get()=='' or mobileEntry.get()=='':
         tkinter.messagebox.askokcancel('System','please fill all data required for student')
    else:
        
        backEnd_DB.updateStudent(
                stdIDEntry.get(),
                fnameEntry.get(),
                lnameEntry.get(),
                ageEntry.get(),
                gendercombobox.get(),
                addressEntry.get(),
                mobileEntry.get()
                )
        displayButton()
        tkinter.messagebox.showinfo('System','record sucessfully updated')
    
#**************** 6-  add Buttons ****************************************************

btnfont=('arial',20,'bold')

btnAdd=Button(bottomFrame,pady=5,bd=4,font=btnfont,text='Add',width=11,command=addButton)
btnAdd.grid(row=0,column=0,padx=1)

btnDisplay=Button(bottomFrame,pady=5,bd=4,font=btnfont,text='Display',width=11,command=displayButton)
btnDisplay.grid(row=0,column=1,padx=1)

btnDelete=Button(bottomFrame,pady=5,bd=4,font=btnfont,text='Delete',width=11,command=deleteButton)
btnDelete.grid(row=0,column=2,padx=1)

btnUpdate=Button(bottomFrame,pady=5,bd=4,font=btnfont,text='Update',width=11,command=updateButton)
btnUpdate.grid(row=0,column=3,padx=1)

btnReset=Button(bottomFrame,pady=5,bd=4,font=btnfont,text='Reset',width=11,command=resetButton)
btnReset.grid(row=0,column=4,padx=1)

btnEXit=Button(bottomFrame,pady=5,bd=4,font=btnfont,text='Exit',width=11,command=exitButton)
btnEXit.grid(row=0,column=5,padx=1)


root.mainloop()
