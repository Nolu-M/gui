from tkinter import *
#from PIL import ImageTk, Image

root = Tk()
root.geometry("2500x2667")

# Define image
bg = PhotoImage(file="images/beans.png")

# Create a canvas
my_canvas = Canvas(root, width=2500, height=2667)
my_canvas.pack(fill="both", expand=True)


my_canvas.create_image(-250,0, image=bg, anchor="nw")

my_canvas.create_text(550, 100, text="ArdaCiti Coffee Shop", font=("Segoe Script", 40), anchor="nw")
my_canvas.create_text(700, 200, text="The Best In Town", font=("Segoe Script", 20),  anchor="nw")



button1 = Button(text="Tea", bg="white", fg="black")
button2 = Button(text="Coffee", bg="white", fg="black")
button3 = Button(text="Voice Command", bg="white", fg="black")


button1_window = my_canvas.create_window(300, 200, anchor="nw", window=button1)
button2_window = my_canvas.create_window(300, 250, anchor="nw", window=button2)
button3_window = my_canvas.create_window(300, 300, anchor="nw", window=button3)


















root.mainloop()

'''
def resizer(e):
    global bg1, resized_bg, new_bg
    # Open the image
    bg1 = Image.open("images/beans.png")
    # resize t
    resized_bg = bg1.resize((e.width, e.height), Image.ANTIALIAS)
    # Define image again
    new_bg = ImageTk.PhotoImage(resized_bg)
    # Add it back to the canvas
    my_canvas.create_image(0,0, image=new_bg, anchor="nw")
    # Read the text
    my_canvas.create_text(400, 100, text="ArdaCiti Coffee Shop", font=("Helvetica", 30))
    my_canvas.create_text(400, 150, text="The Best In Town", font=("Helvetica", 15) )



root.bind('<Configure>', resizer)  
'''

