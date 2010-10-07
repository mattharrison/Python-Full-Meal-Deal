import StringIO
import sys
import types
import unittest

class TestDecorators(unittest.TestCase):
    def test_decorators(self):
        # Decorators
        # create a decorator, ``noisy`` that
        # prints "before" before invoking the
        # wrapped function and "after", after
        # invoking it
        # ================================
        
        @noisy
        def nothing():
            print 'middle'

        old_stdout = sys.stdout
        sys.stdout = StringIO.StringIO()
        nothing()
        captured = sys.stdout
        sys.stdout = old_stdout
        self.assertEquals(captured.getvalue(), 'before\nmiddle\nafter\n')
        self.assert_(isinstance(noisy, types.FunctionType))
        self.assert_(nothing.func_closure is not None)

        # Good decorators
        # write a decorator ``good_pointless`` that
        # updates the wrapped ``__doc__`` and ``func_name``
        # and just calls the function
        # ================================
        
        @good_pointless
        def nothing2():
            """doc string"""
            pass

        self.assertEquals(nothing2.__doc__, 'doc string')
        self.assertEquals(nothing2.func_name, 'nothing2')

        # Parameterized Decorators
        # write a decorator ``times_n`` that takes a
        # number (n) and multiples the result of the
        # function it is wrapping by that number (n).
        # ================================
        

        @times_n(3)
        def echo(txt):
            return txt
        
        self.assertEquals(echo('f'), 'fff')
        self.assertEquals(echo(4), 12)



if __name__ == '__main__':
    unittest.main()
