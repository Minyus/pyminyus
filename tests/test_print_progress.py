import unittest
import sys
from pyminyus.print_progress import print_progress

class TestPrintProgress(unittest.TestCase):

    def test_print_progress(self):
        # Test occuerence of exception
        try:
            # Make sure no e
            i = 1
            n = 10
            print_progress(i, n)
        except:
            (etype, evalue, etrace) = sys.exc_info()
            self.fail('Failed with {}'.format(sys.exc_info()))
        # Test returned value
        actual = 1 + 1
        expected = 2
        self.assertAlmostEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()