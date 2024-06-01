from unittest import TestCase
from unittest.mock import MagicMock
from candidates_finder.service.report import Report


class TestReport(TestCase):
    def setUp(self):
        self.spark = MagicMock()
        self._report = Report()
        self._report._spark = MagicMock()
        self._report._configure_logger = MagicMock()

    def test_configure_logger(self):
        self._report._configure_logger()
        self.assertTrue(hasattr(self._report, '_logger'))
