'''
This module contains the test cases for the utility functions.
'''

import unittest
import os
from core.utils import check_file_exists

class TestUtils(unittest.TestCase):
    """Test cases for the utility functions.
    
    Functions:
        test_check_file_exists(self): Test the check_file_exists function.
    """

    def setUp(self):
        self.existing_file = "tests/files/existing_file.txt"
        self.non_existing_file = "tests/files/non_existing_file.txt"

        # Create a dummy file for testing
        with open(self.existing_file, 'w', encoding='utf-8') as f:
            f.write("Test content")

    def test_check_file_exists(self):
        """
        Test the check_file_exists function."""
        # Test with an existing file
        self.assertTrue(check_file_exists(self.existing_file))

        # Test with a non-existing file
        self.assertFalse(check_file_exists(self.non_existing_file))

    def tearDown(self):
        # Clean up the dummy file after tests
        if os.path.exists(self.existing_file):
            os.remove(self.existing_file)

if __name__ == "__main__":
    unittest.main()
