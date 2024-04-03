from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.geometry("1480x1076")

# Define image
bg = PhotoImage(file="images/c-beans.png")

# Create a canvas
my_canvas = Canvas(root, width=740, height=538)
my_canvas.pack(fill="both", expand=True)


my_canvas.create_image(0,0, image=bg, anchor="nw")

#my_canvas.create_text(550, 100, text="ArdaCiti Coffee Shop", font=("Segoe Script", 40), anchor="nw")
#my_canvas.create_text(700, 200, text="The Best In Town", font=("Segoe Script", 20),  anchor="nw")


button1 = Button(text="Tea", bg="#8B3E2F", fg="white", pady=10, padx=30)
button2 = Button(text="Coffee", bg="#8B3E2F", fg="white", pady=10, padx=30)
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

