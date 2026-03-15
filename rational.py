import math

class Rational():
    def __init__(self, num, denom):
        if denom == 0:
            raise ValueError("Initializing a Rational with 0 denominator.")
        else:
            gcd = math.gcd(num, denom)
            self.num = num//gcd
            self.denom = denom//gcd
    def display(self):
        print(f"{self.num}/{self.denom}")

def addRat(p, q):
    lcm = math.lcm(p.denom, q.denom)
    return Rational(lcm//p.denom * p.num + lcm//q.denom * q.num, lcm)

def subRat(p, q):
    lcm = math.lcm(p.denom, q.denom)
    return Rational(lcm//p.denom * p.num - lcm//q.denom * q.num, lcm)

def mulRat(p, q):
    return Rational(p.num * q.num, p.denom * q.denom)

def divRat(p, q):
    if q.num == 0:
        raise ValueError("Dividing by Rational with numerator 0.")
    return mulRat(p, Rational(q.denom, q.num))

def eqRat(p, q):
    return (p.num == q.num and p.denom == q.denom)