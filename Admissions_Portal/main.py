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


def id_number():
    # generates a random number as the id number of the student just in case they have same names with the other person
    # assuming that not no more than 5000 students will apply
    return str(random.randint(1000, 5000))

def account_login():
    id_num = ''
    email_address = ''
    full_name = ''

    log_in = input('Do you have an account (yes/no): ')
    if log_in == 'yes':
        id_num = input('Enter your ID number: ')
        if id_num in profile.keys():
            print(f'Welcome back, {profile[id_num][0]}')
            # application_stage()
        else:
            print('ID number not found. Please create an account')
            full_name = input('Enter your full name: ')
            email_address = input('Enter your email address: ')
            id_num = id_number()
            print(f'Your ID Number is {id_num},Please always remember your ID number.')
            print(f'Welcome {full_name} to Leather VIII Admissions Portal, your account has been created.')
            # application_stage()
    else:
        full_name = input('Enter your full name: ')
        email_address = input('Enter your email address: ')
        id_num = id_number()
        print(f'Your ID Number is {id_num},Please always remember your ID number')
        print(f'Welcome {full_name} to Leather VIII Admissions Portal, your account has been created')

    profile[id_num] = [full_name, email_address]
    return id_num
def load_from_file():
    try:
        fout = open('admission_management.txt', 'r')

        for line in fout:
            entries = line.strip().split(";")
            stages = 0

            identification_number = 0
            for individual_data in entries:
                individual_data = individual_data.split(',')
                if stages == 0:
                    identification_number = individual_data[2]
                    profile[identification_number] = [individual_data[0], individual_data[1], individual_data[3],
                                                      individual_data[4], individual_data[5], individual_data[6]]
                elif stages == 1:
                    contact[identification_number] = individual_data
                elif stages == 2:
                    education[identification_number] = individual_data
                elif stages == 3:
                    personal_essay[identification_number] = individual_data
                elif stages == 4:
                    activities[identification_number] = individual_data

                stages += 1
        fout.close()
    except FileNotFoundError:
        open('admission_management.txt', 'x')


def save_to_file(profile, contact, education, essay, activities):
    fin=None

    try:
        fin = open('students_admissions.txt', "w")
        print('file opened')

    except IOError:
        print("Error creating file")
    except:
        print("File does not exist")

    for id_number, elements in profile.items():
        '''
            profile={
                71972027=[yoofi setsie
            }
        '''
        # Create a list of parts for this ID number.
        # Adds the profile information.
        add = ",".join(elements)
        parts = [f"{add}"]

        # Add the contact information.
        add = ",".join(contact[id_number])
        parts.append(f"{add}")

        # Add the education information.
        add = ",".join(education[id_number])
        parts.append(f"{add}")

        # Add the essay information.
        parts.append(f"{essay[id_number]}")

        # Add the activities information
        add = ",".join(activities[id_number])
        parts.append(f"{add}")

        # Join the parts with semicolons and write them to the file followed by a newline character.
        fin.write(";".join(parts) + "\n")

    fin.close()


# print(profile)
# print(contact)
# print(education)
# print(essay)
# print(activities)

entries = [profile,
           contact,
           education,
           personal_essay,
           activities]


def application_stage(user_id):
    # id_num = id_number()
    # identification = {full_name: id_number}

    while True:
        print('1. Profile')
        print('2. Contact details ')
        print('3. Education ')
        print('4. Personal Essay and Activities')
        print('5. Creativity activity')
        print('6.Decision')
        print('7.Exit')
        application_stage = int(input('Enter the stage(1-6): '))

        if application_stage == 1:
            print('PROFILE\n')

            dob = input('Enter your date of birth(eg. 30/03/2020): ')
            gender = input('Enter your gender(male/female): ')
            nationality = input('Enter your nationality: ')

            profile[user_id].extend([dob, gender, nationality])

        elif application_stage == 2:
            # full_name = input('Enter your full name')
            print('CONTACT DETAILS')
            email_address = input('Enter your email address: ')
            phone_number = input('Enter your phone number:')

            print('\nFAMILY')
            print('i. PARENT 1: ')
            name_of_parent1 = input(('Enter the name of your parent: '))
            relation1 = input('Enter your relation with parent1: ')
            parent_phone_number1 = input('Enter phone number: ')

            print('\nii. PARENT 2')
            name_of_parent2 = input(('Enter the name of your parent: '))
            relation2 = input('Enter your relation with parent1: ')
            parent_phone_number2 = input('Enter phone number: ')

            contact[user_id] = [email_address, phone_number, name_of_parent1, relation1, parent_phone_number1,
                                  name_of_parent2,
                                  relation2, parent_phone_number2]


        elif application_stage == 3:
            print('Education: ')
            educational_institution = input('Enter your recent high school: ')
            level = input('Enter level of education: ')

            print('EXAMINATION: ')
            board = input('Enter examination board: ')
            math_grade = input('Enter grade for math: ')
            eng_grade = input('Enter grade for English language: ')
            art_grade = input('Enter the grade for art: ')

            education[user_id] = [educational_institution, level, board, math_grade, eng_grade, art_grade]

        elif application_stage == 4:
            attempts = 5
            print('PERSONAL ESSAY AND ACTIVITIES')
            essay = input('Paste your personal essay that is between 100 to 200 words: ')
            personal_essay[user_id] = essay
            while attempts >= 0:
                activity = input('Enter the activities you have been part of: ')
                if activity == 'quit':
                    break
                if attempts == 5:
                    activities[user_id] = [activity]
                else:
                    activities[user_id].append(activity)

                attempts -= 1

        elif application_stage == 5:
            print('CREATIVITY ACTIVITY')
            print(
                'Leather VIII Institute of Creativity focuses more on your creativity and problem solving skills. Below is an image that you need to show these skills by filtering. ')
        # image to filter
        elif application_stage == 6:
            print('APPLICATION DECISION')
        elif application_stage == 7:
            print('Bye!!see you next time')
            break


user_id = account_login()
application_stage(user_id)
save_to_file(profile, contact, education, personal_essay, activities)
