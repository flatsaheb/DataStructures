class Employee:
    def __init__(self, firstname, lastname):
        self.first = firstname
        self.last = lastname
     #   self.email = firstname+'.'+lastname+'@email.com'

    @property
    def email(self):
        return f'{self.first}.{self.last}@email.com'

    @property
    def fullname(self):
        return f'Full name of employee is {self.first} {self.last}'

    @fullname.setter
    def fullname(self,name):
        self.first, self.last = name.split(' ')


emp1 = Employee('John', 'Smith')
emp1.first = 'Golu'
print (emp1.first)
print (emp1.last)
# Below print (emp1.email) not work when we chnage the emp1.first = Golu. It will continue print email address as
# John.Smith@email.com
#print (emp1.email)
# To print email we have to add parenthesis which is not feasible option because that would require changes at
# many places in code. emp1.email(). So to avoid this we can define @property decorator which will allow us to use
# to call emp1.email
#print (emp1.email())
# Below print will now print Golu.Smith@email.com
print (emp1.email)

## Setter Example
#print(emp1.fullname())

# After adding property decorator above fullname function we need tio remove ()
print(emp1.fullname)

# Now lets say emp1.fullname = 'Fakhruddin Latsaheb' we want everything to get change. First Name = Fakhruddin
# Last Name =  Latsaheb and email = fakhruddin.latsaheb@email.com. So in order to do that we have to use setter property

emp1.fullname = 'Fakhruddin Latsaheb'
print (emp1.first)
print (emp1.last)
print (emp1.fullname)
print (emp1.email)



# Below youtube link have more information on this topic.
 #https://www.youtube.com/watch?v=jCzT9XFZ5bw