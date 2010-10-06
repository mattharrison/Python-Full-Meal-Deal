import unittest

class TestLists(unittest.TestCase):
    def test_lists(self):
        """
        A basic introduction to lists
        """
        # Create the variable ``a`` and assign to an empty list
        # **************************************************

        self.assertEquals(a, [])

        # Append 'fred' and 'arnold' to ``a``
        # **************************************************

        self.assertEquals(a, ['fred', 'arnold'])

        # Sort ``a``
        # **************************************************

        self.assertEquals(a, ['arnold', 'fred'])

        # ``extend`` the list ``a`` with ['barney', 'george']
        # **************************************************

        self.assertEquals(a, ['arnold', 'fred', 'barney', 'george'])

        # create a variable ``idx`` with the index of 'barney' in ``a`` using list methods.
        # **************************************************

        self.assertEquals(idx, 2)
        

if __name__ == '__main__':
    unittest.main()
