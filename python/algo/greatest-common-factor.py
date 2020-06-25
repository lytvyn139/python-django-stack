"""
Greatest Common Factor
Given two integers, create rGCF(num1,num2) to recursively determine Greatest Common Factor 
(the largest integer dividing evenly into both). 
Greek mathematician Euclid demonstrated these facts:
1) gcf(a,b) == a, if a == b;
2) gcf(a,b) == gcf(a-b,b), if a>b;
3) gcf(a,b) == gcf(a,b-a), if b>a.”
"""

def gcf(num1, num2):
    if num1 == num2:
        return num1
    elif num1 > num2:
        return gcf(num1 - num2, num2)
    else:
        return gcf(num1, num2 - num1)

print ( gcf(25,20) ) #5
print ( gcf(6,12) )  #6

