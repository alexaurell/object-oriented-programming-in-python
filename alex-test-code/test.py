class Person:
    def set_details(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print('I am', self.name)
    
    def greet(self):
        print('Hello, how are you doing?', self)

p1 = Person()

p1.set_details('Tom', 8)
p1.display()
