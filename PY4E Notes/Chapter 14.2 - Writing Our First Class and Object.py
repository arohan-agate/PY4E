class PartyAnimal:  # 'class' is a reserved word. This is the template for making PartyAnimal objects.
    x = 0  # attribute associated with each PartyAnimal object

    def party(self):
        self.x = self.x + 1
        print("So far", self.x)

an = PartyAnimal()  # constructs a PartyAnimal object and store in the variable 'an'

an.party()  # no parameter is needed because 'an', the object, is passed in as a varaible
an.party()
an.party()