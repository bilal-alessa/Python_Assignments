class Person():
    personName = 'Henry'
    personAge = '30'
    personWeight = 200
    def printAll(self):
        print(self.personName)
        print(self.personAge)
        print(self.personWeight)
        
class Hobbies(Person):
    favoriteGame = 'Call of Duty'
    FavoriteMovie = 'KungPow Enter The First'
    
    def printAll(self):
        print(self.personName)
        print(self.favoriteGame)
        print(self.FavoriteMovie)
        
class Experience(Person):
    job = 'Unemployed'
    experience = 'Software Developer'
    language = 'English'
    
    def printAll(self):
        print(self.personName)
        print(self.personAge)
        print(self.language)

Person().printAll()
Hobbies().printAll()
Experience().printAll()




