class books:
    def __init__(self,name,author):
        self.name=name
        self.author=author
book1 = books("Powerless", "Lauren Roberts")
book2 = books("As good as dead", "Holly Jackson")
   

print("My library has:", book1.name, "written by", book1.author)

print("My library has:", book2.name, "written by", book2.author)

        