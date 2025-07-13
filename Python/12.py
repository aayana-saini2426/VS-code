class animal:
    def make_sound(self):
        pass
class Dog(animal):
    def make_sound(self):
        print("🐶Dog says: WOOF!")
class Cat(animal):
    def make_sound(self):
        print("😺Cat says: MEOW!")
class Cow(animal):
    def make_sound(self):
        print("🐮Cow says: MOO!")
class Frog(animal):
    def make_sound(self):
        print("🐸Frog says: TRR-TRR !")

def animal_sound(animal):
    animal.make_sound()

dog=Dog()
cat=Cat()
cow=Cow()
frog=Frog()

animal_sound(dog)
animal_sound(frog)
animal_sound(cow)
animal_sound(cat)