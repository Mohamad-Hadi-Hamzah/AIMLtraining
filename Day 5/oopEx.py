#class className:
    #definition of class
    #attribute Method,constructors

#objective=ClassName()
#objectname.Methodname()

#contoh 1
# class Emp:
#     def display():
#         print('Display of employee class')

# obj = Emp()
# obj.display()

# e=Emp()
# e.display()

#contoh 2
class Emp:
    def reg(self,eid,ename):
        self.eid=eid
        self.ename=ename

    def display(self):
        print('Employee Id: ',self.eid)
        print('Employee Name: ',self.ename)

e1 = Emp()
e2 = Emp()
e3 = Emp()
e1.reg(1,'Rose')
e2.reg(22,'Jennie')
e3.reg(66,'Jisoo')
print('First Employee Details')
e1.display()
print('Second Employee Details')
e2.display()
print('Third Employee Details')
e3.display()

