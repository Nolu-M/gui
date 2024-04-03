from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.geometry("740x538")



# open image
my_pic = Image.open("images/c-beans.png")

# resize image
resized = my_pic.resize((1480, 876), Image.LANCZOS)

new_pic = ImageTk.PhotoImage(resized)



# image size
my_label = Label(root, image=new_pic)
my_label.pack()

root.mainloop()

'''
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
    my_canvas.create_text(400, 100, text="ArdaCiti Coffee Shop", font=("Helvetica", 30))
    my_canvas.create_text(400, 150, text="The Best In Town", font=("Helvetica", 15) )



root.bind('<Configure>', resizer)  
'''