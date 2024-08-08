import unittest
from unittest.mock import patch
from io import StringIO
import sys

class TestEnergyCalculation(unittest.TestCase):
    @patch('builtins.input', return_value='10')  # Mocking input to simulate 'm: 10
    def test_energy_output(self, mock_input):
        # Redirect stdout to capture prints
        captured_output = StringIO()
        sys.stdout = captured_output
        
        # Execute script
        exec(open("03-einstein/einstein.py").read())
        
        sys.stdout = sys.__stdout__
        
        # Get the output and strip any extra newlines or spaces
        output = captured_output.getvalue().strip()
        
        # Check if the output is the expected string
        expected_output = "E: 900000000000000000"
        self.assertEqual(output, expected_output, f"Expected '{expected_output}', but got '{output}'")

if __name__ == '__main__':
    unittest.main()
