# # user_entry = input('Enter your name or your id : ')
# # try:
# #     user_entry = eval(user_entry)
# # except:
# #     pass
# #
# #
# # identification ={
# #     71972027:'yoofi awotwi',
# #     98652927:'melanie chitehwe'
# # }
# #
# # individual_data = {
# #     'yoofi awotwi':['06/05/05','male','ghanaian'],
# #     'melanie chitehwe':['30/01/03','female','zimbabwean']
# # }
# #
# # contact = {
# #     'yoofi awotwi':['0204833295','yoofi.awotwi@ashesi.edu.gh'],
# #     'melanie chitehwe':['0547862981','melanie.chitehwe@ashesi.edu.gh']
# # }
# #
# # if type(user_entry) == int:
# #     profile = identification[user_entry]
# # else:
# #     profile = user_entry
# #
# #
# # print(individual_data[profile])
# # print(contact[profile])
#
# profile = {}
# contact = {}
# education = {}
# essay = {}
# activities = {}
# def load_from_file():
#     try:
#         fout = open('admission_management.txt', 'r')
#
#         for line in fout:
#             entries = line.strip().split(";")
#             stages = 0
#
#             identification_number = 0
#             for individual_data in entries:
#                 individual_data = individual_data.split(',')
#                 if stages == 0:
#                     identification_number = individual_data[2]
#                     profile[identification_number] = [individual_data[0], individual_data[1], individual_data[3],
#                                                       individual_data[4], individual_data[5], individual_data[6]]
#                 elif stages == 1:
#                     contact[identification_number] = individual_data
#                 elif stages == 2:
#                     education[identification_number] = individual_data
#                 elif stages == 3:
#                     essay[identification_number] = individual_data
#                 elif stages == 4:
#                     activities[identification_number] = individual_data
#
#                 stages += 1
#     except:
#         pass
#
#
# load_from_file()
# print(profile)
# print(contact)
# print(education)
# print(essay)
# print(activities)
#


dict={
    1:2,
    3:5
}

dict[8]=7
print(dict)

