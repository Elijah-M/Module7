import unittest
from fun_with_collections.sort_and_search_array import search_array
from fun_with_collections.sort_and_search_array import make_array
from fun_with_collections.sort_and_search_array import sort_array
from unittest.mock import patch

class Testarray(unittest.TestCase):
    @patch('fun_with_collections.sort_and_search_array.search_array', return_value=2)
    def test_search_array(self, input):
        x = make_array()
        self.assertEqual(search_array(x), 2)
"""
    @patch('fun_with_collections.sort_and_search_array.sort_array', return_value=[3.0,45.0,6.0])
    def test_sort_array(self, input):
        x = make_array()
        self.assertEqual(sort_array(x), [3.0,6.0, 45.0])
"""
if __name__ == '__main__':
    unittest.self