import string 
import random
from tkinter import *

root =Tk()
root.title("password generator tool")
root.geometry("350x250")


label_title = Label(root, text="Choose the Strength of your password", fg="white", bg="blue", font=("helvtica",15))
label_title.pack()

def selection():
    selection = choice.get()


choice = IntVar()
rb1 = Radiobutton(root, text="Poor Password", variable=choice,value=1,command=selection)
rb1.pack()
rb2 = Radiobutton(root, text="Average Password", variable=choice,value=2,command=selection)
rb2.pack()
rb3 = Radiobutton(root, text="Strong Password", variable=choice,value=3,command=selection)
rb3.pack()

label_space = Label(root)
label_space.pack()
label_password = Label(root, text="Choose the strength of your password ")
label_password.pack()

val = IntVar()
Spinlength = Spinbox(root, from_=8, to_=30, textvariable=val, width=15,)
Spinlength.pack()

def callback():
    result.config(text=passgen())

button_submit = Button(root, text="Generate Password",command=callback)
button_submit.pack(pady=10)

result = Message(root,text="",relief=RAISED, width=200,font=(25))
result.pack(side=BOTTOM)

poor = string.ascii_uppercase + string.ascii_lowercase
average = string.ascii_uppercase + string.ascii_lowercase + string.digits
advance = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation

def passgen():
    if choice.get() == 1:
        return "".join(random.sample(poor,val.get()))
    elif choice.get() == 2:
        return "".join(random.sample(average,val.get()))
    elif choice.get() == 3:
        return "".join(random.sample(advance,val.get()))

root.mainloop()
