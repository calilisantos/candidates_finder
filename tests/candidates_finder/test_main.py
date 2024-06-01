from candidates_finder.main import Main
from unittest.mock import patch


class TestMain():
    @patch(
        "candidates_finder.main.Main.__init__",
        return_value=None
    )
    @patch("candidates_finder.main.Main.run")
    def test_run(self, mock_run, mock_init):
        main = Main()
        main.run()

        mock_init.assert_called_once()
        mock_run.assert_called_once()
