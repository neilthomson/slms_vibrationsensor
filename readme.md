# SLMS Train Sensor

A software toolkit for the Raspberry Pi Sense Hat to enable us to detect when a
train is passing overhead.

Currently doesn't do that and simply displays the accelerometer data on the RGB
matrix display.

Clone the repo then simply run
```shell
$ python sensetrain.py high
```

To enable high sensitivity readings to be displayed.

## Data acquisiton tests

From picking it up and shaking it around:  

![alt text](images/shaking-it.png "Picking it up and shaking it around data")

From knocking on the table next to it:  

![alt text](images/knocking-it.png "Knocking on the table next to it data")

Accelerometer data displayed on the RGB matrix

![alt text](images/rgb-matrix.jpg "RGB matrix accelerometer data")

## Bill of materials (BOM)  

* [Raspberry Pi] (http://bit.ly/2nyBJ3V)

* [Raspberry Pi Sense Hat] (http://bit.ly/2nE67L2)

## Alternative BOM

A solution based on the ubiquitous NodeMCU (ESP8266 arduino compatible wifi enabled board) with an accelerometer module should come in ten times cheaper - code not yet written.

* [NodeMCU] (http://ebay.eu/2nS6hzd)

* [Accelerometer module] (http://ebay.eu/2nEpPqb)
