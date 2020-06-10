#https://pynative.com/python-random-randrange/

import random 
def randInt(min=0 , max=100):
    if max < 0:
        return "MAX must be > 0 pal"
    elif min > max:
        return "MIN is > MAX buddy "
    else:
        num = random.random()*max
        num = round(num)
    return num

print(randInt(0, 20))             # 0 to 20 default
print(random.randint(0,50))       # 0 to 50

print(randInt(max=50,min=100))     #ERROR
print(randInt(max=-5))             #ERROR


# Random number between 25 and 249 divisible by 5
#num = random.randrange(25, 250, 5)
#print("Random integer: ", num)