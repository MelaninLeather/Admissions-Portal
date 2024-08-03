# def application_stage():
#     print('1. Profile')
#     print('2.Contact details ')
#     print('3. Education ')
#     print('4. Personal Essay and Activities')
#     print('5. Creativity activity')
#     print('6.Decision')
#     application_stage = int(input('Enter the stage(1-6): '))
#     if application_stage == 1:
#         print('PROFILE\n')
#
#         full_name = input('Enter your full name(eg Melanie Chitehwe): ')
#         dob = input('Enter your date of birth(eg. 30/03/2020): ')
#         gender = input('Enter your gender(male/female)')
#         nationality = input('Enter your nationality')
#     elif application_stage == 2:
#         print('CONTACT DETAILS')
#         email_address = input('Enter your email address: ')
#         phone_number = int(input('Enter your phone number: \n'))
#
#         print('FAMILY')
#         print('i. PARENT 1: ')
#         name_of_parent = input(('Enter the name of your parent: '))
#         relation = input('Enter your relation with parent1: ')
#         phone_number = int(input('Enter phone number: \n'))
#
#         print('ii. PARENT 2')
#         name_of_parent = input(('Enter the name of your parent: '))
#         relation = input('Enter your relation with parent1: ')
#         phone_number = int(input('Enter phone number: \n'))
#
#     elif application_stage == 3:
#         print('Education: ')
#         high_school = input('Enter your recent high school: ')
#         level = input('Enter level of education: ')
#         print('EXAMINATION: ')
#         board = input('Enter examination board: ')
#         math_grade = input('Enter grade for math: ')
#         eng_grade = input('Enter grade for English language: ')
#         art_grade = input('Enter the grade for art: ')
#     elif application_stage == 4:
#         attempts = 5
#         print('PERSONAL ESSAY AND ACTIVITIES')
#         essay = input('Paste your personal essay that is between 100 to 200 words: ')
#         while attempts <= 0:
#             activities = input('Enter the activities you have been part of: ')
#             attempts -= 1
#     elif application_stage == 5:
#         print('CREATIVITY ACTIVITY')
#         print(
#             'Leather VIII Institute of Creativity focuses more on your creativity and problem solving skills. Below is an image that you need to show these skills by filtering. ')
#     # image to filter
#     elif application_stage == 6:
#         print('APPLICATION DECISION')

# application_stage()
import random
password=input('Create a password: ')


def id_number():
    #generates a random number as the id number of the student just in case they have same names with the other person
    #assuming that not no more than 5000 students will apply
    return random.randint(1,5000)
print(id_number())