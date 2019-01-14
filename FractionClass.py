
# Simplify Fraction
def gcd (m,n):

    while m%n != 0:
        oldM = m
        oldN = n

        m = oldN
        n = oldM%oldN
    return n

class Fraction:

    def __init__(self, top, bottom):

        if isinstance (top, float) or isinstance(bottom, float): 
            raise RuntimeError("Error: Numerator / Denominator must be whole numbers")

        if bottom < 0:
            abs(bottom)
        
        self.common = gcd(top, bottom)
        self.num = top // self.common
        self.den = bottom // self.common

    def __str__(self):
        return str(self.num)+"/"+str(self.den)
        
    def show(self):
        print (self.num, "/", self.den)

    def __repr__(self):
        return "Numerator (top):%s -- Denominator (bottom: %s)" % (self.num, self.den)

#Arithmatic method overrides

    # +
    def __add__(self, other):
        newNum = self.num*other.den+self.den*other.num
        newDen = self.den*other.den

        return Fraction(newNum, newDen)

    # Right side addition, used when adding an integer to a fraction
    def __radd__(self, other):
        other = Fraction(other,1)
        return self.__add__(other)

    # += adds and combines 2 variables into the first variable
    def __iadd__(self, other):
        if isinstance(self, int):
            self = Fraction(self, 1)
        if isinstance(other, int):
            other = Fraction(self,1)

        self = self.__add__(other).gcd(self.num,self.den)
        
        return Fraction(self.num, self.den)
                 
    # -
    def __sub__(self, other):
        newNum = self.num*other.den - self.den*other.num
        newDen = self.den*other.den

        return Fraction(newNum, newDen)

    # x
    def __mul__(self, other):
        newNum = self.num*other.num
        newDen = self.den*other.den

        return Fraction(newNum, newDen)

    # /
    def __truediv__(self, other):
        newNum = self.num*other.den
        newDen = self.den*other.num

        return Fraction(newNum,newDen)

# Logical Operator method overrides

    #Equal to
    def __eq__(self, other):
        firstNum = self.num * other.den
        secondNum = other.num * self.den
    
        return firstNum == secondNum

    #Greater than
    def __gt__(self, other):
        firstNum = self.num * other.den
        secondNum = other.num * self.den

        return firstNum > secondNum

    #Greater or Equal 
    def __ge__(self,other):
        firstNum = self.num * other.den
        secondNum = other.num * self.den

        return firstNum >= secondNum

    #Less than
    def __lt__(self,other):
        firstNum = self.num * other.den
        secondNum = other.num * self.den

        return firstNum < secondNum

    #Less or Equal
    def __le__(self, other):
        firstNum = self.num * other.den
        secondNum = other.num * self.den

        return firstNum <= secondNum

    #Not Equal
    def __ne__(self,other):
        firstNum = self.num * other.den
        secondNum = other.num * self.den

        return firstNum != secondNum
    
# Return Value methods    
    def getNum(self):
        return self.num

    def getDen(self):
        return self.den
