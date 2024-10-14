import unittest
from unittest.mock import patch
from zoo_ticketing import main

class TestIntegration(unittest.TestCase):

    @patch('builtins.input', side_effect=['adult', '2', 'no'])
    def test_adult_ticket_purchase(self, mock_input):
        """Simulate buying 2 adult tickets and verify the output"""
        with patch('builtins.print') as mock_print:
            main()
            # Check that the summary and final cost are printed
            mock_print.assert_any_call("Total Cost: $40\n")

if __name__ == '__main__':
    unittest.main()
