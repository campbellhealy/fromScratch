import tkinter
from tkinter import Tk, Entry, Label, Button

def delete():
    ''' Clears all four edit boxes'''
    N1.delete(0, "end")
    N2.delete(0, "end")
    O1.delete(0, "end")
    A1.delete(0, "end")


def proces():
    ''' Takes two operands and an operator and performs the calculation'''
    number1= int(Entry.get(N1))
    number2= int(Entry.get(N2))
    operator= Entry.get(O1)

    if operator =="+":
        answer=number1+number2
    elif operator =="-":
        answer=number1-number2
    elif operator=="*":
        answer=number1*number2
    elif operator=="/":
        answer=number1/number2

    Entry.insert(A1,0,answer)
    print(" ",answer)

root = Tk()
root.title("My Calculator")
root.geometry("300x230")
L1 = Label(root, text="VC Healy",).grid(row=0,column=1)
L2 = Label(root, text="Value 1",).grid(row=1,column=0)
L3 = Label(root, text="Value 2",).grid(row=2,column=0)
L4 = Label(root, text="Operator",).grid(row=3,column=0)
L4 = Label(root, text="Answer",).grid(row=4,column=0)
N1 = Entry(root, bd =5)
N1.grid(row=1,column=1)
N2 = Entry(root, bd =5)
N2.grid(row=2,column=1)
O1 = Entry(root, bd =5)
O1.grid(row=3,column=1)
A1 = Entry(root, bd =5)
A1.grid(row=4,column=1)
B=Button(root, text ="Submit",command = proces).grid(row=5,column=1,)
clearButton = Button(root, text = "Clear", command = delete).grid(row=6,column=1,)

root.mainloop()
