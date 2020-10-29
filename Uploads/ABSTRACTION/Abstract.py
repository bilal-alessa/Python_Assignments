from abc import ABC, abstractmethod
class LivingThings(ABC):
    def Habitat(self, area):
        print('And the habitat in which these species lives is a {}'.format(area))
        
        @abstractmethod
        def specie(self, kind):
            pass
    
class Plant(LivingThings):
    def specie(self, kind, base):
        print('The {} type of species are {} based'.format(kind, base))
        
if __name__ == "__main__":
    obj = Plant()
    obj.specie("Tree", "Plant")
    obj.Habitat("Forest")
