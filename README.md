# spider-arms

## Installation

``` pip install -r requirements.txt```

## Connect to JoyCon

Type ``sudo bluetoothctl`` then press enter and input the administrator password (the default password is raspberry).

Next, enter ``agent on`` and press enter. Then type ``default-agent`` and press enter.

Type ``scan on`` and press enter one more time. The unique addresses of all the Bluetooth devices around the Raspberry Pi will appear.

To pair the device, type ``pair [device Bluetooth address]``.

Source: <https://www.cnet.com/tech/computing/how-to-setup-bluetooth-on-a-raspberry-pi-3/>

## GPIO Pins

The servo signal should be connected to __GPIO14__ or __Pin No. 8__

![GPIO Pin Diagram](https://www.bigmessowires.com/wp-content/uploads/2018/05/Raspberry-GPIO.jpg)

Source: <https://www.bigmessowires.com/2018/05/26/raspberry-pi-gpio-programming-in-c/>