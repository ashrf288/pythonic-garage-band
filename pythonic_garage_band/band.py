


class Band:
  
   def __init__(self,name,members  ):
         self.name =name 
         self.members=members


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

class Drummer(Guitarist):
       def __str__(self):
            return (f'My name is {self.name} and I play drums')
       def __repr__(self):
            return (f'Drummer instance. Name = {self.name}')

class Bassist(Guitarist):
       def __str__(self):
            return (f'My name is {self.name} and I play bass')
       def __repr__(self):
            return (f'Bassist instance. Name = {self.name}')