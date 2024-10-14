import unittest

class TestSample(unittest.TestCase):

    def test_always_passes(self):
        self.assertTrue(True)

    def test_always_fails(self):
        self.assertFalse(False)

if __name__ == '__main__':
    unittest.main()
