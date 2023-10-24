import unittest

import HtmlTestRunner

from test_cases.test_negative_login import TestNegativeLogin
from test_cases.test_positive_login import TestPositiveLogin


class TestLoginSuite(unittest.TestCase):
    def test_suite(self):
        test_suite = unittest.TestSuite()
        test_suite.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(TestPositiveLogin),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestNegativeLogin)
        ])
#Terminal: pip install html-testRunner

        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=False,
            report_title="Login Page Test Report",
            report_name="Test Results"
        )

        runner.run(test_suite)
