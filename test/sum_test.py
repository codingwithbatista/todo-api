import unittest
from unittest.mock import MagicMock


from sum import Sum


class TestSum(unittest.TestCase):
    def test_sum(self):
        sum = Sum()
        sum.add_one = MagicMock(name='add_one')
        sum.add_one.return_value = 5
        result: int = sum.sum(4, 3)
        self.assertEqual(result, 5)
        sum.add_one.assert_called_with(4, 3)

if __name__ == '__main__':
    unittest.main()
