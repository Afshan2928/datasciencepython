#syntax of inheritance
# class BaseClass:
# Body of base class
# class DerivedClass(BaseClass):
# Body of derived class

#single inheritance
#multiple inheritance
# class Base1:
# pass
# class Base2:
# pass
# class MultiDerived(Base1, Base2):
# pass

#multilevel inheritance


class person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname,self.lastname)
x=person("John","Doe")
x.printname()
# class student(person):
#     pass
# x=student("mike","jollie")
# x.printname()
# class student(person):
#     def __init__(self, fname, lname):
#         person.__init__(self,fname,lname)
# x=student("Alia","Talwar")
# x.printname()
# class student(person):
#     def __init__(self, fname, lname):
#         super().__init__(fname,lname)
# x=student("Ria","Sharma")
# x.printname()
# class student(person):
#     def __init__(self, fname, lname):
#         super().__init__(fname,lname)
#         self.graduationyear=2023
# x=student("Ria","Sharma")
# print(x.graduationyear)





        