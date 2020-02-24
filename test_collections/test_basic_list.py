import unittest
from unittest.mock import patch
from fun_with_collections import basic_list as topic1

class TestList(unittest.TestCase):
    @patch('fun_with_collections.topic1.get_input',return_vaule='5')
    def test_make_list(self,input):
        self.assertEqual(topic1.make_list(),[5,5,5])