from tkinter.ttk import *
from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
root = Tk()
root.geometry('1000x1000')
root.title('Documentation')
root.iconbitmap('/home/bc2113449/projects/MadLibs/hyd.gif')
#######################WIDGETS################################
#----label
l1=Label(root, text= 'Hello world!' , font = 'arial 30 bold')
l1.grid(row=0,column=0)
#----button
b1=Button(root,text="Submit")
b1.grid(row=0,column=1)
#----we can also add button click event
def clicked():
    b2.configure(text="You clicked on enter!!")
b2=Button(root,text="Enter",bg="red",fg="white",command=clicked,padx=50,pady=50)
b2.grid(row=0,column=3)
#----Entry(used to take input from user)
l7=Label(root, text= 'Entry class' , font = 'arial 10 bold')
l7.grid(row=1,column=0)
txt=Entry(root,width=20) ## we can also add the fg,bg colour and borderwidth
txt.insert(1,"Enter your name")
txt.grid(row=1,column=1)
def clicked():
    res="Welcome "+txt.get()
    b3.configure(text=res)
b3=Button(root,text="Click here to see magic",bg="red",fg="white",command=clicked)
b3.grid(row=1,column=2)
#---- Combobox(dropdown box)
l6=Label(root, text= 'Combobox' , font = 'arial 10 bold')
l6.grid(row=2,column=0)
combo=Combobox(root)
combo['values']=("india","pak","bangladesh","srilanka")
combo.current(0)
combo.grid(row=2,column=1)
#----Check button 
l5=Label(root, text= 'Check boxes' , font = 'arial 10 bold')
l5.grid(row=3,column=0)
chk_state=BooleanVar()   #here BooleanVar() is tkinter variable not the python variable
chk_state.set(True)
c1=Checkbutton(root,text="I have read all the conditions",var=chk_state)
c1.grid(row=3,column=1)
#----Radio button;
l4=Label(root, text= 'RadioButtons' , font = 'arial 10 bold')
l4.grid(row=4,column=0)
rad1 = Radiobutton(root,text="Python",value=1)
rad2 = Radiobutton(root,text="Java",value=2)
rad3 = Radiobutton(root,text="Scalar",value=3)
rad1.grid(column=1,row=4)
rad2.grid(column=2,row=4)
rad3.grid(column=3,row=4)
#----ScrolledText
l4=Label(root, text= 'Scrolled text' , font = 'arial 10 bold')
l4.grid(row=5,column=0)
stxt=scrolledtext.ScrolledText(root,width=20,height=10)
stxt.insert(INSERT,"____________________")
stxt.insert(INSERT,"Enter your text here")
stxt.insert(INSERT,"____________________")
stxt.grid(row=5,column=1)
#----MessageBox
l3=Label(root, text= 'MessageInfo' , font = 'arial 10 bold')
l3.grid(row=6,column=0)
def clicked1():
    messagebox.showinfo('Message title',"Message content")
b4=Button(root,text="click here for message",command=clicked1)
b4.grid(row=6,column=1)
#----Spinbox
l2=Label(root, text= 'Spinbox' , font = 'arial 10 bold')
l2.grid(row=7,column=0)
spin=Spinbox(root,from_=0,to_=20,width=5)
spin.grid(row=7,column=1)

##########Geometry Manager Classes
# 1.pack()--organizes the widgets in block,occupies the entire width
# 2.grid()--organizes the widgets in table like structure
# 3.place()--organizes the widgets at specific position that we want
Label(root,text="Username").grid(row=8)
Entry(root).grid(row=8,column=1)
Label(root,text="Password").grid(row=9)
Entry(root).grid(row=9,column=1)
Checkbutton()
chk_state2=BooleanVar()   #here BooleanVar() is tkinter variable not the python variable
chk_state2.set(False)
Checkbutton(root,text="Keep me logged in",var=chk_state2).grid(row=10,column=1)
#----Binding Function(calling functions whenever an event occur refers to binding fucntion)
#----Event Handling
# 1.<Button-1>--left click
# 2.<Button-2>--middle click
# 3.<Button-3>--Right click
l8=Label(root, text= 'EventHandling' , font = 'arial 10 bold')
l8.grid(row=11,column=0)
i = 1
def click2(event):
    global i
    Label(root,text="Hi Akshith").grid(row=12,column=i)
    i = i + 1
bt = Button(root, text="click here for event handling")
bt.bind("<Button-1>", click2)   # to bind the button widget to event handler
bt.grid(row=11, column=1)  # Use grid instead of pack to place the button
#----PhotoImage
icon=PhotoImage(file="/home/bc2113449/projects/MadLibs/hyd.gif")
l9=Label(root, text= 'PhotoImage',font = 'arial 10 bold')
l9.grid(row=13,column=0)
Label(root,image=icon).grid(row=13,column=1)



root.mainloop()

