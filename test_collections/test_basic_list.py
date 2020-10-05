import unittest
from fun_with_collections.basic_list import make_list
from unittest.mock import patch

class TestList(unittest.TestCase):
    @patch('fun_with_collections.basic_list.get_input', return_value='5.0')
    def test_make_list(self, input):
        self.assertEqual(make_list(), ['5.0', '5.0', '5.0'])

if __name__ == '__main__':
    unittest.self