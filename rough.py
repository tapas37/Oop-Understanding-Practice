# using the chatbook as module 
# here from oop2_project module i am importing chatbook class then i can use its attributes and methods by creating object of the class


# from oop2_project import chatbook
# yes.chatbook()


# checking for emplyee class

from oop3_set_set_stat import employee
user1=employee()

# this attribute is hidden now using __name
# print(user1.name)

# to access this use this 
# print(user1._employee__name)
# in python nothing is protected unlike java or other language its just hidden


# checking for getter and setter->using the hidden attibute by getter and setter
# print(user1.get_name())
# user1.set_name("tapas")
# print(user1.get_name())



# checking for static variable and methods
# print(user1.id)

# user2=employee()
# print(user2.id)

# user3=employee()
# print(user3.id)


# checking for static method(without using attribute)->(if developer want to start count from other number)
# print(user1.id)
# employee.set_id(10)
# user2=employee()
# print(user2.id)
# user3=employee()
# print(user3.id)







