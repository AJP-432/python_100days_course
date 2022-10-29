

# Ajlal F. Paracha - Oct 16, 2022

import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="I am a label", font=("Times New Roman", 24, "bold"))
my_label.grid(column=0, row=0)
my_label.config(text="New Text")

# Entry
my_entry = tkinter.Entry()
my_entry.grid(column=3, row=2)

# Button
def button_clicked(): my_label.config(text=my_entry.get())

my_button = tkinter.Button(text="Click Me!", command=button_clicked)
my_button.grid(column=1, row=1)

my_button2 = tkinter.Button(text="Button 2 Here!", command=button_clicked)
my_button2.grid(column=2, row=0)


window.mainloop()
