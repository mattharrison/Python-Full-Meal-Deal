import unittest

class TestDicts(unittest.TestCase):
    def test_dicts(self):
        """
        A basic introduction to dictionaries
        """
        # Create the variable ``room2names`` and assign to an empty dict
        #**************************************************

        self.assertEquals(room2names, {})

        # map the string 'room1' to an empty list
        #**************************************************

        self.assertEquals(room2names['room1'], [])
        self.assert_('room1' in room2names)

        # map the string 'room2' to ['fred', 'hermione']
        #**************************************************

        self.assertEquals(room2names['room2'], ['fred', 'hermione'])

        # add 'harry' to the list in 'room1'

        self.assertEquals(room2names['room1'], ['harry'])

        # use ``setdefault`` to assign the contents of 'room3'
        # to variable ``empty``
        
        self.assertEquals(room2names['room3'], [])
        self.assertEquals(empty, [])

        # use ``in`` to see if 'room4' is there.
        # assign the results to variable ``d``

        self.assertEquals(d, False)

        # use ``del`` to remove 'room1'

        self.assert_('room1' not in room2names)
        
if __name__ == '__main__':
    unittest.main()
