class person (object):
    def __init__(self,name,idnumber):
        self.name = name
        self.idnumber=idnumber
    def display (self):
        print(self.name)
        print(self.idnumber)
class employee (person):
    def __init__(self, name, idnumber,salary,post):
        self.salary=salary
        self.post=post
        person.__init__( self,name,idnumber)
a=employee("Aayana", "899965", "15000", "Cashier")
b=employee("Mango","8755666","20000", "manager")
c=employee("Banana", "7899950", "12000", "intern")
d=employee("tulips", "987456", "5000", 'janitor')

a.display()
b.display()
c.display()
d.display()