#1. Basic - Print all integers from 0 to 150.
for i in range(0, 151):
    print(i)

#2. Multiples of Five - Print all the multiples of 5 from 5 to 1,000
for i in range(0, 1005, 5):
    print(i)

#3. Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for i in range(0, 101, 1):
    if i % 10 == 0:
        print('codingdojo')
    elif i % 5 == 0:
        print('coding')
    else:
        print(i)

#4.  Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
oddtotal = 0
for number in range(1, 500001):
    if(number % 2 == 0):
        #print("{0}".format(number))
        oddtotal = oddtotal + number
print("The Sum of Odd Numbers from 1 to {0} = {1}".format(number, oddtotal)) 
    
#5 Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
for backwards in range(2018, 1, -4):
    print (backwards)

#6 Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
lownum = 2
highnum = 9
mult = 3
for i in range(lownum, highnum+1, 1):
    if i % mult == 0:
        print(i)





