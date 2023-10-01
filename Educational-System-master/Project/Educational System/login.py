from tkinter import *
from tkinter import messagebox
from tkinter import Frame

root= Tk()
width=500
height=300
padx=10
pady=10
screenwidth=root.winfo_screenwidth()
screenheight=root.winfo_screenheight()
x=int((screenwidth-width) / 2)
y=int((screenheight-height) / 2)
root.title("login")
root.geometry(f"{width}x{height}+{x}+{y}")
root.resizable(False,False)
font=("Tahoma",12)

frame=Frame(root)
def check_user():
    validuser="omar"
    validpass="1234"
    username=txt_user.get()
    password=txt_pass.get()
    if(validuser==username and validpass==password):
        messagebox.showinfo("login","User logged in successfully!")
    else:
        messagebox.showerror("error","username or password is incorrect :(")
lbl_user=Label(frame,text="username",font=font)
txt_user=Entry(frame,font=font)
lbl_pass=Label(frame,text="password",font=font)
txt_pass=Entry(frame,show="*",font=font)
btn=Button(frame,text="login",command=check_user,font=font,bg="darkred",fg="white")

lbl_user.grid(row=0,column=0,padx=padx,pady=pady)
txt_user.grid(row=0,column=1,padx=padx,pady=pady)

lbl_pass.grid(row=1,column=0,padx=padx,pady=pady)
txt_pass.grid(row=1,column=1,padx=padx,pady=pady)

btn.grid(row=2,column=0,columnspan=2,padx=padx,pady=pady)

frame.place(anchor="center",relx=0.5,rely=0.5)
root.mainloop()