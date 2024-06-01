from unittest import TestCase
from unittest.mock import patch, MagicMock
from candidates_finder.model.read import Read


class TestRead(TestCase):
    def setUp(self):
        self._followers_list = [
            {"url": "https://example.com/follower_a"},
            {"url": "https://example.com/follower_b"}
        ]
        self._read = Read()
        self._response_mock = {
            "follower1": "info1",
            "follower2": "info2"
        }
        self._mock_response = MagicMock()
        self._mock_response.json.return_value = self._response_mock

    @patch('candidates_finder.model.read.requests')
    def test_get_followers_request(self, mock_requests):
        mock_requests.get.return_value = self._mock_response

        result = self._read.get_followers_request()

        self.assertIsInstance(result, dict)

    def test_get_followers_info_list(self):
        result = self._read.get_followers_info_list(self._followers_list)
        self.assertIsInstance(result, list)

    @patch('candidates_finder.model.read.requests')
    def test_get_followers_info_request(self, mock_requests):
        mock_requests.get.return_value = self._mock_response

        follower_url = 'https://example.com/follower'
        result = self._read.get_followers_info_request(follower_url)

        self.assertIsInstance(result, dict)
