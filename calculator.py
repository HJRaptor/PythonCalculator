import tkinter as tk
from PIL import ImageTk

calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_results.delete(1.0,"end")
    text_results.insert(1.0,calculation)




def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_results.delete(1.0,"end")
        text_results.insert(1.0,calculation)

    except:
        clear_field()
        text_results.insert(1.0,"Error")
        pass

def clear_field():
    global calculation
    calculation = ""
    text_results.delete(1.0,"end")

def delete():
    global calculation
    calculation = calculation[:-1]
    text_results.delete("end-2c", "end-1c")


root = tk.Tk()
root.geometry("320x420")
text_results = tk.Text(root, height=1, width=16, font=("Arial",24))
text_results.grid(columnspan=5)
#number keys
btn1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1), width=5, font=("Arial",14))
btn1.grid(row=4, column=1)
btn2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2), width=5, font=("Arial",14))
btn2.grid(row=4, column=2)
btn3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3), width=5, font=("Arial",14))
btn3.grid(row=4, column=3)
btn4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4), width=5, font=("Arial",14))
btn4.grid(row=3, column=1)
btn5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5), width=5, font=("Arial",14))
btn5.grid(row=3, column=2)
btn6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6), width=5, font=("Arial",14))
btn6.grid(row=3, column=3)
btn7 = tk.Button(root, text="7", command=lambda: add_to_calculation(7), width=5, font=("Arial",14))
btn7.grid(row=2, column=1)
btn8 = tk.Button(root, text="8", command=lambda: add_to_calculation(8), width=5, font=("Arial",14))
btn8.grid(row=2, column=2)
btn9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9), width=5, font=("Arial",14))
btn9.grid(row=2, column=3)
btn0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), width=12, font=("Arial",14))
btn0.grid(row=6,column=1,columnspan=2   )

#functions
btndel = tk.Button(root, text="del", command=delete ,width=5, font=("Arial",14))
btndel.grid(row=6, column=3)

btnadd = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), font=("Arial", 14))


# Load the image and set it to the button
add = ImageTk.PhotoImage(file="Untitled.png")


btnadd.config(image=add)

# Use grid layout manager to place the button
btnadd.grid(row=2, column=4)


btnminus = tk.Button(root, text="-", command=lambda: add_to_calculation("-"),  font=("Arial",14))
btnminus.grid(row=3, column=4)
minus = ImageTk.PhotoImage(file="minus.png")
btnminus.config(image=minus)



btnmultiply = tk.Button(root, text="*", command=lambda: add_to_calculation("*"), font=("Arial",14))
btnmultiply.grid(row=4, column=4)
multi = ImageTk.PhotoImage(file="multiply.png")
btnmultiply.config(image=multi)


btndivide = tk.Button(root, text="/", command=lambda: add_to_calculation("/"),  font=("Arial",14))
btndivide.grid(row=6, column=4)
divide = ImageTk.PhotoImage(file="divide.png")
btndivide.config(image=divide)

btnresult = tk.Button(root, text="=", command=evaluate_calculation, width=18, font=("Arial",14))
btnresult.grid(row=7, column=1, columnspan=3)

btnclear = tk.Button(root, text="clear", command= clear_field, width=5, font=("Arial",14))
btnclear.grid(row=7, column=4)



root.mainloop()
