class Student:
    def __init__(self,A,B,C):
        self.name = A  # Pubic
        self._age = B  # Protected
        self.__marks = C # Private

    def Display(self):    # Access speicifiers can be applied to methods as well       
        print(self.name)
        print(self._age)
        print(self.__marks)

obj = Student("Rahul", 24, 89)
obj.Display()

# outside members:

print(obj.name)
print(obj._age)
#print(obj.__marks) # Private Variable cant access
#print(obj._Student.__marks)