# Hello World program in Python

class Person(object):
   #Common for all objects of the class[like static variables]
   count = 0
    
   #constructor
   def __init__(self, owner_name, age):
      self.owner_name = owner_name
      self.age = age
      Person.count += 1
      
   def getOwner_name(self):
        return self.owner_name
        
   def displayCount(self):
     print "Total Objects created so far : ", Person.count

   def displayPersonDetails(self):
      print "Name : ", self.name,  ", Age: ", self.age
class Pet(object):
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def getName(self):
        return self.name

    def getSpecies(self):
        return self.species

    def __str__(self):
        return "%s is a %s" % (self.name, self.species)

class Dog(Pet, Person):
    def __init__(self, name, owner):
        Pet.__init__(self, name, "Dog")
        Person.__init__(self,owner.owner_name, owner.age )

owner= Person("CJ", 25)
myPet=Dog("Spike", owner)
print myPet.getName()
print myPet.getOwner_name()