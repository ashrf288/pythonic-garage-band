


class Band:
   member=[]
   def __init__(self,name,members  ):
         self.name =name 
       


   def play_solos(self):
    print("Hello my name is " + self.name)

    
   def to_list(self):
    print("Hello my name is " + self.name)


class Guitarist:
      def __init__ (self,name):
            self.name=name
      def __str__(self):
            return (f'My name is {self.name} and I play guitar')