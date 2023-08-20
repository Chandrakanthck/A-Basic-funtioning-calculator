from tkinter import *

ck=Tk()
ck.title("Calculator")

a=Entry(ck,text="")
a.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def button_click(number):
    current=a.get()
    a.delete(0,END)
    a.insert(0,str(current)+str(number))

def button_clear():
    a.delete(0,END)

def button_add():
    a_num=a.get()
    global f_num
    f_num=int(a_num)
    a.delete(0,END)

def button_equal():
    sec_num=a.get()
    a.delete(0,END)
    a.insert(0,f_num+int(sec_num))
    
def button_sub():
    return

def button_mult():
    return

def button_div():
    return

#defining buttons


button_1=Button(ck,text="1",padx=30,pady=20,command=lambda:button_click(1))
button_2=Button(ck,text="2",padx=30,pady=20,command=lambda:button_click(2))
button_3=Button(ck,text="3",padx=30,pady=20,command=lambda:button_click(3))
button_4=Button(ck,text="4",padx=30,pady=20,command=lambda:button_click(4))
button_5=Button(ck,text="5",padx=30,pady=20,command=lambda:button_click(5))
button_6=Button(ck,text="6",padx=30,pady=20,command=lambda:button_click(6))
button_7=Button(ck,text="7",padx=30,pady=20,command=lambda:button_click(7))
button_8=Button(ck,text="8",padx=30,pady=20,command=lambda:button_click(8))
button_9=Button(ck,text="9",padx=30,pady=20,command=lambda:button_click(9))
button_0=Button(ck,text="0",padx=30,pady=20,command=lambda:button_click(0))
#now here additioning, or clearing screen and blablablaaa
button_add=Button(ck,text="+",padx=30,pady=20,command=button_add)
button_equal=Button(ck,text="=",padx=69,pady=20,command=button_equal)
button_clear=Button(ck,text="clear",padx=59,pady=20,command=button_clear)

button_sub=Button(ck,text="-",padx=30,pady=20,command=button_sub())
button_mult=Button(ck,text="x",padx=30,pady=20,command=button_mult())
button_div=Button(ck,text="÷",padx=30,pady=20,command=button_div())

#Button Grids and Size
button_1.grid(row=1,column=0)
button_2.grid(row=1,column=1)
button_3.grid(row=1,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=3,column=0)
button_8.grid(row=3,column=1)
button_9.grid(row=3,column=2)

button_0.grid(row=4,column=0)
button_add.grid(row=5,column=0)
button_equal.grid(row=4,column=1,columnspan=2)
button_clear.grid(row=5,column=1,columnspan=2)

button_sub.grid(row=6,column=0)
button_mult.grid(row=6,column=1)
button_div.grid(row=6,column=2)

ck.mainloop()
