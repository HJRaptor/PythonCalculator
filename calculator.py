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
root.geometry("290x375")
text_results = tk.Text(root, height=1, width=16, font=("Consolas",24))
text_results.grid(columnspan=5,sticky='nesw')
#number keys
btn1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1), font=("Consolas",14), bg="white",highlightthickness = 5, bd = 0)
btn1.grid(row=4, column=1,sticky='nesw')
btn2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2), width=5, font=("Consolas",14), bg="white",highlightthickness = 5, bd = 0)
btn2.grid(row=4, column=2,sticky='nesw')
btn3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3), width=5, font=("Consolas",14), bg="white",highlightthickness = 5, bd = 0)
btn3.grid(row=4, column=3,sticky='nesw')
btn4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4), width=5, font=("Consolas",14), bg="white",highlightthickness = 5, bd = 0)
btn4.grid(row=3, column=1,sticky='nesw')
btn5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5), width=5, font=("Consolas",14), bg="white",highlightthickness = 5, bd = 0)
btn5.grid(row=3, column=2,sticky='nesw')
btn6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6), width=5, font=("Consolas",14), bg="white",highlightthickness = 5, bd = 0)
btn6.grid(row=3, column=3,sticky='nesw')
btn7 = tk.Button(root, text="7", command=lambda: add_to_calculation(7), width=5, font=("Consolas",14), bg="white",highlightthickness = 5, bd = 0)
btn7.grid(row=2, column=1,sticky='nesw')
btn8 = tk.Button(root, text="8", command=lambda: add_to_calculation(8), width=5, font=("Consolas",14), bg="white",highlightthickness = 5, bd = 0)
btn8.grid(row=2, column=2,sticky='nesw')
btn9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9), width=5, font=("Consolas",14), bg="white",highlightthickness = 5, bd = 0)
btn9.grid(row=2, column=3,sticky='nesw')
btn0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), width=12, font=("Consolas",14), bg="white",highlightthickness = 5, bd = 0)
btn0.grid(row=6,column=1,columnspan=2,sticky='nesw')

#functions
btndel = tk.Button(root, text="del", command=delete ,width=5, font=("Consolas",14), bg="white",highlightthickness =0, bd = 0)
btndel.grid(row=6, column=3,sticky='nesw')

btnadd = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), font=("Consolas", 14), highlightthickness = 0, bd = 0)


# Load the image and set it to the button
add = ImageTk.PhotoImage(file="Untitled.png")


btnadd.config(image=add)

# Use grid layout manager to place the button
btnadd.grid(row=2, column=4,sticky='nesw')


btnminus = tk.Button(root, text="-", command=lambda: add_to_calculation("-"),  font=("Consolas",14),highlightthickness = 0, bd = 0)
btnminus.grid(row=3, column=4,sticky='nesw')
minus = ImageTk.PhotoImage(file="minus.png")
btnminus.config(image=minus)



btnmultiply = tk.Button(root, text="*", command=lambda: add_to_calculation("*"), font=("Consolas",14),highlightthickness = 0, bd = 0)
btnmultiply.grid(row=4, column=4,sticky='nesw')
multi = ImageTk.PhotoImage(file="multiply.png")
btnmultiply.config(image=multi)


btndivide = tk.Button(root, text="/", command=lambda: add_to_calculation("/"),  font=("Consolas",14),highlightthickness = 0, bd = 0)
btndivide.grid(row=6, column=4,sticky='nesw')
divide = ImageTk.PhotoImage(file="divide.png")
btndivide.config(image=divide)

btnresult = tk.Button(root, text="=", command=evaluate_calculation,  font=("Consolas",14), bg="white",highlightthickness = 0, bd = 0)
btnresult.grid(row=7, column=1,columnspan=2,sticky='nesw')

btndecimal = tk.Button(root, text=".", command=lambda: add_to_calculation("."), font=("Consolas",14), bg="white",highlightthickness = 0, bd = 0)
btndecimal.grid(row=7, column=3,sticky='nesw')

btnclear = tk.Button(root, text="clear", command= clear_field, font=("Consolas",14), bg="white",highlightthickness = 0, bd = 0)
btnclear.grid(row=7, column=4,sticky='nesw')



root.mainloop()
