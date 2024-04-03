from tkinter import *
from PIL import ImageTk, Image

def open_coffee_options():
    # Hide the main menu buttons
    button1.destroy()
    button2.destroy()
    button3.destroy()
    
    # Create a new frame for coffee options
    coffee_frame = Frame(root, bg="white")
    coffee_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
    
    # Add background image to the frame
    coffee_bg = Image.open("images/coffee_options.jpeg")
    coffee_bg = coffee_bg.resize((1480, 876), Image.LANCZOS)
    coffee_bg = ImageTk.PhotoImage(coffee_bg)
    bg_label = Label(coffee_frame, image=coffee_bg)
    bg_label.image = coffee_bg  # Keep a reference to avoid garbage collection
    bg_label.pack(fill="both", expand=True)

    text_label = Label(coffee_frame, text="ArdaCiti Coffee Shop", font=("Segoe Script", 40))
    text_label.pack(pady=20)
    #my_canvas.create_text(400, 150, text="The Best In Town", font=("Segoe Script", 20) )





root = Tk()
root.geometry("1480x1076")

# Define image
bg = PhotoImage(file="images/c-beans.png")

# Create a canvas
my_canvas = Canvas(root, width=740, height=538)
my_canvas.pack(fill="both", expand=True)


my_canvas.create_image(0,0, image=bg, anchor="nw")

button1 = Button(text="Tea", bg="#8B3E2F", fg="white", pady=10, padx=30)
button2 = Button(text="Coffee", bg="#8B3E2F", fg="white", pady=10, padx=30, command=open_coffee_options)
button3 = Button(text="Voice Command", bg="#8B3E2F", fg="white", pady=10, padx=30)


button1_window = my_canvas.create_window(200, 400, anchor="nw", window=button1)
button2_window = my_canvas.create_window(300, 400, anchor="nw", window=button2)
button3_window = my_canvas.create_window(420, 400, anchor="nw", window=button3)

def resizer(e):
    global bg1, resized_bg, new_bg
    # Open the image
    bg1 = Image.open("images/c-beans.png")
    # resize the image
    resized_bg = bg1.resize((1480, 876), Image.LANCZOS)
    # Define image again
    new_bg = ImageTk.PhotoImage(resized_bg)
    # Add it back to the canvas
    my_canvas.create_image(0,0, image=new_bg, anchor="nw")
    # Read the text
    my_canvas.create_text(400, 100, text="ArdaCiti Coffee Shop", font=("Segoe Script", 40))
    my_canvas.create_text(400, 150, text="The Best In Town", font=("Segoe Script", 20) )

root.bind('<Configure>', resizer)  


root.mainloop()

