import tkinter as tk



def addition():
    n1=float(Nmbr1.get()) 
    n2=float(Nmbr2.get()) 
    result.configure(text=str(n1+n2))

def subtraction():
    n1=float(Nmbr1.get()) 
    n2=float(Nmbr2.get()) 
    result.configure(text=str(n1-n2))

def multiplication():
    n1=float(Nmbr1.get()) 
    n2=float(Nmbr2.get()) 
    result.configure(text=str(n1*n2))

def division():
    n1=float(Nmbr1.get()) 
    n2=float(Nmbr2.get()) 
    result.configure(text=str(n1/n2))

screen = tk.Tk()
screen.title('Calculator')
screen.geometry("280x300")


Nmbr1 = tk.Entry(screen, justify="center")
Nmbr1.place(x=70, y=20)

Nmbr2 = tk.Entry(screen, justify="center")
Nmbr2.place(x=70, y=40)

btn1 = tk.Button(screen, text="+", command=addition)
btn1.place(x=70, y=70)

btn2 = tk.Button(screen, text="-", command=subtraction)
btn2.place(x=90, y=70)

btn3 = tk.Button(screen, text="*", command=multiplication)
btn3.place(x=110, y=70)

btn4 = tk.Button(screen, text="/", command=division)
btn4.place(x=130, y=70)

result = tk.Label(screen, text="Result")
result.place(x=70,y=200)

screen.mainloop()