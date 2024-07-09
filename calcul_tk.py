import tkinter as tk
import math
from PIL import Image, ImageTk

window = tk.Tk()
window.geometry("500x700")
window.title("Calculator")

def btn(number):
    entr.insert(tk.END, number)

def syl(symbal):
    global num1,num2,oper
    num1=entr.get()
    oper=symbal
    entr.insert(tk.END,oper)
    num2=entr.get()

def clear():    
    entr.delete(0,tk.END)    

def equal():
    inp=entr.get()
    num2=str(inp[inp.index(oper)+1:])
    entr.delete(0, tk.END)
    if oper=='+':
        # print(int(num1)+int(num2))
       entr.insert(0, str(int(num1)+int(num2)))
    elif oper=='-':
       entr.insert(0, str(int(num1)-int(num2)))
    elif oper=='*':
       entr.insert(0, str(int(num1)*int(num2)))
    elif oper=='/':
       try:
            entr.insert(0, str(int(num1)/int(num2)))
       except ZeroDivisionError:
            # in case there is a zero in the denominator, answer is undefined
            entr.insert(0, "Can't divide by zero")     
img = "myimage.png"
x = Image.open(img)
new_img = ImageTk.PhotoImage(x)

lbl = tk.Label(window,image = new_img, height=200, width=200)
lbl.pack(fill="x",pady=20)

fram1 = tk.Frame(window, relief = "groove")
fram1.pack()

entr = tk.Entry(fram1,textvariable="data", justify="right", font = ("robort", 20, "bold"),bd=20)
entr.grid(row=0, column=1)

fram2 = tk.Frame(window, relief = "groove")
fram2.pack()


lbl = tk.Button(fram2, text="7", font = ("robort", 25, "bold"), bd=10,command=lambda:btn("7"))
lbl.grid(row=1,column=0)
lbl1 = tk.Button(fram2, text="8", font = ("robort",25 , "bold") ,bd=10,command=lambda:btn("8"))
lbl1.grid(row=1,column=1, padx=5)
lbl2 = tk.Button(fram2, text="9", font = ("robort", 25, "bold"), bd=10,command=lambda:btn("9"))
lbl2.grid(row=1,column=2, padx=5)
lbl3 = tk.Button(fram2, text="/", font = ("robort", 28, "bold" ),bd=10,command=lambda:syl("/"))
lbl3.grid(row=1,column=3, padx=5)

lblx = tk.Button(fram2, text="4", font = ("robort", 25, "bold"), bd=10,command=lambda:btn("4"))
lblx.grid(row=2,column=0, padx=5)
lblx1 = tk.Button(fram2, text="5", font = ("robort", 25, "bold") ,bd=10,command=lambda:btn("5"))
lblx1.grid(row=2,column=1, padx=5)
lblx2 = tk.Button(fram2, text="6", font = ("robort", 25, "bold"), bd=10,command=lambda:btn("6"))
lblx2.grid(row=2,column=2, padx=5)
lblx3 = tk.Button(fram2, text="*", font = ("robort", 25, "bold" ),bd=10,command=lambda:syl("*"))
lblx3.grid(row=2,column=3, padx=5)

lb = tk.Button(fram2, text="1", font = ("robort", 25, "bold"), bd=10,command=lambda:btn(1))
lb.grid(row=3,column=0, padx=5)
lb1 = tk.Button(fram2, text="2", font = ("robort", 25, "bold") ,bd=10,command=lambda:btn(2))
lb1.grid(row=3,column=1, padx=5)
lb2 = tk.Button(fram2, text="3", font = ("robort", 25, "bold"), bd=10,command=lambda:btn(3))
lb2.grid(row=3,column=2, padx=5)
lb3 = tk.Button(fram2, text="-", font = ("robort", 28, "bold" ),bd=10,command=lambda:syl("-"))
lb3.grid(row=3,column=3, padx=5)


l = tk.Button(fram2, text="0", font = ("robort", 25, "bold"), bd=10,command=lambda:btn(0))
l.grid(row=4,column=0, padx=5)
l1 = tk.Button(fram2, text="c", font = ("robort", 25, "bold") ,bd=10,command=clear)
l1.grid(row=4,column=1, padx=2)
l2 = tk.Button(fram2, text="+", font = ("robort", 25, "bold"), bd=10,command=lambda:syl("+"))
l2.grid(row=4,column=2, padx=5)
l3 = tk.Button(fram2, text="=", font = ("robort", 25, "bold" ),bd=10,command=equal)
l3.grid(row=4,column=3, padx=5)


window.mainloop()



















