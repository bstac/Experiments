def av(a,b):
    return (a+b)/2.0

def avg(a,b):
    f = (a*a) - (b*b) + a + b
    d = a - b + 1.0
    f = f/d
    return (f/2.0)

#used these to test a rule I found for
#the average of arethmetic sequences while studying for the
#GRE test. It works out, only differences involving pythons
# use of -0 where found, in my equation anyways.
