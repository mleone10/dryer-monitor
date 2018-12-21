#!/usr/bin/env python3
import unittest
from unittest.mock import patch
import dryer_monitor

class TestDryerMonitor(unittest.TestCase):
    @patch('dryer_monitor.RPi')
    @patch('dryer_monitor.RPi.GPIO')
    def test_debug(self, mock_gpio, mock_rpi):
        mock_gpio.input.return_value = True
        self.assertEqual(dryer_monitor.main(), True)

if __name__ == '__main__':
    unittest.main()
