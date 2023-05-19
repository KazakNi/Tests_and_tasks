import unittest
from hw2 import CustomClass, CustomList


class TestMeta(unittest.TestCase):

    def setUp(self):
        self.sample_list_1 = CustomList(20, 4)
        self.sample_list_2 = CustomList(10, 5, 2)
        self.metasample = CustomClass

    def test_custom_list(self):
        result = self.sample_list_1 - self.sample_list_2
        return self.assertEqual(result, [10, -1])

    def test_metaclass_work(self):
        with self.assertRaises(AttributeError):
            self.metasample.lol()


if __name__ == '__main__':
    unittest.main()