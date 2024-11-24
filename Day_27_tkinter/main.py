from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="Label", font=("Arial", 24, "bold"))
my_label.pack()

# my_label["text"] = "New Text"
my_label.config(text="New Text")


# Button

def button_clicked():
    my_label.config(text=input.get())
    print("I got clicked")

button = Button(text="Click Me", command=button_clicked)
button.pack()

# Entry
input = Entry(width=20)
input.pack()

window.mainloop()