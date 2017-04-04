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

* [Raspberry Pi] ()

* [Raspberry Pi Sense Hat] ()
