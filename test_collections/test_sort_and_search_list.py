import unittest
from fun_with_collections.sort_and_search_list import search_list
from fun_with_collections.sort_and_search_list import make_list
from unittest.mock import patch

class TestList(unittest.TestCase):
    @patch('fun_with_collections.sort_and_search_list.search_list', return_value=3)
    def test_search_list(self, input):
        x = make_list()
        self.assertEqual(search_list(x), 3)

if __name__ == '__main__':
    unittest.self
