from tkinter import *
root = Tk()
root.title("Mango Calculator")
icon = PhotoImage(file="C:/Users/abhis/OneDrive/Documents/DEVA/MaC.png")
root.iconphoto(True,icon)
root.resizable(0,0) #makes main window unresizable

e = Entry(root,width = 35, borderwidth = 1) #Entry widget
e.grid(row=0, column = 0,columnspan = 3,padx =10, pady = 10)

global label_1 #Label to display process
label_1 = Label(root)
label_1.grid(row =1, columnspan= 3)

def label(str):
    global previous
    previous = str
    label_1.config(text =str, fg = "blue")


def button_click(number) : #inserts value in entry widget
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current)+ str(number))
    return

def button_clear(): #clears the window
    label("")
    e.delete(0,END)
    return

def button_add(): #stores and the first number
    try :
        first_number = e.get()
        global f_num
        global operation
        operation = '+'
        f_num = int(first_number)
        label(str(first_number)+'+')
        e.delete(0, END)
    except:
        label("First enter a number")


def button_subtract():  #stores and the first number
    try :
        first_number = e.get()
        global f_num
        global operation
        operation = '-'
        f_num = int(first_number)
        label(str(first_number)+'-')
        e.delete(0, END)
    except:
        label("First enter a number")

def button_multiply():  #stores and the first number
    try :
        first_number = e.get()
        global f_num
        global operation
        operation = '*'
        f_num = int(first_number)
        label(str(first_number)+'*')
        e.delete(0, END)
    except:
        label("First enter a number")

def button_divide():  #stores and the first number
    try :
        first_number = e.get()
        global f_num
        global operation
        operation = '/'
        f_num = int(first_number)
        label(str(first_number)+'/')
        e.delete(0, END)
    except:
        label("First enter a number")

def button_equal():  #stores and the second number and performs operation with
    try :           #the first number
        second_number = e.get()
        e.delete(0, END)
        if operation =='+':
            e.insert(0, f_num + int(second_number))
            label(previous + str(second_number))
        elif operation == '-':
            e.insert(0, f_num - int(second_number))
            label(previous + str(second_number))
        elif operation == '*':
            e.insert(0, f_num * int(second_number))
            label(previous + str(second_number))
        else :
            e.insert(0, f_num / int(second_number))
            label(previous + str(second_number))
    except ZeroDivisionError:
        label("Can't divide by zero")

#buttons
button_1=Button(root, text = "1", padx =40, pady = 20, command =lambda: button_click(1))
button_2=Button(root, text = "2", padx =40, pady = 20, command =lambda: button_click(2))
button_3=Button(root, text = "3", padx =40, pady = 20, command =lambda: button_click(3))
button_4=Button(root, text = "4", padx =40, pady = 20, command =lambda: button_click(4))
button_5=Button(root, text = "5", padx =40, pady = 20, command =lambda: button_click(5))
button_6=Button(root, text = "6", padx =40, pady = 20, command =lambda: button_click(6))
button_7=Button(root, text = "7", padx =40, pady = 20, command=lambda: button_click(7))
button_8=Button(root, text = "8", padx =40, pady = 20, command=lambda: button_click(8))
button_9=Button(root, text = "9", padx =40, pady = 20, command=lambda: button_click(9))
button_0=Button(root, text = "0", padx =40, pady = 20, command=lambda: button_click(0))

button_add=Button(root, text = "+", padx =39, pady = 20, command=button_add)
button_subtract=Button(root, text = "-", padx =40, pady = 20, command=button_subtract)
button_multiply=Button(root, text = "*", padx =40, pady = 20, command=button_multiply)
button_divide=Button(root, text = "/", padx =40, pady = 20, command=button_divide)

button_clear=Button(root, text = "Clear", padx =77, pady = 20, command=button_clear)

button_equal=Button(root, text = "=", padx =87, pady = 20, command=button_equal)


#put buttons on the screen
button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)

button_0.grid(row=5,column=0)
button_clear.grid(row = 5, column = 1, columnspan = 2)

button_add.grid(row =6, column =0)
button_equal.grid(row= 6, column =1 , columnspan = 2)

button_subtract.grid(row=7, column =0)
button_multiply.grid(row=7, column=1)
button_divide.grid(row=7, column=2)


root.mainloop()
