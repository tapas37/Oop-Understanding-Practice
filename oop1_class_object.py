# shown about the class and object 

# initiating class

class employee:
    # special method/constructor/magic method -> autometically execute when object is created
    def __init__(self):
        print(id(self))
        self.id=123
        self.salary=5000
        self.designation="data scientist"
        # these are the attribute of the class that will assign to the object 
    
    
    # this is the fucntion/method that object willdo when needed(travel or presentation etc etc)
    def travel(self,destination):
        print(f"employee is traveling to {destination}")

    def presentation(self):
        print("employee is presenting the project")



# object/instance is created
tapas=employee()
tapas.travel("londo")
tapas.presentation()


# you can create atribute from outside as well
tapas.name="tapas parida"
print(tapas.name)


# print(id(self)) = rint(id(tapas)) will be same self is nothing but this object we are creating and have the same id number for each object and self
print(id(tapas))

