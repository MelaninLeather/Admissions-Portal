import random

file_name = "students_admissions.txt"
# intialising for the points the applicant will have
points = 0

# data from text file
profile = {}
contact = {}
education = {}
personal_essay = {}
activities = {}

user_id = ''

class Data():
    def __init__(self):
        #initializing the dictionary data structure frameworks
        self.profile = {}
        self.contact = {}
        self.education = {}
        self.personal_essay = {}
        self.activities = {}

        #initializing the data storing variable for writing to files
        self.parts = []

    def load_from_file(self, file_name):
        try:
            self.fout = open(f'{file_name}', 'r')

            for line in self.fout:
                entries = line.strip().split(";")
                stages = 0

                identification_number = 0
                for individual_data in entries:
                    individual_data = individual_data.split(',')
                    if stages == 0:
                        identification_number = individual_data[0]
                        self.profile[identification_number] = individual_data
                    elif stages == 1:
                        self.contact[identification_number] = individual_data
                    elif stages == 2:
                        self.education[identification_number] = individual_data
                    elif stages == 3:
                        self.personal_essay[identification_number] = individual_data
                    elif stages == 4:
                        self.activities[identification_number] = individual_data

                    stages += 1
            self.fout.close()
            print('data Loaded.')
        except FileNotFoundError:
            open(f'{file_name}.txt', 'x')

    def save_to_file(self, file_name, category):
        self.fin = None

        try:
            self.fin = open(f'{file_name}', "w")
            print('file opened')

        except IOError:
            print("Error creating file")
        except:
            print("File does not exist")

        for id_number in self.profile.keys():
            # Create a list of parts for this ID number. The parts are the different category

            # Adding the profile information
            if category == 'profile':
                #adding the id number to the profile data
                add = ",".join(self.profile[id_number])
                self.parts.append(add)

            # Add the contact information.
            elif category == 'contact':
                self.parts = [','.join(self.profile[id_number])]
                add = ",".join(self.contact[id_number])
                self.parts.append(f"{add}")

            # Add the education information.
            elif category == 'education':
                self.parts = [','.join(self.profile[id_number]),','.join(self.contact[id_number])]
                add = ",".join(self.education[id_number])
                self.parts.append(f"{add}")

            # Add the essay information.
            elif category == 'essay':
                self.parts = [','.join(self.profile[id_number]),','.join(self.contact[id_number]),','.join(self.education[id_number])]
                self.parts.append(f"{self.personal_essay[id_number]}")

            # Add the activities information
            elif category == 'activities':
                self.parts = [','.join(self.profile[id_number]),','.join(self.contact[id_number]),','.join(self.education[id_number]),','.join(self.personal_essay[id_number])]
                add = ",".join(self.activities[id_number])
                self.parts.append(f"{add}")

            # Join the parts with semicolons and write them to the file followed by a newline character.
            self.fin.write(";".join(self.parts) + "\n")
            self.parts=[]

        self.fin.close()
        print('file closed')

    def generate_id_number(self):
        # generates a random number as the id number of the student just in case they have same names with the other person
        # assuming that not no more than 5000 students will apply
        return str(random.randint(1000, 5000))

