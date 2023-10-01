import sqlite3
from tkinter import *
from tkinter import messagebox

from PIL import Image, ImageTk

try:
    conn = sqlite3.connect('..\\Educational_System_Db.db')
    cur = conn.cursor()
    cur.execute("select * from Questions where Quiz_Id=?", [24])
    result = cur.fetchall()
    print(result)
    conn.close()
except:
    messagebox.showerror(title="DB Error", message="Make sure the queries you wrote is correct")