from tkinter import *
from PIL import ImageTk, Image

def open_coffee_options():
    # Hide the main menu buttons
    button1.destroy()
    button2.destroy()
    button3.destroy()
    
    # Create a new frame for coffee options
    coffee_frame = Frame(root)
    coffee_frame.place(relx=0.5, rely=0.5, anchor="center")
    # define images
    coffee_bg = PhotoImage(file="images/c-beans.png")
    # coffee options
    cuppaccino = PhotoImage(file="images/cuppaccino.png").subsample(3)
    expresso = PhotoImage(file="images/expresso.png").subsample(3)
    latte = PhotoImage(file="images/latte.png").subsample(3)
    macch = PhotoImage(file="images/macch.png").subsample(2)
    mocha = PhotoImage(file="images/mocha.png").subsample(3)
    ameri = PhotoImage(file="images/ameri.png").subsample(3)


    # create a canvas
    my_canvas2 = Canvas(coffee_frame, width=1600, height=900)
    my_canvas2.pack(fill="both", expand=True)

    my_canvas2.create_image(0,0, image=coffee_bg, anchor="nw")


    
    # Add background image to the frame
    def resized(e):
        global coffee_bg, resized_coffee_bg, new_coffee_bg
        # Open the image
        coffee_bg = Image.open("images/c-beans.png", )
        # Resize the image
        resized_coffee_bg = coffee_bg.resize((1600, 900), Image.LANCZOS)
        # Define image again
        new_coffee_bg = ImageTk.PhotoImage(resized_coffee_bg)
        # Add it back to the canvas
        my_canvas2.create_image(0,0, image=new_coffee_bg, anchor="nw")
        # Read the text
        my_canvas2.create_text(400, 100, text="ArdaCiti Coffee Shop", font=("Segoe Script", 40))
        my_canvas2.create_text(400, 150, text="The Best In Town", font=("Segoe Script", 20))
        # Add coffee options
        my_canvas2.create_image(50,300, image=cuppaccino, anchor="nw")
        my_canvas2.create_image(300,300, image=expresso, anchor="nw")
        my_canvas2.create_image(600,280, image=latte, anchor="nw")
        my_canvas2.create_image(-20,500, image=macch, anchor="nw")
        my_canvas2.create_image(310,500, image=mocha, anchor="nw")
        my_canvas2.create_image(580,500, image=ameri, anchor="nw")


    root.bind('<Configure>', resized)

def open_tea_options():
    # Hide the main menu buttons
    button1.destroy()
    button2.destroy()
    button3.destroy()
    
    # Create a new frame for coffee options
    tea_frame = Frame(root)
    tea_frame.place(relx=0.5, rely=0.5, anchor="center")
    # define images
    tea_bg = PhotoImage(file="images/tea.png")
    rooibos = PhotoImage(file="images/rooibos.png")
    peppermint = PhotoImage(file="images/peppermint.png")
    greantea = PhotoImage(file="images/greentea.png")
    cinnamon = PhotoImage(file="images/cinnamon.png")
    chamomile = PhotoImage(file="images/chamomile.png")
    ceylon = PhotoImage(file="images/ceylon.png")
    # create a canvas
    my_canvas3 = Canvas(tea_frame, width=1600, height=900)
    my_canvas3.pack(fill="both", expand=True)

    my_canvas3.create_image(0,0, image=tea_bg, anchor="nw")
    
    # Add background image to the frame
    def resized(e):
        global tea_bg, resized_tea_bg, new_tea_bg
        # Open the image
        tea_bg = Image.open("images/tea.png")
        # Resize the image
        resized_tea_bg = tea_bg.resize((1600, 900), Image.LANCZOS)
        # Define image again
        new_tea_bg = ImageTk.PhotoImage(resized_tea_bg)
        # Add it back to the canvas
        my_canvas3.create_image(0,0, image=new_tea_bg, anchor="nw")
        # Read the text
        my_canvas3.create_text(400, 100, text="ArdaCiti Coffee Shop", font=("Segoe Script", 40))
        my_canvas3.create_text(400, 150, text="The Best In Town", font=("Segoe Script", 20))
        # Add images
        my_canvas3.create_image(0,0, image=rooibos, anchor="nw")
        my_canvas3.create_image(400,0, image=peppermint, anchor="nw")
        my_canvas3.create_image(800,0, image=greantea, anchor="nw")
        my_canvas3.create_image(0,200, image=cinnamon, anchor="nw")
        my_canvas3.create_image(400,200, image=chamomile, anchor="nw")
        my_canvas3.create_image(800,200, image=ceylon, anchor="nw")
    root.bind('<Configure>', resized)






root = Tk()
root.geometry("1600x900")

# Define image
bg = PhotoImage(file="images/c-beans.png")

# Create a canvas
my_canvas = Canvas(root, width=740, height=538)
my_canvas.pack(fill="both", expand=True)


my_canvas.create_image(0,0, image=bg, anchor="nw")

button1 = Button(text="Tea", bg="#8B3E2F", fg="white", pady=10, padx=30, command=open_tea_options)
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
    resized_bg = bg1.resize((1600, 900), Image.LANCZOS)
    # Define image again
    new_bg = ImageTk.PhotoImage(resized_bg)
    # Add it back to the canvas
    my_canvas.create_image(0,0, image=new_bg, anchor="nw")
    # Read the text
    my_canvas.create_text(400, 100, text="ArdaCiti Coffee Shop", font=("Segoe Script", 40))
    my_canvas.create_text(400, 150, text="The Best In Town", font=("Segoe Script", 20) )
root.bind('<Configure>', resizer)  


root.mainloop()

