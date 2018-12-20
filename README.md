# Dryer Monitor

This script is designed to run on a Raspberry Pi.  It reads input from a vibration sensor attached to a GPIO pin, using the state of the sensor to monitor whether a clothes dryer is running or not.  If the dryer stops, the script attempts to send a text to a given phone number via AWS' SNS API.

## Prerequisites
* Raspberry Pi with an attached SW-420 vibration sensor
* Preconfigured AWS credentials

## Testing
`./test.py`

## Running
`./dryer_monitor.py <phone number>`
