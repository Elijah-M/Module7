import unittest
from fun_with_collections.basic_list_exception import make_list
from unittest.mock import patch

class TestList(unittest.TestCase):
    @patch('fun_with_collections.basic_list_exception.get_input', return_value='ab')
    def test_make_list_non_numeric(self, input):
        with self.assertRaises(ValueError):
            make_list()

   def test_make_list_below_range(self, input):
       with self.assertRaises(ValueError):
           make_list()

    def test_make_list_above_range(self, input):
        with self.assertRaises(ValueError):
            make_list()

if __name__ == '__main__':
    unittest.self