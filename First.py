







# def add_data():
#     data_input=input("assign a data to input: ")
#     database.append(data_input)

# def remove_data():
#     data_remove=input("assign a data to remove from the list: ")
#     database.remove(data_remove)

# database = ["pranav", 'himel',"diba"]

# while True:

#     for index , name in enumerate(database, 1):

#         print(f"{index}) {name}")

#     user_input =input("type keyword here ")

#     if user_input == "add":
#         add_data()
       
#     elif user_input == "remove":
#         remove_data()
#     else:
#         print("user has not inputed valid keyword")










# import json
 
# database = ['Pranav','himel', 'Sangam']
 
      
# json.dump(
#      {'db': database},
#      open('test.json', 'w')
#  )
 

# content = json.load(open('test.json', 'r'))
 
# database_2 = content.get('db')
 
# print(database_2)
# print(type(database_2))



# database = ['Pranav', 'Diba', 'Shuvo']
 
# f = open('test.txt', 'w')
# f.write(str(database))
# f.close()
 
 
# f = open('test.txt', 'r')  
# content = f.read()
# f.close()
 
# database = eval(content)
 
# print(database)
# print(type(database))



import django