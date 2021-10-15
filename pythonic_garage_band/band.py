


class Musician:
    '''
         this is the super class of all other classes
         with 4 methods and the constructer

    '''
    def __init__(self, name):
        self.name = name

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def get_instrument(self):
        pass

    def play_solo(self):
        pass
class Band(Musician):
    '''
    this class takes has  1 class mthod and one class variable and 4 methods
    this class stores all instencies of the muscicain class
    '''
    instances = []

    def __init__(self, name, members):
        self.name = name
        self.members = members
        Band.instances.append(self)
    def play_solos(self):
        solos_member = []
        for member in self.members:
            solos_member.append(member.play_solo())
        return solos_member

    def __str__(self):
        return f" band {self.name}"

    def __repr__(self):
       return f"{self.name}"
    @classmethod
    def to_list(cls):
        return cls.instances

class Guitarist (Musician):
      def __init__ (self,name):
            self.name=name
      def __str__(self):
            return (f'My name is {self.name} and I play guitar')
      def __repr__(self):
            return (f'Guitarist instance. Name = {self.name}')
      def get_instrument(self):
          return 'guitar'
      def play_solo (self):
          return 'face melting guitar solo'

class Drummer(Musician):
       def __str__(self):
            return (f'My name is {self.name} and I play drums')
       def __repr__(self):
            return (f'Drummer instance. Name = {self.name}')
       def get_instrument(self):
          return 'drums'
       def play_solo (self):
          return 'rattle boom crash'

 
class Bassist(Musician):
       def __str__(self):
            return (f'My name is {self.name} and I play bass')
       def __repr__(self):
            return (f'Bassist instance. Name = {self.name}')
       def get_instrument(self):
          return 'bass'
       def play_solo (self):
          return 'bom bom buh bom'





ash=Drummer('ash')
print(ash.get_instrument())