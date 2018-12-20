#!/usr/bin/env python3
import unittest
import dryer_monitor

class TestDryerMonitor(unittest.TestCase):
    def test_debug(self):
        self.assertEqual(dryer_monitor.main(True), True)

if __name__ == '__main__':
    unittest.main()
