import unittest

class TestVariables(unittest.TestCase):
    def test_variables(self):
        """
        This is a test method you will need to fill in the content
        where it says and then run it (ie ``python variables.py``).
        If it doesn't complain, then you pass!
        """
        # create a the variable ``a`` and assign it to a float (5.0)
        # **************************************************

        self.assert_(isinstance(a, float))

        # re-assign ``a`` to 6
        # **************************************************
        
        self.assertEqual(a, 6)
        self.assert_(isinstance(a, int))

        # create a variable ``b`` assigned to "hello"
        # **************************************************

        self.assertEqual(b, "hello")
        self.assertTrue(isinstance(b, str))
        

if __name__ == '__main__':
    unittest.main()
