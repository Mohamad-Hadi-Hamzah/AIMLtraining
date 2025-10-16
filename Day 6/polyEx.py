# class Bird:
#     def fly(self):
#         print('Birds can fly')

# class Airplane(Bird):
#     def fly(self):
#         print('Airplanes fly')

# b=Bird()
# print('Bird Implement')
# b.fly()

# print('Airplane Implementation')
# a=Airplane()
# a.fly()
# print('Using for loop')
# for obj in [Bird(),Airplane(),]:
#     obj.fly()


#contoh
class Emp:
    def reg(self):
        self.id=int(input ('Enter Id: '))
        self.name=input('Enter Name: ')

    def disp(self):
        print('Name: ',self.name)
        print('Id: ',self.id)

class Dev(Emp):
    def reg(self):
        super().reg()
        self.domain=input('Enter Domain: ')

    def disp(self):
        super().disp()
        print('Domain: ',self.domain)

d1=Dev()
d1.reg()
d1.disp()



