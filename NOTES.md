## magic 
__cmp__ compare
__eq__(self, other)
Defines behavior for the equality operator, ==.
__ne__(self, other)
Defines behavior for the inequality operator, !=.
__lt__(self, other)
Defines behavior for the less-than operator, <.
__gt__(self, other)
Defines behavior for the greater-than operator, >.
__le__(self, other)
Defines behavior for the less-than-or-equal-to operator, <=.
__ge__(self, other)
Defines behavior for the greater-than-or-equal-to operator, >=.



object.__repr__(self)

Returns a string as a representation of the object.


## input
# A simple Person class

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        rep = 'Person(' + self.name + ',' + str(self.age) + ')'
        return rep


# Let's make a Person object and print the results of repr()

person = Person("John", 20)
print(repr(person))


# output 
'''
Person(John,20)
'''