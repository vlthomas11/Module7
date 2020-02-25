import unittest
from unittest.mock import patch
import fun_with_collections.basic_list_exception as topic1


class TestList(unittest.TestCase):
    @patch('fun_with_collections.basic_list_exception.get_input', return_value='ab')  # patch function for input
    def test_make_list_non_numeric(self, input):  # pass input
        with self.assertRaises(ValueError):  # this is familiar
            topic1.make_list()


