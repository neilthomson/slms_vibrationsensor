#!/usr/bin/env python

"""
Train detector
"""

import sys, signal, time, csv
from math import fabs
from datetime import datetime
from sense_hat import SenseHat


class TrainSensor(SenseHat):
    """
    Extension of SenseHat class containing utilities and methods that enable us
    to make a Train Sensor.
    """
    def __init__(self):
        super(TrainSensor, self).__init__()
        self.prev_accel_values = self.accel_raw


    @staticmethod
    def map_to_new_range(value, in_min, in_max, out_min, out_max):
        """
        Re-maps a number from one range to another.
        """
        return (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


    @staticmethod
    def map_data_for_matrix(data, min_range, max_range):
        """
        Maps values to 0-8 for display on the RGB display matrix on the sense
        hat

        data is a list of values,
        min max is the range of accelerometer values to map.

        Returns a list of values between 0-7 for x, y and z
        """

        col_heights = []
        for value in data:
            col_heights.append(TrainSensor.map_to_new_range(value, min_range, max_range, 0, 7))

        return col_heights


    def save_accel_raw_to_csv(self, sample_count, sample_rate):
        """
        Writes sample_count number of samples at sample_rate to a csv file in the
        local directory with a datetime stamped name 'acceldata_' in the format
        acceldata_Day_Month_[monthDay]_[hour]-[mins]-[secs]_[year].csv
        """

        now_stamp = datetime.now().ctime()
        now_stamp = now_stamp.replace(":", "-")
        now_stamp = now_stamp.replace(" ", "_")

        with open('acceldata_{}.csv'.format(now_stamp), 'wb') as csvfile:
            field_names = ['x', 'y', 'z']
            accel_data_writer = csv.DictWriter(csvfile, fieldnames=field_names)
            accel_data_writer.writeheader()
            count = 0
            while count < sample_count:
                accel_data_writer.writerow(self.accel_raw)
                time.sleep(1.0/float(sample_rate))
                count += 1


    def calc_accel_diff(self):
        """
        Calculates the difference between current and previous raw accelerometer
        values and returns a list for x, y and z
        """
        accel_raw_vals = self.accel_raw
        xyz_diffs = []

        for key, value in accel_raw_vals.iteritems():
            diff = fabs(self.prev_accel_values[key] - value)
            xyz_diffs.append(diff)

        self.prev_accel_values = accel_raw_vals

        return xyz_diffs

    def display_accel_data(self, xyz_heights):
        """
        Displays X Y Z accelerometer on the RGB display in Audio Spectral Analyser
        fashion. Two rows are used per axis, in the order of x y z. X is red, Y is
        green, z is blue. The last two rows are blank.

        xyz_heights is a list of ints between 0-7 for x, y and z
        """
        display_pixels = self.get_pixels()

        for row in range(8):
            for col in range(8):
                # Set X pixels
                if row < 2:
                    if col <= xyz_heights[0]:
                        display_pixels[row*8+col] = [255, 0, 0]
                    else:
                        display_pixels[row*8+col] = [0, 0, 0]
                # Set Y pixels
                if (row >= 2) and (row < 4):
                    if col <= xyz_heights[1]:
                        display_pixels[row*8+col] = [0, 255, 0]
                    else:
                        display_pixels[row*8+col] = [0, 0, 0]
                # Set Z pixels
                if (row >= 4) and (row < 6):
                    if col <= xyz_heights[2]:
                        display_pixels[row*8+col] = [0, 0, 255]
                    else:
                        display_pixels[row*8+col] = [0, 0, 0]

        self.set_pixels(display_pixels)


def main():
    """
    The main loop
    """
    from sys import argv

    sensitivity = argv[1]
    signal.signal(signal.SIGINT, signal.default_int_handler)

    if "high" in sensitivity:
        min_range, max_range = 0, 0.1
    if "medium" in sensitivity:
        min_range, max_range = 0, 1
    if "low" in sensitivity:
        min_range, max_range = 0, 2.5

    sensor = TrainSensor()
    sensor.set_imu_config(False, False, True) #Enable only the Accelerometer

    try:
        while True:
            xyz_diffs = sensor.calc_accel_diff()
            col_heights = sensor.map_data_for_matrix(xyz_diffs, min_range, max_range)
            sensor.display_accel_data(col_heights)
    except KeyboardInterrupt:
        sensor.clear((255, 0, 0))
        time.sleep(0.3)
        sensor.clear()
        sys.exit(0)


if __name__ == "__main__":
    main()
