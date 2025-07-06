class student: 
    name="penguin"
    grade=10
    age=15
    gender= 'male'

    def introduction(self):
        print("Hi I am a Student")
    def details(self):
        print("my name:", self.name, "my age:", self.age, "my gender:", self.gender)
        
ob=student()


ob.introduction()
ob.details()