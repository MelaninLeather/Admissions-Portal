# file_name= 'admission management txt'
#
# profile = {}
# contact = {}
# education = {}
# essay = {}
# activities = {}
# entries=[profile;contact;education;essay;essay;activities]
# full_name=input('What is your name')
# def save_to_file():
#     try:
#         fos = open(file_name, "w")
#
#     except FileNotFoundError:
#         print("File does not exist")
#
#     for profile in entries:
#         parts = [profile[full_name]]
#
#         for key, value in entry.items():
#             parts.append(f"{full_name}, {email_address},{phone_number}, {dob},{gender}, {nationality};{parent_name1}")
#
#         fos.write(";".join(parts) + "\n")
#
#     fos.close()
def save_to_file(profile, contact, education, essay, activities):

    try:
        fos = open('students_admissions.txt', "w")

    except IOError:
        print("Error creating file")

    for id_number in profile:
        # Create a list of parts for this ID number.
        # Adds the profile information.
        parts = [f"Profile: {profile[id_number][0]}"]

        # Add the contact information.
        parts.append(f"Contact: {contact[id_number][0]},{contact[id_number][1]},{contact[id_number][2]},{contact[id_number][3]}")

        # Add the education information.
        parts.append(f"Education: {education[id_number][0]},{education[id_number][1]},{education[id_number][2]}")

        # Add the essay information.
        parts.append(f"Essay: {essay[id_number][0]}")

        #Add the activities information
        parts.append(f"Activities: {activities[id_number][0]}")

        # Join the parts with semicolons and write them to the file followed by a newline character.
        fos.write(";".join(parts) + "\n")


    fos.close()

