#!python3
"""
##### Problem 2
Create a function that determines if a triangle is acute, right or obtuse.  
3 input parameters:  
float: one side  
float: another side  
float: 3rd side  

return:
0 : triangle does not exist
1 : if the triangle is acute
2 : if the triangle is right
3 : if the triangle is obtuse

Sample assertions:  
assert triangle(12,5,13) == 2     
assert triangle(5,3,3) == 3  
assert triangle(5,15,12) == 3  
assert triangle(1,1,4) == 0  
(2 points)
"""

def triangle(x,y,z):
    import statistics
    import math
    # pi radians = 180 degrees
    # 3.14 radians = 180 degrees

    numlist = (x,y,z)
    a = min(x,y,z) 
    b = statistics.median(numlist)
    c = max(x,y,z)
    if a + b < c:
        result = 0
        return result
    else:
        anglec = math.acos((a**2 + b**2 - c**2)/(2*a*b))
        anglec = anglec/3.14*180
        anglec = round(anglec,0)

    if anglec < 90:
        result = 1
        return result
    elif anglec == 90:
        result = 2
        return result
    elif anglec > 90: 
        result = 3
        return result

def tests():
    assert triangle(12,5,13) == 2     
    assert triangle(5,3,3) == 3  
    assert triangle(5,15,12) == 3  
    assert triangle(1,1,4) == 0  


if __name__== "__main__":
    tests()
