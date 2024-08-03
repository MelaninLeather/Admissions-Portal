import tkinter as tk
from PIL import Image, ImageTk

# initializing the main window
root = tk.Tk()
app_height = 600
app_width = 400

#makingtheloginpopupwindowfunction
def login_popup():
    login_window = tk.Toplevel(root)
    login_window.title("Login!")
    login_window.geometry("400x400")

    login_window.mainloop()
def signup_popup():
    login_window = tk.Toplevel(root)
    login_window.title("SignUp!")
    login_window.geometry("400x400")

    login_window.mainloop()

# defining the title, and size of the  window
root.title('Admission Portal')
root.geometry(f"{app_width}x{app_height}")

# giving the app a white background.
background = tk.Label(root,height=app_height,width=app_width,bg='white')
background.pack()

# adding the image to the screen
icon = Image.open('LEATHER vIII INSTITUTE OF CREATIVITY.png')
resized_icon = icon.resize((270, 270))
converted_icon = ImageTk.PhotoImage(resized_icon)

icon_label = tk.Label(root, image=converted_icon, height=250, width=200)
icon_label.place(x=100, y=50)

# Making the buttons for signup and login
login_btn = tk.Button(root, text="Log In", font=('Arial', 18),command=login_popup)
login_btn.place(x=100, y=320, height=50, width=200)

signup_btn = tk.Button(root, text="Sign Up", font=('Arial', 18),command=signup_popup)
signup_btn.place(x=100, y=400, height=50, width=200)

root.mainloop()
