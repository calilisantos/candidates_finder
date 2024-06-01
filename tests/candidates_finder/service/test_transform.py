from unittest import TestCase
from unittest.mock import MagicMock
from candidates_finder.service.transform import Transform


class TestTransform(TestCase):
    def setUp(self):
        self._spark = MagicMock()
        self._followers_list = ["João", "Maria", "José"]
        self._transform = Transform(self._spark, self._followers_list)

    def test_read_followers_list(self):
        self._transform._read_followers_list = MagicMock()
        self._transform._read_followers_list()

        self._transform._read_followers_list.assert_called_once()

    def test_transform_date_column(self):
        self._transform._transform_date_column = MagicMock()
        self._transform._transform_date_column()

        self._transform._transform_date_column.assert_called_once()

    def test_transform_company_column(self):
        self._transform._transform_company_column = MagicMock()
        self._transform._transform_company_column()

        self._transform._transform_company_column.assert_called_once()

    def test_save_to_csv(self):
        self._transform._save_to_csv = MagicMock()
        self._transform._save_to_csv()

        self._transform._save_to_csv.assert_called_once()

    def test_run(self):
        self._transform._read_followers_list = MagicMock()
        self._transform._transform_date_column = MagicMock()
        self._transform._transform_company_column = MagicMock()
        self._transform._save_to_csv = MagicMock()

        self._transform.run()

        self._transform._read_followers_list.assert_called_once()
        self._transform._transform_date_column.assert_called_once()
        self._transform._transform_company_column.assert_called_once()
        self._transform._save_to_csv.assert_called_once()
