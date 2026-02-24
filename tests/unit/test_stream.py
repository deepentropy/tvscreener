import unittest
from unittest.mock import MagicMock, patch

from tvscreener import StockScreener


class TestStream(unittest.TestCase):
    @patch.object(StockScreener, "get")
    def test_stream_max_iterations(self, mock_get):
        mock_get.return_value = MagicMock()
        ss = StockScreener()
        results = list(ss.stream(interval=1.0, max_iterations=3))
        self.assertEqual(len(results), 3)
        self.assertEqual(mock_get.call_count, 3)

    @patch.object(StockScreener, "get")
    @patch("tvscreener.core.base.time.sleep")
    def test_stream_minimum_interval(self, mock_sleep, mock_get):
        mock_get.return_value = MagicMock()
        ss = StockScreener()
        # Even if user passes 0.1, it should use minimum of 1.0
        list(ss.stream(interval=0.1, max_iterations=2))
        # Should sleep with minimum interval of 1.0
        mock_sleep.assert_called_with(1.0)

    @patch.object(StockScreener, "get")
    @patch("tvscreener.core.base.time.sleep")
    def test_stream_callback(self, mock_sleep, mock_get):
        mock_df = MagicMock()
        mock_get.return_value = mock_df
        callback = MagicMock()

        ss = StockScreener()
        list(ss.stream(interval=1.0, max_iterations=2, on_update=callback))

        self.assertEqual(callback.call_count, 2)
        callback.assert_called_with(mock_df)

    @patch.object(StockScreener, "get")
    @patch("tvscreener.core.base.time.sleep")
    def test_stream_handles_errors(self, mock_sleep, mock_get):
        mock_get.side_effect = [Exception("API Error"), MagicMock()]
        ss = StockScreener()
        results = list(ss.stream(interval=1.0, max_iterations=2))
        self.assertEqual(len(results), 2)
        self.assertIsNone(results[0])  # First result is None due to error

    @patch.object(StockScreener, "get")
    @patch("tvscreener.core.base.time.sleep")
    def test_stream_no_sleep_after_last_iteration(self, mock_sleep, mock_get):
        mock_get.return_value = MagicMock()
        ss = StockScreener()
        list(ss.stream(interval=1.0, max_iterations=1))
        # Should not sleep after the last iteration
        mock_sleep.assert_not_called()

    @patch.object(StockScreener, "get")
    @patch("tvscreener.core.base.time.sleep")
    def test_stream_custom_interval(self, mock_sleep, mock_get):
        mock_get.return_value = MagicMock()
        ss = StockScreener()
        list(ss.stream(interval=5.0, max_iterations=2))
        # Should sleep with the custom interval
        mock_sleep.assert_called_with(5.0)


if __name__ == "__main__":
    unittest.main()
