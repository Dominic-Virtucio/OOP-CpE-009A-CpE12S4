from tkinter import *

class MyWindow:
    def __init__(self, win):
        win.configure(bg="dark green")
        
        self.Label1 = Label(win, text="Calculator", fg="white", bg="dark green", font=("Helvetica", 36, "bold"))
        self.Label1.place(x=90, y=40)
        
        self.Label5 = Label(win, text="---------------------------------", fg="white", bg="dark green", font=("Helvetica", 15, "bold"))
        self.Label5.place(x=90, y=90)
        
        self.Label2 = Label(win, text="Number 1: ", bg="dark green", fg="white", font=("Helvetica", 10, "bold"))
        self.Label2.place(x=90, y=120)
        self.Entry1 = Entry(win, bd=2)
        self.Entry1.place(x=200, y=120)
        
        self.Label3 = Label(win, text="Number 2: ", bg="dark green", fg="white", font=("Helvetica", 10, "bold"))
        self.Label3.place(x=90, y=150)
        self.Entry2 = Entry(win, bd=2)
        self.Entry2.place(x=200, y=150)
        
        self.Label4 = Label(win, text="Result: ", bg="dark green", fg="white", font=("Helvetica", 10, "bold"))
        self.Label4.place(x=90, y=180)
        self.Entry3 = Entry(win, bd=2)
        self.Entry3.place(x=200, y=180)
        
        self.Button1 = Button(win, text="Add", command=self.add, bg="lightblue", fg="black", font=("Helvetica", 10, "bold"))
        self.Button1.place(x=90, y=220)
        
        self.Button2 = Button(win, text="Minus", command=self.sub, bg="lightcoral", fg="black", font=("Helvetica", 10, "bold"))
        self.Button2.place(x=140, y=220)
        
        self.Button3 = Button(win, text="Multiply", command=self.multiply, bg="lightgreen", fg="black", font=("Helvetica", 10, "bold"))
        self.Button3.place(x=200, y=220)
        
        self.Button4 = Button(win, text="Divide", command=self.divide, bg="lightyellow", fg="black", font=("Helvetica", 10, "bold"))
        self.Button4.place(x=275, y=220)

    def add(self):
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result = num1 + num2
        self.Entry3.delete(0, END)  
        self.Entry3.insert(0, str(result))
        
    def sub(self):
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result = num1 - num2
        self.Entry3.delete(0, END)  
        self.Entry3.insert(0, str(result))
        
    def multiply(self):
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result = num1 * num2
        self.Entry3.delete(0, END)  
        self.Entry3.insert(0, str(result))
        
    def divide(self):
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error"
        self.Entry3.delete(0, END)  
        self.Entry3.insert(0, str(result))

window = Tk()
MyWin = MyWindow(window)
window.geometry("400x300+10+10")
window.title("Standard Calculator")
window.mainloop()
