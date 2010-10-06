import types
import unittest

class TestClosures(unittest.TestCase):
    def test_closure(self):
        # Closure
        # Create a function ``echo_creator`` that returns a function that returns what was passed into it
        # ================================
        
        echo = echo_creator()
        self.assert_(isinstance(echo, types.FunctionType))
        self.assertEquals(echo(5), 5)
        self.assertEquals(echo("foo"), "foo")

        # Closure 2
        # Create a function ``mult_factory`` that accepts
        # a number and returns a function that multiples its
        # input by that number
        # ================================
        
        mult5 = mult_factory(5)
        self.assert_(isinstance(mult5, types.FunctionType))
        self.assertEquals(mult5(5), 25)
        self.assertEquals(mult5("f"), "fffff")


if __name__ == '__main__':
    unittest.main()
