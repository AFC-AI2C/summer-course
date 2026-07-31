
# A list can be changed
my_list = ['c', 'a', 't']


# you can my_list[0] = z  change c to z cna do

# A sting can not be changed 
my_string = "cat"

# you cant my_sting[0] = z  you will brak it the place in the string is locked


# 1. Loop over Both
# for item in my_list:
#     print(item)

# for char in my_string:
#     print(char)


# print(my_list[0], my_string[0])
# print(my_list[-1], my_string[-1])
# print(my_string[0:2])


# print(len(my_list), len(my_string))
# print('a' in my_list, 'a' in my_string)

# print(list("cat")) 


# #Keep working on this ####



# # Define the function 
# def validate_username(username: str) -> bool:
#     is_between_5and15 = True
#     starts_with_alpha = True
#     no_underscore_at_end= True
#     is_a_number_or_leter_or_underscore = True


# # username is more than 5 characters and not more than 15 character
#     if len(username) >= 5  and len(username)<= 15:
#        is_between_5and15 = True
#     else:
#        is_between_5and15  = False


# # username starts with a a letter
#     if username and username[0].isalpha():
#         starts_with_alpha = True
#     else:
#         starts_with_alpha = False

# # username doesnt end with "_"
    
#     if username and username[-1] != "_":
#         no_underscore_at_end = True
#     else:
#          no_underscore_at_end = False
 
# # make sure user name only uses number alpha or unnderscore 
#     for char in username:
       
#         if not (char .isalnum() or char == "_"):
#             is_a_number_or_leter_or_underscore = False
        

#     return (is_between_5and15 
#     and starts_with_alpha
#     and no_underscore_at_end
#     and is_a_number_or_leter_or_underscore) 

# while True:
#     username_input = input("enter your username: ")

#     if validate_username(username_input):
#         print("User name accepted")
#         break

#     else:
#         print("User nam enot vaild, please try again. ")



##############################################################################33

# passengers = ["Lopez", "tony", "todd", "jacob"]


# for index, passenger in enumerate(passengers, 1):
#     print(f"passenger {passenger} in seat {index}")


        


    


    