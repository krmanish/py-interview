from tkinter import *


window = Tk()

def submitBtn():
    lbl.configure(text="Submit Button was clicked !!")

def cancelBtn():
    global window
    lbl.configure(text="Cancel Button was clicked !!")
    window.destroy()

window.geometry('800x800')
window.title("Welcome to Programmin world Mahi....")
lbl = Label(window, text="Hello Mahi...", font=("Arial Bold", 30))
 
lbl.grid(column=0, row=0) 
btn = Button(window, text="Submit", command=submitBtn)
btn.grid(column=0, row=1)
btn = Button(window, text="Close", command=cancelBtn)
btn.grid(column=1, row=1)
window.mainloop()
