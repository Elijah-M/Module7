import unittest
from fun_with_collections import basic_list
from unittest.mock import patch

class TestList(unittest.TestCase):
    @patch('fun_with_collections.get_input', return_value='1')
    def test_make_list(self, input):
        self.assertEqual(basic_list(), [5, 5, 5])

if __name__ == '__main__':
    unittest.self