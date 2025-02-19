import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import data

user = data.Data()

user.load_from_file('students_admissions.txt')


class Application(tk.Tk):
    def __init__(self, a_width, a_height):
        tk.Tk.__init__(self)
        self.a_width = a_width
        self.a_height = a_height

        self.title('Admissions Portal')
        self.resizable(False, False)
        self.geometry(f"{a_width}x{a_height}")

        self.id_num = 0

        # knowing which section/stage to go to. homescreen is stage =1 results is last stage
        self.stage = 0

        self.homescreen = tk.Frame(self, bg='white')

        self.homescreen.pack(fill='both')
        self.homescreen.configure(width=a_width, height=a_height)

        self.icon = Image.open('LEATHER vIII INSTITUTE OF CREATIVITY.png')
        self.resized_icon = self.icon.resize((270, 270))
        self.converted_icon = ImageTk.PhotoImage(self.resized_icon)

        self.icon_label = tk.Label(self.homescreen, image=self.converted_icon, height=250, width=200)
        self.icon_label.place(x=100, y=50)

        # Making the buttons for signup and login
        self.login_btn = tk.Button(self.homescreen, text="Log In", font=('Arial', 18), command=self.login)
        self.login_btn.place(x=100, y=320, height=50, width=200)

        signup_btn = tk.Button(self.homescreen, text="Sign Up", font=('Arial', 18), command=self.signup)
        signup_btn.place(x=100, y=400, height=50, width=200)

        self.mainloop()

    # function for confirming if the user already has an account
    def confirm_login(self):
        # Taking the user input
        self.id_num = self.id_entry.get()

        # comparing with the profile dictionary from the data file
        if self.id_num in user.profile.keys():
            self.homescreen.destroy()
            messagebox.showinfo('Welcome!',
                                f"Welcome back, {user.profile[self.id_num][1]}\nLet's continue from where you left off!")
            self.login_window.destroy()

            if len(user.activities) > 0:
                self.stage = 6
            elif len(user.personal_essay) > 0:
                self.stage = 5
            elif len(user.education) > 0:
                self.stage = 4
            elif len(user.contact) > 0:
                self.stage = 3
            elif self.id_num in user.profile.keys():
                if len(user.profile[self.id_num]) < 4:
                    self.stage = 1
                else:
                    self.stage = 2
            self.switch_stage()
        else:
            messagebox.showinfo('Error!', 'Please enter a valid ID or create a new account')

    # function for processing the data obtained from signup
    def confirm_signup(self):
        # setting a condition to make sure the data with the already existing mail is not added to the database
        skip = False
        # Before anything prompt the user to take not of his/her id number
        messagebox.showwarning('Notice', "Your id number is crutial for the entire admission process."
                                         "\n Please take note of it")

        # Taking all the fullname, input and ID from the signup process.
        self.fullname = self.fullname_entry.get()
        self.email_address = self.email_address_entry.get()
        self.id_num = self.new_id_num

        # checking if the email address already exists
        for line in user.profile.values():
            if self.email_address in line:
                skip = True

        if skip == False:
            # Persisting the data

            # writing the data to a dictionary data framework
            user.profile[self.id_num] = [self.fullname, self.email_address]
            print(user.profile)
            # writing it to a file
            user.save_to_file('students_admissions.txt', category='profile')

            # displaying the process was successful
            messagebox.showinfo('welcome', f'Welcome {self.fullname} to Leather VIII Admissions Portal. '
                                           f'Your account has been created')
            self.signup_window.destroy()
            self.homescreen.destroy()

            # Moving unto the profile stage
            self.stage = 1
            self.switch_stage()
        else:
            messagebox.showerror('Error', 'This email already exists. '
                                          'Use another email address or login')

    def login(self):
        # initializing and configuring the login window
        self.login_window = tk.Toplevel(self)
        self.login_window.title("Login!")
        self.login_window.geometry("200x200")

        # User entry slot for their identification number
        self.id_label = tk.Label(self.login_window, text="Enter your ID:", font=('Arial', 11))
        self.id_label.pack(pady=20)
        self.id_entry = tk.Entry(self.login_window)
        self.id_entry.pack()

        # signup button
        submit_button = tk.Button(self.login_window, text='Login', font=('Arial', 18), command=self.confirm_login)
        submit_button.pack(side='bottom', pady=20)

        self.login_window.mainloop()

    def signup(self):
        # initializing and configuring the window
        self.signup_window = tk.Toplevel(self)
        self.signup_window.title("SignUp!")
        self.signup_window.geometry("400x400")

        # generating the id number for the new applicant
        self.new_id_num = user.generate_id_number()
        # displaying that id number
        self.display_id_num = tk.Label(self.signup_window, text=f'Your ID: {self.new_id_num}', font=('Arial', 12))
        self.display_id_num.pack(pady=20)

        # User Entry for their full name (Both label and input box)
        self.fullname_label = tk.Label(self.signup_window, text='Enter your full name: ', font=('Arial', 12))
        self.fullname_label.pack(pady=20, padx=20)
        self.fullname_entry = tk.Entry(self.signup_window)
        self.fullname_entry.pack(pady=20, padx=20)

        # User Entry for their email address (Both label and input box)
        self.email_address_label = tk.Label(self.signup_window, text='Enter your email address: ', font=('Arial', 12))
        self.email_address_label.pack(pady=20, padx=20)
        self.email_address_entry = tk.Entry(self.signup_window)
        self.email_address_entry.pack(pady=20, padx=20)

        # Signup submit button
        self.signup_button = tk.Button(self.signup_window, text='Sign Up', font=('Arial', 18),
                                       command=self.confirm_signup)
        self.signup_button.pack(side='bottom', pady=20)

        self.signup_window.mainloop()

    def profile_stage(self):
        # making the background
        self.bg = tk.Label(self, bg='white', width=500, height=700)
        self.bg.place(x=0, y=0)

        # making the content
        self.profile_frame = tk.Frame(self, bg='white')
        self.profile_frame.pack(fill='both')

        # putting the information and user entry on the app
        self.profile_heading = tk.Label(self.profile_frame, text="Profile", font=('Arial', 18), bg='white')
        self.profile_heading.pack(pady=20, fill='y')
        self.dob_label = tk.Label(self.profile_frame, text='Enter your date of birth(eg. 30/03/2020): ',
                                  font=('Arial', 12), bg='white')
        self.dob_label.pack(pady=20)
        self.dob_entry = tk.Entry(self.profile_frame)
        self.dob_entry.pack(pady=20)

        self.gender_label = tk.Label(self.profile_frame, text='Enter your gender(male/female): ', font=('Arial', 12),
                                     bg='white')
        self.gender_label.pack(pady=20)
        self.gender_entry = tk.Entry(self.profile_frame)
        self.gender_entry.pack(pady=20)

        self.nationality_label = tk.Label(self.profile_frame, text='Enter your nationality: ', font=('Arial', 12),
                                          bg='white')
        self.nationality_label.pack(pady=20)
        self.nationality_entry = tk.Entry(self.profile_frame)
        self.nationality_entry.pack(pady=20)

        # Now to the buttons
        self.button_frame = tk.Frame(self, bg='white')
        self.button_frame.pack(side='bottom')
        self.next_button = tk.Button(self.button_frame, text='Continue', font=('Arial', 11), command=self.move_on)
        self.next_button.pack(side='left', padx=30, pady=50, fill='x')
        self.quit_button = tk.Button(self.button_frame, text='Save and Logout', font=('Arial', 11),
                                     command=self.log_out)
        self.quit_button.pack(side='left', padx=30, pady=50, fill='x', anchor='e')

    def contact_stage(self):

        # making the background
        self.bg = tk.Label(self, bg='white', width=500, height=700)
        self.bg.place(x=0, y=0)

        # making the content
        self.contact_frame = tk.Frame(self, bg='white')
        self.contact_frame.pack(fill='both')

        self.heading_1 = tk.Label(self.contact_frame, text='CONTACT DETAILS', font=('Arial', 16), bg='white')
        self.heading_1.pack(pady=20)

        self.phone_number_label = tk.Label(self.contact_frame, text='Enter your phone number:', font=('Arial', 11),
                                           bg='white')
        self.phone_number_label.pack(pady=5)
        self.phone_number_entry = tk.Entry(self.contact_frame)
        self.phone_number_entry.pack(pady=5)

        self.name_of_parent1_label = tk.Label(self.contact_frame, text='Enter the name of your 1st parent: ',
                                              font=('Arial', 11), bg='white')
        self.name_of_parent1_label.pack(pady=5)
        self.name_of_parent1_entry = tk.Entry(self.contact_frame)
        self.name_of_parent1_entry.pack(pady=5)

        self.relation1_label = tk.Label(self.contact_frame, text='Enter your relation with parent 1:',
                                        font=('Arial', 11), bg='white')
        self.relation1_label.pack(pady=5)
        self.relation1_entry = tk.Entry(self.contact_frame)
        self.relation1_entry.pack(pady=5)

        self.parent_phone_number1_label = tk.Label(self.contact_frame, text='Enter phone number: ', font=('Arial', 11),
                                                   bg='white')
        self.parent_phone_number1_label.pack(pady=5)
        self.parent_phone_number1_entry = tk.Entry(self.contact_frame)
        self.parent_phone_number1_entry.pack(pady=5)

        self.name_of_parent2_label = tk.Label(self.contact_frame, text='Enter the name of your 2nd parent: ',
                                              font=('Arial', 11), bg='white')
        self.name_of_parent2_label.pack(pady=5)
        self.name_of_parent2_entry = tk.Entry(self.contact_frame)
        self.name_of_parent2_entry.pack(pady=5)

        self.relation2_label = tk.Label(self.contact_frame, text='Enter your relation with parent 2:',
                                        font=('Arial', 11), bg='white')
        self.relation2_label.pack(pady=5)
        self.relation2_entry = tk.Entry(self.contact_frame)
        self.relation2_entry.pack(pady=5)

        self.parent_phone_number2_label = tk.Label(self.contact_frame, text='Enter phone number: ', font=('Arial', 11),
                                                   bg='white')
        self.parent_phone_number2_label.pack(pady=5)
        self.parent_phone_number2_entry = tk.Entry(self.contact_frame)
        self.parent_phone_number2_entry.pack(pady=5)

        # Now to the buttons
        self.button_frame = tk.Frame(self, bg='white')
        self.button_frame.pack(side='bottom')
        self.next_button = tk.Button(self.button_frame, text='Continue', font=('Arial', 11), command=self.move_on)
        self.next_button.pack(side='left', padx=30, pady=20, fill='x')
        self.quit_button = tk.Button(self.button_frame, text='Save and Logout', font=('Arial', 11),
                                     command=self.log_out)
        self.quit_button.pack(side='left', padx=30, pady=20, fill='x', anchor='e')

    def education_stage(self):
        # making the background
        self.bg = tk.Label(self, bg='white', width=500, height=700)
        self.bg.place(x=0, y=0)

        # making the content
        self.education_frame = tk.Frame(self, bg='white')
        self.education_frame.pack(fill='both')

        self.heading_1 = tk.Label(self.education_frame, text='EDUCATION', font=('Arial', 16), bg='white')
        self.heading_1.pack(pady=7)

        self.educational_institution_label = tk.Label(self.education_frame, text='Enter your recent school completed: ',
                                                      font=('Arial', 11), bg='white')
        self.educational_institution_label.pack(pady=7)
        self.educational_institution_entry = tk.Entry(self.education_frame)
        self.educational_institution_entry.pack(pady=7)

        self.level_label = tk.Label(self.education_frame, text='Enter level of education: ', font=('Arial', 11),
                                    bg='white')
        self.level_label.pack(pady=7)
        self.level_entry = tk.Entry(self.education_frame)
        self.level_entry.pack(pady=7)

        self.heading_1 = tk.Label(self.education_frame, text='EXAMINATION', font=('Arial', 16), bg='white')
        self.heading_1.pack(pady=7)

        self.board_label = tk.Label(self.education_frame, text='Enter examination board: ', font=('Arial', 11),
                                    bg='white')
        self.board_label.pack(pady=7)
        self.board_entry = tk.Entry(self.education_frame)
        self.board_entry.pack(pady=7)

        self.math_grade_label = tk.Label(self.education_frame, text='Enter grade for math: ', font=('Arial', 11),
                                         bg='white')
        self.math_grade_label.pack(pady=7)
        self.math_grade_entry = tk.Entry(self.education_frame)
        self.math_grade_entry.pack(pady=7)

        self.eng_grade_label = tk.Label(self.education_frame, text='Enter grade for English language: ',
                                        font=('Arial', 11), bg='white')
        self.eng_grade_label.pack(pady=7)
        self.eng_grade_entry = tk.Entry(self.education_frame)
        self.eng_grade_entry.pack(pady=7)

        self.art_grade_label = tk.Label(self.education_frame, text='Enter the grade for art: ', font=('Arial', 11),
                                        bg='white')
        self.art_grade_label.pack(pady=7)
        self.art_grade_entry = tk.Entry(self.education_frame)
        self.art_grade_entry.pack(pady=7)

        # Now to the buttons
        self.button_frame = tk.Frame(self, bg='white')
        self.button_frame.pack(side='bottom')
        self.next_button = tk.Button(self.button_frame, text='Continue', font=('Arial', 11), command=self.move_on)
        self.next_button.pack(side='left', padx=30, pady=20, fill='x')
        self.quit_button = tk.Button(self.button_frame, text='Save and Logout', font=('Arial', 11),
                                     command=self.log_out)
        self.quit_button.pack(side='left', padx=30, pady=20, fill='x', anchor='e')

    def personal_essay_stage(self):
        # making the background
        self.bg = tk.Label(self, bg='white', width=500, height=700)
        self.bg.place(x=0, y=0)

        # making the content
        self.essay_frame = tk.Frame(self, bg='white')
        self.essay_frame.pack(fill='both')

        self.heading_1 = tk.Label(self.essay_frame, text='PERSONAL ESSAY', font=('Arial', 16), bg='white')
        self.heading_1.pack(pady=20, fill='y')

        self.essay_label = tk.Label(self.essay_frame,
                                    text='Paste your personal essay that is between 100 to 200 words: ',
                                    font=('Arial', 11), bg='white')
        self.essay_label.pack(pady=20, fill='y')
        self.essay_entry = tk.Entry(self.essay_frame)
        self.essay_entry.pack(pady=20, fill='y')

        # Now to the buttons
        self.button_frame = tk.Frame(self, bg='white')
        self.button_frame.pack(side='bottom')
        self.next_button = tk.Button(self.button_frame, text='Continue', font=('Arial', 11), command=self.move_on)
        self.next_button.pack(side='left', padx=30, pady=50, fill='x')
        self.quit_button = tk.Button(self.button_frame, text='Save and Logout', font=('Arial', 11),
                                     command=self.log_out)
        self.quit_button.pack(side='left', padx=30, pady=50, fill='x', anchor='e')

    def activities_stage(self):
        # making the background
        self.bg = tk.Label(self, bg='white', width=500, height=700)
        self.bg.place(x=0, y=0)

        # making the content
        self.activity_frame = tk.Frame(self, bg='white')
        self.activity_frame.pack(fill='both')

        self.heading_1 = tk.Label(self.activity_frame, text='ACTIVITIES', font=('Arial', 16),
                                  bg='white')
        self.heading_1.pack(pady=20, fill='y')

        self.activity_label = tk.Label(self.activity_frame,
                                       text='Enter the activities you have been part of (at most 5):',
                                       font=('Arial', 11), bg='white')
        self.activity_label.pack(pady=20)

        self.activity_entry1 = tk.Entry(self.activity_frame)
        self.activity_entry1.pack(pady=20)
        self.activity_entry2 = tk.Entry(self.activity_frame)
        self.activity_entry2.pack(pady=20)
        self.activity_entry3 = tk.Entry(self.activity_frame)
        self.activity_entry3.pack(pady=20)
        self.activity_entry4 = tk.Entry(self.activity_frame)
        self.activity_entry4.pack(pady=20)
        self.activity_entry5 = tk.Entry(self.activity_frame)
        self.activity_entry5.pack(pady=20)

        # Now to the buttons
        self.button_frame = tk.Frame(self, bg='white')
        self.button_frame.pack(side='bottom')
        self.next_button = tk.Button(self.button_frame, text='Continue', font=('Arial', 11), command=self.move_on)
        self.next_button.pack(side='left', padx=30, pady=50, fill='x')
        self.quit_button = tk.Button(self.button_frame, text='Save and Logout', font=('Arial', 11),
                                     command=self.log_out)
        self.quit_button.pack(side='left', padx=30, pady=50, fill='x', anchor='e')

    def results_stage(self):
        self.bg = tk.Label(self, bg='white', width=500, height=700)
        self.bg.place(x=0, y=0)

        self.label_1 = tk.Label(self,text='Details',font=('Arial', 11), bg='white')
        self.label_1.pack(pady=7)

        self.label_2 = tk.Label(self,text=f'Identification number: {user.profile[self.id_num][0]}',font=('Arial', 11), bg='white')
        self.label_2.pack(anchor='w')
        self.label_3 = tk.Label(self,text=f'Full name: {user.profile[self.id_num][1]}',font=('Arial', 11), bg='white')
        self.label_3.pack(anchor='w')
        self.label_4 = tk.Label(self,text=f'Email: {user.profile[self.id_num][2]}',font=('Arial', 11), bg='white')
        self.label_4.pack(anchor='w')
        self.label_5 = tk.Label(self,text=f'Date of Birth: {user.profile[self.id_num][3]}',font=('Arial', 11), bg='white')
        self.label_5.pack(anchor='w')
        self.label_6 = tk.Label(self,text=f'Gender: {user.profile[self.id_num][4]}',font=('Arial', 11), bg='white')
        self.label_6.pack(anchor='w')
        self.label_6 = tk.Label(self,text=f'Nationality: {user.profile[self.id_num][5]}',font=('Arial', 11), bg='white')
        self.label_6.pack(anchor='w')
        self.label_7 = tk.Label(self,text=f'Phone Number: {user.contact[self.id_num][0]}',font=('Arial', 11), bg='white')
        self.label_7.pack(anchor='w')
        self.label_8 = tk.Label(self,text=f'Name of Parent: {user.contact[self.id_num][1]}',font=('Arial', 11), bg='white')
        self.label_8.pack(anchor='w')
        self.label_9 = tk.Label(self,text=f'Relation : {user.contact[self.id_num][2]}',font=('Arial', 11), bg='white')
        self.label_9.pack(anchor='w')
        self.label_10 = tk.Label(self,text=f'Phone Number of Parent: {user.contact[self.id_num][3]}',font=('Arial', 11), bg='white')
        self.label_10.pack(anchor='w')
        self.label_11 = tk.Label(self,text=f'Name of Parent: {user.contact[self.id_num][4]}',font=('Arial', 11), bg='white')
        self.label_11.pack(anchor='w')
        self.label_12 = tk.Label(self,text=f'Relation: {user.contact[self.id_num][5]}',font=('Arial', 11), bg='white')
        self.label_12.pack(anchor='w')
        self.label_13 = tk.Label(self,text=f'Phone Number of Parent: {user.contact[self.id_num][6]}',font=('Arial', 11), bg='white')
        self.label_13.pack(anchor='w')
        self.label_14 = tk.Label(self,text=f'Past School: {user.education[self.id_num][0]}',font=('Arial', 11), bg='white')
        self.label_14.pack(anchor='w')
        self.label_15 = tk.Label(self,text=f'Level of education: {user.education[self.id_num][1]}',font=('Arial', 11), bg='white')
        self.label_15.pack(anchor='w')
        self.label_16 = tk.Label(self,text=f'Examination Board: {user.education[self.id_num][2]}',font=('Arial', 11), bg='white')
        self.label_16.pack(anchor='w')
        self.label_17 = tk.Label(self,text=f'Mathematics Grade: {user.education[self.id_num][3]}',font=('Arial', 11), bg='white')
        self.label_17.pack(anchor='w')
        self.label_18 = tk.Label(self,text=f'English Grade: {user.education[self.id_num][4]}',font=('Arial', 11), bg='white')
        self.label_18.pack(anchor='w')
        self.label_19 = tk.Label(self,text=f'Art Grade: {user.education[self.id_num][5]}',font=('Arial', 11), bg='white')
        self.label_19.pack(anchor='w')
        self.label_20 = tk.Label(self,text=f'Activities: {user.activities[self.id_num]}',font=('Arial', 11), bg='white')
        self.label_20.pack(anchor='w')







    def process_profile_stage(self):
        self.dob = self.dob_entry.get()
        self.gender = self.gender_entry.get()
        self.nationality = self.nationality_entry.get()

        # putting them into the profile dictionary
        user.profile[self.id_num].append(self.dob)
        user.profile[self.id_num].append(self.gender)
        user.profile[self.id_num].append(self.nationality)

        # saving to file
        user.save_to_file('students_admissions.txt', 'profile')

        self.profile_frame.destroy()
        self.button_frame.destroy()

    def process_contact_stage(self):

        self.phone_number = self.phone_number_entry.get()
        self.name_of_parent1 = self.name_of_parent1_entry.get()
        self.relation1 = self.relation1_entry.get()
        self.parent_phone_number1 = self.parent_phone_number1_entry.get()
        self.name_of_parent2 = self.name_of_parent2_entry.get()
        self.relation2 = self.relation2_entry.get()
        self.parent_phone_number2 = self.parent_phone_number2_entry.get()

        # putting them into the contact dictionary
        user.contact[self.id_num] = [self.phone_number, self.name_of_parent1, self.relation1, self.parent_phone_number1,
                                     self.name_of_parent2, self.relation2, self.parent_phone_number2]

        # saving to file
        user.save_to_file('students_admissions.txt', 'contact')

        self.contact_frame.destroy()
        self.button_frame.destroy()

    def process_education_stage(self):
        self.educational_institution = self.educational_institution_entry.get()
        self.level = self.level_entry.get()
        self.board = self.board_entry.get()
        self.math_grade = self.math_grade_entry.get()
        self.eng_grade = self.eng_grade_entry.get()
        self.art_grade = self.art_grade_entry.get()

        # putting them into the education dictionary
        user.education[self.id_num] = [self.educational_institution, self.level, self.board, self.math_grade,
                                       self.eng_grade, self.art_grade]

        # saving to file
        user.save_to_file('students_admissions.txt', 'education')

        self.education_frame.destroy()
        self.button_frame.destroy()

    def process_essay_stage(self):
        self.essay = self.essay_entry.get()

        # putting them into the education dictionary
        user.personal_essay[self.id_num] = self.essay

        # saving to file
        user.save_to_file('students_admissions.txt', 'essay')

        self.essay_frame.destroy()
        self.button_frame.destroy()

    def process_activity_stage(self):
        self.activity = [self.activity_entry1.get(), self.activity_entry2.get(), self.activity_entry3.get(),
                         self.activity_entry4.get(), self.activity_entry5.get()]

        # putting them into the education dictionary
        user.activities[self.id_num] = self.activity

        # saving to file
        user.save_to_file('students_admissions.txt', 'activities')

        self.activity_frame.destroy()
        self.button_frame.destroy()

    def move_on(self):
        self.process()
        self.stage += 1
        self.switch_stage()

    def move_back(self):
        self.process()
        self.stage -= 1
        self.switch_stage()

    def log_out(self):
        self.process()
        self.stage = 0
        self.switch_stage()

    def switch_stage(self):
        if self.stage == 0:
            self.destroy()
            self.__init__(400, 600)
        elif self.stage == 1:
            self.profile_stage()
        elif self.stage == 2:
            self.contact_stage()
        elif self.stage == 3:
            self.education_stage()
        elif self.stage == 4:
            self.personal_essay_stage()
        elif self.stage == 5:
            self.activities_stage()
        else:
            self.results_stage()

    def process(self):
        if self.stage == 0:
            self.__init__(400, 600)
        elif self.stage == 1:
            self.process_profile_stage()
        elif self.stage == 2:
            self.process_contact_stage()
        elif self.stage == 3:
            self.process_education_stage()
        elif self.stage == 4:
            self.process_essay_stage()
        elif self.stage == 5:
            self.process_activity_stage()
        else:
            self.results_stage()


App = Application(400, 600)
