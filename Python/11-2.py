class animal(object):
    def __init__(self,name,fruit):
        self.name=name
        self.fruit=fruit
    def printintro(self):
        print(self.name, self.fruit)
class animals (animal):
    def __init__(self,name,fruit,sound):
        super().__init__(name,fruit)
        self.sound=sound
x=animals("Barney","bones","woof")
y=animals("Frogy", "flies","trr-trr")
x.printintro()
print(x.name)
print(x.fruit)
print(x.sound)
y.printintro()
print(y.name)
print(y.fruit)
print(y.sound)

