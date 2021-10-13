
from abc import abstractclassmethod

class Band:
   '''
      this class has (name and member )
      member is an array which we add to it every band member once we creat new object
      (calls init fun) 
   '''
   members=[]
   def __init__(self,name,memberName):
         self.name =name 
         Band.members.append(memberName)


   def play_solos(self):
    print("Hello my name is " + self.name)

    
   def to_list(self):
    print("Hello my name is " + self.name)
   


 

class Guitarist:
      def __init__ (self,name):
            self.name=name
      def __str__(self):
            return (f'My name is {self.name} and I play guitar')
      def __repr__(self):
            return (f'Guitarist instance. Name = {self.name}')
      def get_instrument(self):
          return 'guitar'
      def play_solos (self):
          return 'face melting guitar solo'

class Drummer(Guitarist):
       def __str__(self):
            return (f'My name is {self.name} and I play drums')
       def __repr__(self):
            return (f'Drummer instance. Name = {self.name}')
       def get_instrument(self):
          return 'drums'
       def play_solos (self):
          return 'rattle boom crash'

 
class Bassist(Guitarist):
       def __str__(self):
            return (f'My name is {self.name} and I play bass')
       def __repr__(self):
            return (f'Bassist instance. Name = {self.name}')
       def get_instrument(self):
          return 'bass'
       def play_solos (self):
          return 'bom bom buh bom'


class Musician:
    members = []

    def init(self, name):

        self.name = name
        Musician.members.append(self)

    @abstractclassmethod
    def str(self):
        pass

    @abstractclassmethod
    def repr(self):
        pass

    @abstractclassmethod
    def get_instrument(self):
        pass

    @abstractclassmethod
    def play_solo(self):
        pass




ash=Drummer('ash')
print(ash.get_instrument())