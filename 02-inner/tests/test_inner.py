import unittest
from unittest.mock import patch
from io import StringIO
import sys

class TestToLowerOutput(unittest.TestCase):
    @patch('builtins.input', return_value='HELLO WORLD')
    def test_output_is_lowercase(self, mock_input):
        
        # Redirect stdout to capture prints
        captured_output = StringIO()
        sys.stdout = captured_output
        
        # Execute script
        exec(open("02-inner/inner.py").read())
        sys.stdout = sys.__stdout__
        
        # Get the output 
        output = captured_output.getvalue().strip()
        
        # Check if the output is lowercase
        self.assertTrue(output.islower(), "The output should be all lowercase")

if __name__ == '__main__':
    unittest.main()
