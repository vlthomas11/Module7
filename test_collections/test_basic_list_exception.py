import unittest


class TestListElements(unittest.TestCase):
    def setUp(self):
        self.initial_list = [1, 3, 5]
        self.expected = [1, 4, 5]

    def tearDown(self):
        self.initial_list = []
        self.expected = []

    def test_count_eq(self):
        """Will succeed"""
        self.assertCountEqual(self.initial_list, self.expected)

    def test_list_eq(self):
        """Will fail"""
        self.assertListEqual(self.initial_list, self.expected)


if __name__ == '__main__':
    unittest.main()

