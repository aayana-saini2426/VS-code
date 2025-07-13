class employee:
    def __init__(self,name,email,password):
        self.name=name
        self.email=email
        self.__password=password
    def show_intro(self):
        print("name:",self.name)
        print("email", self.email)
    def check_password(Self):
        print("Password is hidden for safety")
    def update_password(self,new_password):
        self.__password=new_password
        print("Password is updated")

emp=employee("Aayana", "aayana@example.com", "secret123")
emp.show_intro()
emp.check_password()
emp.update_password("me2426")
