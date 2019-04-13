import unittest

from process_list.process_list import process_list


class TestList(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(process_list(
            [1, 2, 8, 9, 3, 7, -11, -12, 4, 6, -13, 5, -14, -15])[0], 45)

    def test_negative_count(self):
        self.assertEqual(process_list(
            [1, 2, 8, 9, 3, 7, -11, -12, 4, 6, -13, 5, -14, -15])[1], 5)

    def test_wrong_input(self):
        raised = False
        try:
            process_list("some_wrong_input")
        except:
            raised = True
        self.assertFalse(raised, 'Exception raised')


if __name__ == "__main__":
    unittest.main()
    print("Everything passed")
