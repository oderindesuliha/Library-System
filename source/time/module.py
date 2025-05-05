import re
#
#
# my_num = '012346'
# print(re.fullmatch(my_num, '0123456'))
# # print(uk)
#
# if re.fullmatch(my_num, '0123456'):
#     print("E match oo 😂😂😂")
# else:
#     print("E no match oo 😒😒")
#
#
#
# text ='123SddCkk'
# print('\d+[A-Z][a-z]* [A-Z][a-z]*]')

email = "s.oderinde@native.semicolon.africa"
pattern = r'^[a-z0-9@_.+$]*[a-z9@_.+$]*[a-z.]*+$'
if re.fullmatch(pattern, email):
    print("valid email")
else:
    print("invalid email")

