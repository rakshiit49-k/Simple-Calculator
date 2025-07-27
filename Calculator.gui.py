import tkinter as tk
from tkinter import messagebox

def calculator(a,b,opr):
    if opr==1:
        result=a+b
    elif opr==2:
        result=a-b
    elif opr==3:
        result=a*b
    elif opr==4:
        if b!=0:
            result=a/b
        else:
            return "cannot divide by zero"
    elif opr==5:
        result=(a/b)*100
    elif opr==6:
        result=a**b
    else:
        return "invalid operation!"
    return result

def calculate_from_gui():
    try:
        a= float(entry1.get())
        b= float(entry2.get())
        opr= int(opr_entry.get())

        result= calculator(a,b,opr)

        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Input Error","Please enter valid numbers and operator (1-6)")

#GUI setup

window=tk.Tk()
window.title("Basic Calculator")
window.geometry("450x400")
window.configure(bg="mistyrose")
window.resizable(False, False)

tk.Label(window,text="Enter First Number",
         font=("Arial",10,"bold"),
         fg="blue").pack()
entry1=tk.Entry(window)
entry1.pack(pady=5)

tk.Label(window,text="Enter Second Number",
         font=("Arial",10,"bold"),
         fg="blue").pack()
entry2=tk.Entry(window)
entry2.pack(pady=5)

tk.Label(window,text="ENTER YOUR CHOICE : ",
         font=("Helvetica",12,"bold"),
         fg="blue").pack(pady=10)


tk.Label(window,text="1. for Addition\n2. for Subtraction\n3. for Multiplication\n4. for Division\n5. for Percentage\n6. for Power",
         font=("Arial",10,"bold"),
         fg="green",
         bg="lavender").pack()
opr_entry=tk.Entry(window,
                  width=10)
opr_entry.pack(pady=10)
         

tk.Button(window, text="CALCULATE",font=("Arial",10,"bold"),bg="lightblue",
          command=calculate_from_gui).pack(pady=20)

result_label=tk.Label(window, text="Result: ",
                      font=("Arial",12,"bold"),
                      fg="red")
result_label.pack()

window.mainloop()


