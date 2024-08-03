import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

''' 
So what I want to do now is put the code in classes or a class that would be able to be implemented in Mel's code
basically her side of the code asks the questions and stores that entry.
So what I have to do now is make the code such that she can pass the code onto the ui face.
So I'll have to create the a function that acts like an input function. then she specifies the type
then I'll arrange it in a packed form so that she can add as many questions per section. All this would have to be in a frame.
So there would be an initalize frame function which would run several input custom-made functions
At the end-of-every-frame-there-would-be-a-submit-button
Now-what-I-have-just-said-is-for-the-input-section
For-the-login-section-that-would-run-initially-but-then-she-would-have-to-run-the-function-that-would-get-the-login-or-signup-details
after clicking submit it would automatically move to the next frame that she is would have made.                       
'''


# forming a class
class FrontEndApp(tk.Tk):
    def __init__(self, a_width, a_height):
        tk.Tk.__init__(self)

        self.a_width = a_width
        self.a_height = a_height

        self.title('Admissions Portal')
        self.resizable(False, False)
        self.geometry(f"{self.a_width}x{self.a_height}")
        self.whereto = 1

        self.homescreen = tk.Frame(self, bg='white')

        self.profile = tk.Frame(self,bg='white')
        self.contact = tk.Frame(self, bg='white')
        self.education = tk.Frame(self,bg='white')
        self.essay = tk.Frame(self, bg='white')
        self.activities = tk.Frame(self,bg='white')



    # def run(self):
    self.homescreen.pack(fill='both')
    self.homescreen.configure(width=self.a_width, height=self.a_height)

    self.icon = Image.open('LEATHER vIII INSTITUTE OF CREATIVITY.png')
    self.resized_icon = self.icon.resize((270, 270))
    self.converted_icon = ImageTk.PhotoImage(self.resized_icon)

    self.icon_label = tk.Label(self.homescreen, image=self.converted_icon, height=250, width=200)
    self.icon_label.place(x=100, y=50)

    # Making the buttons for signup and login
    self.login_btn = tk.Button(self.homescreen, text="Log In", font=('Arial', 18), command=self.login)
    self.login_btn.place(x=100, y=320, height=50, width=200)

    self.signup_btn = tk.Button(self.homescreen, text="Sign Up", font=('Arial', 18), command=self.signup_popup)
    self.signup_btn.place(x=100, y=400, height=50, width=200)

    self.mainloop()

    def login(self):
        self.login_window = tk.Toplevel(self)
        self.login_window.title("Login!")
        self.login_window.geometry("200x200")

        self.id_label = tk.Label(self.login_window,text="Enter your ID:",font=('Arial', 11))
        self.id_label.pack(pady=20)
        self.id_entry = tk.Entry(self.login_window)
        self.id_entry.pack()

        self.submit_button = tk.Button(self.login_window, text='Submit', font=('Arial', 18),command=self.switch_stage)
        self.submit_button.pack(side='bottom', pady=20)

        self.login_window.mainloop()

    def signup_popup(self):
        self.signup_window = tk.Toplevel(self)
        self.signup_window.title("SignUp!")
        self.signup_window.geometry("400x400")

        self.signup_button = tk.Button(self.signup_window, text='Submit', font=('Arial', 18))
        self.signup_button.pack(side='bottom', pady=20)

        self.signup_window.mainloop()
    def profile_stage(self):
        self.profile.pack(fill='both')

        self.submit_button = tk.Button(self, text='Save & Continue', font=('Arial', 18))
        self.submit_button.pack(side='bottom', pady=20)
    def contact_stage(self):
        self.contact.pack(fill='both')

        self.submit_button = tk.Button(self, text='Save & Continue', font=('Arial', 18))
        self.submit_button.pack(side='bottom', pady=20)
    def education_stage(self):
        self.education.pack(fill='both')

        self.submit_button = tk.Button(self, text='Save & Continue', font=('Arial', 18))
        self.submit_button.pack(side='bottom', pady=20)
    def personal_essay_stage(self):
        self.essay.pack(fill='both')

        self.submit_button = tk.Button(self, text='Save & Continue', font=('Arial', 18))
        self.submit_button.pack(side='bottom', pady=20)
    def activities_stage(self):
        self.activities.pack(fill='both')

        self.submit_button = tk.Button(self, text='Save & Continue', font=('Arial', 18))
        self.submit_button.pack(side='bottom', pady=20)

    def entry(self, text, where):
        if where == 2:
            self.stage = self.profile
        elif where == 3:
            self.stage = self.contact
        elif where == 4:
            self.stage = self.education
        elif where == 5:
            self.stage = self.essay
        elif where == 6:
            self.stage = self.activities

        label = tk.Label(self.stage, text=text)
        label.pack(anchor=tk.W, padx=20, pady=20)
        entry = tk.Entry(self.stage)
        entry.pack()

    def switch_stage(self):
        if self.whereto == 1:
            self.data = self.id_entry.get()
            self.login_window.destroy()
            self.homescreen.pack_forget()
            self.profile_stage()
        elif self.whereto == 2:
            self.profile.pack_forget()
            self.contact_stage()
        elif self.whereto == 3:
            self.contact.pack_forget()
            self.education_stage()
        elif self.whereto == 4:
            self.education.pack_forget()
            self.personal_essay_stage()
        elif self.whereto == 5:
            self.essay.pack_forget()
            self.activities_stage()
        elif self.whereto == 6:
            self.activities.pack_forget()



app = FrontEndApp(400, 600)
app.entry("What is your name?", 2)
app.run()
print(app.data)
