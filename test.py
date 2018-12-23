#!/usr/bin/env python3
import unittest
from unittest.mock import MagicMock, patch
import dryer_monitor

class TestDryerMonitor(unittest.TestCase):
    @patch('dryer_monitor.GPIO')
    def test_happy_path(self, mock_gpio):
        dryer_monitor.SENSING_SECONDS_MAX = 3
        mock_gpio.input.side_effect = [
                False, False, True, True, True, True, False
                ]

        state = dryer_monitor.Waiting()
        for i in range(0, 8):
            state = state.next()

    @patch('dryer_monitor.GPIO')
    def test_stops_before_drying(self, mock_gpio):
        dryer_monitor.SENSING_SECONDS_MAX = 3
        mock_gpio.input.side_effect = [
                False, False, True, True, False
                ]

        state = dryer_monitor.Waiting()
        for i in range(0, 5):
            state = state.next()

if __name__ == '__main__':
    unittest.main()
