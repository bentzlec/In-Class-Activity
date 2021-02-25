import unittest

def calcFactorial():
    num = int(input("Enter your number"))
    factorial = 1
    
    for i in range(1, (num + 1)):
        factorial = factorial * i
    print(factorial)

def calcFibonacci():
    numTerms = int(input("Enter the number of terms"))
    term_1 = 0
    term_2 = 1
    ctr = 0

    if numTerms == 1:
        print(term_1)
    else:
        while ctr < numTerms:
            print(term_1)
            nth_term = term_1 + term_2
            term_1 = term_2
            term_2 = nth_term
            ctr += 1
    return nth_term

class TestFibonacci(unittest.TestCase):
    def test_1(self):
        self.assertEqual(calcFibonacci(10), 55)
    def test_2(self):
        self.assertNotEqual(calcFibonacci(16), 0)
    def test_3(self):
        self.assertNotEqual(calcFibonacci(10), 16)

def test_factorial():
    assert factorial(5) == 120
def test_factorial_2():
    assert factorial(7) == 5040