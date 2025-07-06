class parrot:
    name= 'mithu'
    color= 'green'
    fruit= 'mango'
    
    def talk(self):
         print(self.name, "says Hello!")
    def eat(self):
         print(self.name, "eats" , self.fruit)

ob=parrot()
print("name:",ob.name)
print("color:", ob.color)

ob.talk()
ob.eat()

