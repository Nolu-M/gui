from tkinter import *

root = Tk()

# creating a label widget

e = Entry(root, width=50)
e.pack()
e.insert(0, "Enter Your Name: ")

#myLabel1 = Label(root, text="Ardaciti Coffee Shop")
#myLabel2 = Label(root, text="Get the best tea or coffee")

def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()

#def myClick():
    #myLabel = Label(root, text="Look! I clicked a button!")
    #myLabel.pack()




myButton = Button(root, text="Coffee", command=myClick, bg="green", fg="white")

# shoving it onto the screen

myButton.pack()
# myLabel1.grid(row=0, column=0)
# myLabel2.grid(row=1, column=0)


root.mainloop()