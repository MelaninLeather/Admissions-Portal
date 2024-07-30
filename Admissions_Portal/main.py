#data from text file
import random
def id_number():
    #generates a random number as the id number of the student just in case they have same names with the other person
    #assuming that not no more than 5000 students will apply
    return random.randint(1,5000)


data={}
file_name="students_admissions.txt"

def load_data_from_file():
    try:
        first=open(file_name,"r")
        #loops every line to check if the name is there
        for line in first:
            #Name;email_address,password

            id_number=id_number()
            details = line.strip().split(",")
            #Get student name
            student_name=details[0]+id_number
            #creates a dictionary of the profile

            profile_dict={}
            for i in details[1:0]:



    except FileNotFoundError:
        print("File not found")
def check_student_name():


def save_to_file(data):






def account_login():
    name_of_student=input("Name of student: ")

