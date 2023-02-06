class Fraction:
    def __init__(self, nr, dr = 1):
        if dr == 0:
            raise ZeroDivisionError('Denominator cannot be zero')
        if dr < 0:
            dr = -dr    
            nr = -nr
        self.nr = nr
        self.dr = dr

    def show(self):
        print(self.nr, '/', self.dr)
    
    def multiply(self, other):
        if isinstance(other, int):
            return Fraction(self.nr * other, self.dr)
        else:
            return Fraction(self.nr * other.nr, self.dr * other.dr)

    def add(self, other):
        if isinstance(other, int):
            return Fraction(self.nr + other * self.dr, self.dr)
        else:
            return Fraction(self.nr * other.dr + other.nr * self.dr, self.dr * other.dr)

f1 = Fraction(2,3)
f1.show()
f2 = Fraction(3,4)
f2.show()
f3 = f1.multiply(f2)
f3.show()
f3 = f1.add(f2)
f3.show()
f3 = f1.add(5) 
f3.show()
f3 = f1.multiply(5) 
f3.show()