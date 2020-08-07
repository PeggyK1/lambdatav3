import unittest


class LambdataV3Test(unittest.TestCase):
    """Testing Instantiation of lambdatv3"""

    def test_nan(self):
        """Test the nan values on the test dataset"""

        n = report_nan(test)
        self.assertEqual(n, 4)
