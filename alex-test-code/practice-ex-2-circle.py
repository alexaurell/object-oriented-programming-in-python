class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    def area(self):
        return 3.14*self._radius**2

    @property
    def radius(self):
        if self._radius < 0:
            self._radius = 0
            return ValueError('Radius cannot be negative')
        else:
            return self._radius
    @property
    def diameter(self):
        return 2*self._radius
    
    @property
    def circumference(self):
        return 2*3.14*self._radius

    def display(self):
        print('Radius', self.radius, 'Diameter', self.diameter, 'Circumference', self.circumference)

circ = Circle(-1)
circ.display()