from tkinter import *

root = Tk()

name_list={}

nameh =Entry(root)
nameh.grid(row=0,column=1)
surname =Entry(root)
surname.grid(row=1,column=1)

mylabel1 = Label(root,text="Enter your name: ")
mylabel1.grid(row=0,column=0)
mylabel2 = Label(root,text="Enter surname: ")
mylabel2.grid(row=1,column=0)

def add(nameh,surname):
    names = nameh.get()
    surnames = surname.get()
    name_list[names] = surnames
    mylabel= Label(root,text=f"was added")
    mylabel1.grid(row=3,column=1)

def del_name(name):
    if name in name_list:
        del name_list[name]
    mylbl = Label(root,text=f"{name} is deleted " + surname.get())
    mylbl.grid(row=6,column=2)


def display_names():
    m1 = Label(root,text={name_list})
    m1.grid(row=9,column=9)


button1 = Button(root,text="delete",command=del_name)
button1.grid(row=4,column=3)
button2 = Button(root,text="Add",command=add)
button2.grid(row=5,column=3)
button3 = Button(root,text="display",command=display_names)
button3.grid(row=6,column=3)


root.mainloop()