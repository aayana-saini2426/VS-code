class person(object):
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def printname(self):
        print(self.fname, self.lname)
class student (person):
    def __init__(self, fname, lname,year):
        super().__init__(fname, lname)
        self.graduationyear=year
x=student("Pippa","Amobi","2019")
y=student("Ravi", "Singh","2018")
x.printname()
print(x.fname)
print(x.lname)
print(x.graduationyear)
y.printname()
print(y.fname)
print(y.lname)
print(y.graduationyear)

