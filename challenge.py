#!python3

"""
Population growth can be modeled with the equation P = p*(1+r)^n
Where 
P is the future Population
p is the current population
r is the annual rate of grown as a decimal
n is the number of years

Write a function to determine the future population

Given 2 groups with given starting populations and different rates of growth,
determine how many years in the future they will have the same population or 
if they are diverging and will never have the same population
"""
# sort pop func into four types: higher pop with higher rate/lower with lower rate = diverging 
# smaller pop with a higher rate = could be converging
def population(p,r,t):
    P = p*(1+r)**t
    return P

def equal(p1,r1,p2,r2):
    outcome = False
    i = 0
    x = population(p1,r1,i)
    y = population(p2,r2,i)
    if x > y: 
        h = x
        l = y
        rh = r1
        rl = r2
    elif y > x:
        h = y
        l = x
        rh = r2
        rl = r1
    if rh > rl:
        return None
    while outcome == False:
        x = population(p1,r1,i)
        y = population(p2,r2,i)
        if x == y:
            return i
        if l > h:
            return i - 1 
        input(f"{i} {x} {y}")
        i = 1+i
        
        

def tests():
    assert round(population(1000,.05, 5)) == 1276
    assert round(population(1000,.02, 20)) == 1486
    assert equal(1000,.05,2000,.06) == None
    assert round(equal(1000,.03,2000,.01)) == 35
    
tests()