class Emp:
    def __init__(self,id,name,qual):
        self.id=id
        self.name=name
        self.qual=qual

    def display(self):
        print('Id: ',self.id)
        print('Name: ',self.name)
        print('Qualification: ',self.qual)

class Dev(Emp):
    def __init__(self, id, name, qual,domain,project):
        super().__init__(id, name, qual)
        self.domain=domain
        self.project=project

    def display(self):
        super().display()
        print('Domain: ',self.domain)
        print('Project: ',self.project)

#create one Emp object with id=1, name='Sam', qual='MCA'
#create one Dev object with id=3, name='Ravi',qual='Mtech',Projects='eShopping',Domain='dot net'
#display Dev details
#display Emp details
    
e1 = Emp(1, 'Sam', 'MCA')
d1 = Dev(3, 'Ravi', 'Mtech', 'dot net', 'eShopping')

print("\nEmployee Details:")
e1.display()
print("Developer Details:")
d1.display()