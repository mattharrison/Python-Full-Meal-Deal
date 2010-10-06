import unittest

class TestClass(unittest.TestCase):
    def test_classes(self):
        # Create a class called ``Echoer``
        # Accept a name in the constructor
        # ================================
        
        e = Echoer('matt')
        self.assert_(isinstance(e, Echoer))

        # Add a method ``say`` to Echoer that
        # accepts a string and returns:
        # ${name} said, "${string}"
        # ================================
        
        self.assertEquals(e.say('hi'), 'matt said, "hi"')

        # Subclass - create a subclass ``Screamer``
        # of ``Echoer`` that has the same constructor
        # but ``say`` returns:
        # ${name} screamed, "${string.upper()}"
        # ================================
        
        s = Screamer("Frank")
        self.assertEquals(s.say('later'), 'Frank screamed, "LATER"')


if __name__ == '__main__':
    unittest.main()


        
        
