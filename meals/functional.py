import types
import unittest

class TestFunctional(unittest.TestCase):
    def test_functional(self):
        # Lambda
        # create a lambda statement that adds 2 to it's input
        # assign the statement to a variable named ``add_2``
        # ================================
        
        self.assert_(isinstance(add_2, types.LambdaType))
        self.assertEquals(add_2(4), 6)

        # Lamda 2
        # Create an ``is_odd`` lambda statement,
        # that returns True if the input is odd
        # ================================
        
        self.assert_(isinstance(is_odd, types.LambdaType))
        self.assertEquals(is_odd(5), True)
        self.assertEquals(is_odd(4), False)


        # Map
        # Create a list ``digits`` with the numbers from 0 to 9
        # Create a new list ``two_more`` from digits by
        # mapping ``add_2`` to the elements of digits
        # ================================
        
        self.assertEquals(digits, range(0, 10))
        self.assertEquals(two_more, range(2,12))

        # Reduce
        # Add the values of digits by using
        # ``reduce`` with the ``operator.add``
        # function, store the result in ``digit_sum``
        # ================================
        
        self.assertEquals(digit_sum, 45)

        # Filter
        # use ``filter`` to get the odd digits of
        # ``two_more``, store results in ``two_odd``
        # ================================
        
        self.assertEquals(two_odd, [3, 5, 7, 9, 11])



if __name__ == '__main__':
    unittest.main()
