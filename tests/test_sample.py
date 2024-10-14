import unittest

class TestZooTicketing(unittest.TestCase):
    
    def test_sample(self):
        # A simple test that always passes
        self.assertEqual(1, 1)

    def test_fail_example(self):
        # A test that will fail (you can comment this out if you don't want to see a failure)
        self.assertEqual(1, 2)

if __name__ == '__main__':
    unittest.main()
