import unittest
from io import StringIO #
from unittest.mock import patch #We're using unittest.mock.patch to capture the output printed to sys.stdout.

#from ui.uiUtils import display_map  # Adjust the import path based on your project structure

class TestDisplay(unittest.TestCase):
    
    def setUp(self):
        # Set up any common test data or configurations here
        # For example, create a sample empty game map
        return

if __name__ == '__main__':
    unittest.main()