import unittest
from utils import algorithm


class AlgorithmTester(unittest.TestCase):

    def test_algorithm_on_first_data_example_result(self):
        self.assertEqual(algorithm('data_example_1.txt'), 4)

    def test_algorithm_on_second_data_example_result(self):
        self.assertEqual(algorithm('data_example_2.txt'), 6)

    def test_algorithm_on_third_data_example_result(self):
        self.assertEqual(algorithm('data_example_3.txt'), 0)

    def test_algorithm_on_third_data_example_result(self):
        self.assertEqual(algorithm('example_4.txt'), 0)


if __name__ == '__main__':
    unittest.main()
