#initiate a class
class employee:
    #special mthd/magic mthd/dunder mthd - constructor
    def __init__(self):
        print("Started executing attributes and data")
        self.id = 12
        self.salary = 5000
        self.dep = "CSE(AI)"
        print("attributes and data have been initiated")
        
        
    def travel(self, destination):
      print("This travel mthd is called manually")
      print(f"EMP is now travaling to {destination}")
        
#create an obj/instance of the class
sam = employee()
print("Salary of SAM is : ", sam.salary)


sam.travel("Pune")

# we did till now
# printing the attributes
# print(sam.id)
# calling a mthd