import unittest
'''
def my_div(a, b):
    return a / b
class TestFunc(unittest.TestCase):
    def test_div(self):
        self.assertEqual(2, my_div(4,2))
        self.assertEqual(-2, my_div(2,-1))
       
    def test_div_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            my_div(1,0)
                         
if __name__ == "__main__":
    unittest.main()
 '''


def my_func1(a):
    if a == 1:
        return 2
    elif a == -1:
        return 3
    else:
        return 1

def my_func2(b):
    if b != "yes":
        raise ValueError("you can only say yes!")
    else:
        return True

class TestFunc(unittest.TestCase):
    def test_func1(self):
        self.assertEqual(2, my_func1(1))
        self.assertEqual(3, my_func1(-1))
        for i in range(-100,100):
            if i == 1 or i == -1:
                continue
            self.assertEqual(1, my_func1(i)) 
    
    def test_func2(self):
        self.assertTrue(my_func2("yes"))
        with self.assertRaises(ValueError):
            my_func2("nononono")

suite = unittest.TestSuite()
suite.addTest(TestFunc('test_func1'))
unittest.TextTestRunner().run(suite)


