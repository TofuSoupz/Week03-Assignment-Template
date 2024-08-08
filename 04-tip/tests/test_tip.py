import unittest
from unittest.mock import patch
from io import StringIO
import sys

class TestTipCalculator(unittest.TestCase):

    @patch('builtins.input', side_effect=['100.0', '15.0'])  # Mocking inputs
    def test_tip_output(self, mock_input):
        # Redirect stdout to capture prints
        captured_output = StringIO()
        sys.stdout = captured_output

        # Execute script
        exec(open("04-tip/tip.py").read())

        sys.stdout = sys.__stdout__

        # Get the output and strip any extra newlines or spaces
        output = captured_output.getvalue().strip()

        # Check if the output is the expected string
        expected_output = "Leave $15.00"
        self.assertEqual(output, expected_output, f"Expected '{expected_output}', but got '{output}'")

if __name__ == '__main__':
    unittest.main()
