# simple inheritance

# base class
class employe:
  def __init__(self,name,salary):
    self.name = name
    self.salary = salary
    
  def details(self):
    print(f"Employee name: {self.name}")
    print(f"Employee salary: {self.salary}")
    
    
# derived class    
class Manager(employe):
  def __init__(self,name,salary,Dept):
    super().__init__(name,salary)
    self.Dept = Dept
    
  def details(self):
    super().details()
    print(f"Employee Department: {self.Dept}")
    
class SeniorManager(Manager):
  def __init__(self, name, salary, Dept,Exp):
    super().__init__(name, salary, Dept)
    self.Exp = Exp
    
  def details(self):
    super().details()
    print(f"Employee Experience: {self.Exp}")
    
class Bonus:
  def __init__(self,insentive):
    self.insentive = insentive
    
  def BONUS(self):
    print(f"Employee BONUS: {self.insentive}")
    
"""Example of Multiple inheritance of Employee and Bonus"""
    
class Festive_Salary(employe,Bonus):
  def __init__(self, name, salary,insentive):
    employe.__init__(self,name, salary)
    Bonus.__init__(self,insentive)
    

"""Example of Hirarchical inheritance of Employee and Bonus"""   

class Emp1(employe):
  def Work(self):
        print(f"{self.name} is Developing Game.")
    
class Emp2(employe):
  def Break(self):
        print(f"{self.name} is Drinking Tea.")


# create object 
print("\nManager Called\n")
emp = Manager("Pradeep", 50000000, "CEO")
emp.details()

print("\nEmployee Called\n")
emp = employe("Pradeep", 500000)
emp.details()
    
print("\nSeniorManager Called\n")
emp = SeniorManager("Pradeep", 50000000, "CEO",12)
emp.details()

print("\nFestive Salary Called\n")
emp = Festive_Salary("Pradeep",50,100000)
emp.details()
emp.BONUS() 

print("\nWhat is Employe Doing\n")   
emp = Emp1("pradeep",50000)
emp.Work()

emp = Emp2("Ram",50000)
emp.Break()

    
"""Example of hybrid Inheritance"""
    
# # Base class
# class Employee:
#     def __init__(self, name):
#         self.name = name

#     def work(self):
#         print(f"{self.name} is working.")


# # Child 1
# class Manager(Employee):
#     def manage(self):
#         print(f"{self.name} manages the team.")


# # Child 2
# class Developer(Employee):
#     def code(self):
#         print(f"{self.name} writes Python code.")


# # Child of Manager and Developer
# class TechLead(Manager, Developer):
#     def lead(self):
#         print(f"{self.name} leads the project.")


# emp = TechLead("Pradeep")

# emp.work()
# emp.manage()
# emp.code()
# emp.lead()

    
    
    
    
    
    

    
"""Example of Multilevel Inheritance"""
    
# class emp:
#   def __init__(self,name,salary):
#     self.name = name
#     self.salary = salary
    
#   def details(self):
#     print(f"Emp name: {self.name}")
#     print(f"Emp salary: {self.salary}")
    
# class manager(emp):
#   def __init__(self,name,salary,Dep):
#     super().__init__(name,salary)
#     self.Dep = Dep
    
    
#   def details(self):
#     super().details()
#     print(f"Emp Dept: {self.Dep}")
    
# class SeniorEmp(manager):
#   def __init__(self, name,salary, Dep,Exp):
#     super().__init__(name,salary, Dep)
#     self.Exp = Exp
    
#   def details(self):
#     super().details()
#     # print(f"Emp name: {self.name}")
#     # print(f"Emp Dept: {self.Dep}")
#     print(f"Emp Experience: {self.Exp}")
  
  
  
  
# em = emp("pradeep",5000)
# man = manager("pradeep",500000,"manager")
# se_emp = SeniorEmp("pradeep",500000,"manager",13)
# em.details()
# man.details()
# se_emp.details()

"""Example of Multiple Inheritance"""

# class employe:
#   def __init__(self,name,salary):
#     self.name = name
#     self.salary = salary
    
#   def details(self):
#     print(f"Employee name: {self.name}")
#     print(f"Employee salary: {self.salary}")
    
# class Bonus:
#   def __init__(self,insentive):
#     self.insentive = insentive
    
#   def BONUS(self):
#     print(f"Employee BONUS: {self.insentive}")
    
    
# class Festive_Salary(employe,Bonus):
#   def __init__(self, name, salary,insentive):
#     employe.__init__(self,name, salary)
#     Bonus.__init__(self,insentive)
    
# print("\nFestive Salary Called\n")
# emp = Festive_Salary("Pradeep",50,100000)
# emp.details()
# emp.BONUS()