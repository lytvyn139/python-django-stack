import unittest

def ReverseList(array):
    for i in range(len(array)//2):
        temp = array[i]
        array[i] =  array[len(array)-1-i]
        array[len(array)-1-i] = temp
    return array

class IsReverseTest(unittest.TestCase):
    def testTwo(self):
        self.assertEqual(ReverseList([1,3,5]), [5,3,1])
    def testThree(self):
        self.assertEqual(ReverseList(["taco", 3, "salsa", 0]), [0, "salsa", 3, "taco"])
    def testFour(self):
        self.assertEqual(ReverseList(['mr', 'owl', 'te', 'my', 'metal', 'worm']),['worm', 'metal', 'my', 'ate', 'owl', 'mr'])
    def testFive(self):
        self.assertEqual(ReverseList([34,0,-7,1,2,-8]),[-8,2,1,-7,0,34])



def IsPalindrome(string):
    for i in range(len(string)//2):
        if string[i] != string[len(string)-1-i]:
            return False
    return True

class IsPalindromeTest(unittest.TestCase):
    def testTwo(self):
        self.assertEqual(IsPalindrome('racecar'), True)
    def testThree(self):
        self.assertFalse(IsPalindrome('rabcr'))
    def testFour(self):
        self.assertTrue(IsPalindrome('tacocat'))
    def testFive(self):
        self.assertEqual(IsPalindrome('Mr. owl ate my metal worm'), False)
    def testSix(self):
        self.assertEqual(IsPalindrome('mrowlatemymetalworm'), True)



def Coins(TotalAmount):
    Quarters = 0
    Dimes = 0
    Nickles = 0
    Pennies = 0
    SortedChange = []
    while TotalAmount > 0:
        while TotalAmount >= 25:
            TotalAmount -= 25
            Quarters += 1
        while TotalAmount >= 10:
            TotalAmount -= 10
            Dimes += 1
        while TotalAmount >= 5:
            TotalAmount -= 5
            Nickles += 1
        while TotalAmount >= 1:
            TotalAmount -= 1
            Pennies += 1
    SortedChange.extend((Quarters, Dimes, Nickles, Pennies))
    return SortedChange

class CoinsTest(unittest.TestCase):
    def testTwo(self):
        self.assertEqual(Coins(87),[3,1,0,2])
    def testThree(self):
        self.assertEqual(Coins(125),[5,0,0,0])
    def testFour(self):
        self.assertTrue(Coins(123456789),[4938271,1,0,4])
    def testFive(self):
        self.assertEqual(Coins(41),[1,1,1,1])
    def testSix(self):
        self.assertEqual(Coins(104),[4,0,0,4])



def Factorial(int):
    if int == 0:
        return 1
    elif int < 0:
        return int
    for i in range(int-1, 0, -1):
        int *= i
    return int

class IsFactorial(unittest.TestCase):
    def testTwo(self):
        self.assertEqual(Factorial(5), 120)      
    def testThree(self):
        self.assertEqual(Factorial(0), 1)      
    def testFour(self):
        self.assertEqual(Factorial(-2), -2)      



def Fibonacci(Sequence):
    if Sequence < 0:
        return Sequence
    elif Sequence == 1:    
        return 0
    elif Sequence == 2:
        return 1
    else:
        return Fibonacci(Sequence-1)+Fibonacci(Sequence-2)

class IsFibonacci(unittest.TestCase):
    def testTwo(self):
        self.assertEqual(Fibonacci(5), 3)
    def testThree(self):
        self.assertEqual(Fibonacci(9), 21)
    def testTwo(self):
        self.assertEqual(Fibonacci(-3), -3)

if __name__ == "__main__":
    unittest.main()

# Use this to test out python algorithms and errorsa
