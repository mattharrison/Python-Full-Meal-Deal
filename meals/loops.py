import unittest

class TestLoops(unittest.TestCase):
    def test_loops(self):
        # Using ``range``
        # Write variable ``a`` that holds 0 to 5 (use the ``range`` function)
        # ================================
        
        self.assertEquals(a, [0,1,2,3,4,5])

        # ``range`` 2
        # Create variable ``b`` that holds from 3 to 11
        # ================================
        
        self.assertEquals(b, [3,4,5,6,7,8,9,10,11])

        # Write a function ``even`` that takes a list of
        # number and returns a list of even numbers
        # ================================
        
        self.assertEquals(even(a), [0, 2, 4])
        self.assertEquals(even(b), [4, 6, 8, 10])

        # Write a function ``even_index`` that takes a list
        # of numbers and returns those that are in an even
        # index position
        # ================================
        
        self.assertEquals(even_index(a), [0, 2, 4])
        self.assertEquals(even_index(b), [3, 5, 7, 9, 11])


if __name__ == '__main__':
    unittest.main()
        
