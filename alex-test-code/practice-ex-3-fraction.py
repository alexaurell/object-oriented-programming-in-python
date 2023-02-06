class Fraction:
    def __init__(self, nr, dr = 1):
        if dr == 0:
            raise ZeroDivisionError('Denominator cannot be zero')
        if dr < 0:
            dr = -dr    
            nr = -nr
        self.nr = nr
        self.dr = dr
        self._reduce()

    def show(self):
        print(self.nr, '/', self.dr)
    
    def multiply(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        f = Fraction(self.nr * other.nr, self.dr * other.dr)
        f._reduce()
        return f

    def add(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        f = Fraction(self.nr * other.dr + other.nr * self.dr, self.dr * other.dr)
        f._reduce()
        return f
    
    @staticmethod
    def hcf(x,y):
        x = abs(x)
        y = abs(y)
        smaller = y if x > y else x
        s = smaller
        while s > 0:
            if x%s == 0 and y%s == 0:
                break
            s -= 1
        return s

    def _reduce(self):
        hcf = Fraction.hcf(self.nr, self.dr)
        if hcf == 0:
            return
        self.nr //= hcf
        self.dr //= hcf

f1 = Fraction(6,36)
f1.show()
f2 = Fraction(2,-12)
f2.show()
f3 = f1.multiply(f2)
f3.show()
f3 = f1.add(f2)
f3.show()
f3 = f1.add(5) 
f3.show()
f3 = f1.multiply(5) 
f3.show()