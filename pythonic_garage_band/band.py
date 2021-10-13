class Band():
    members = []
    bands = []
    
    def __init__(self,name):
        self.name=name
        Band.bands.append(self)
    
    def add_members(self,mname):
        self.mname=mname
        Band.members.append(mname)
    
    def play_solos(self):
        result =''
        for i in Band.members:
            result+= f'{i.play_solo()}\n'
        return result
    
    @classmethod 
    def to_list(cls):
        return cls.members

    def __str__(self):
        return f"Band <{self.name}>"
    
    def __repr__(self):
        return f" '{self.name}' "
