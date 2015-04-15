class Fraction:

    def __init__(self, numerator, denominator):
        if (numerator<=denominator):
            x=numerator
        else:
            x=denominator
        while x>1:
            if(numerator%x==0 and denominator%x==0):
                numerator=numerator//x
                denominator=denominator//x
            x-=1
        self.numerator = numerator
        self.denominator = denominator


    def __str__(self):
        if (self.numerator==self.denominator or self.numerator==0):
            return str(self.numerator)
        else:
            return "{} / {}".format(self.numerator, self.denominator)


    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return (self.numerator==other.numerator and self.denominator==other.denominator)

    def __add__(self, other):
        if(self.denominator==other.denominator):
            return (Fraction((self.numerator+other.numerator), self.denominator))
        else:
            return (Fraction((self.numerator*other.denominator)+other.numerator*self.denominator, self.denominator*other.denominator))

    def __sub__(self,other):
        other.numerator=-other.numerator
        return (self.__add__(other))

    def __mul__(self, other):
        return(Fraction((self.numerator*other.numerator), self.denominator*other.denominator))

a=Fraction(1,2)
b=Fraction(2,4)

#print (a*b)