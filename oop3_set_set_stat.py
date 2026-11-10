# use of getter setter and static method


class employee:

    # 2-using static atribute/variable

    __user_id=0


    def __init__(self):
        # here static variable is not access by self it is access by class
        self.id=employee.__user_id
        employee.__user_id+=1  


        self.__name='Default user'
        self.salary=5000
        self.designation="data scientist"
        

    # 3 -  static method(it is also can be access by class)
    @staticmethod
    def get_id():
        return employee.__user_id

    @staticmethod
    def set_id(val):
        employee.__user_id=val
    







    # 1- we use getter and setter to get and set the hidden attributes
    def get_name(self):
        return self.__name

    def set_name(self,value):
        self.__name=value
        
    
    
    def travel(self,destination):
        print(f"employee is traveling to {destination}")

    def presentation(self):
        print("employee is presenting the project")




