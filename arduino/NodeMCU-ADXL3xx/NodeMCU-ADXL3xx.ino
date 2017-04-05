
/*
 ADXL3xx

 Reads an Analog Devices ADXL3xx accelerometer and communicates the
 acceleration to the computer.  The pins used are designed to be easily
 compatible with the breakout boards from Sparkfun, available from:
 http://www.sparkfun.com/commerce/categories.php?c=80

 http://www.arduino.cc/en/Tutorial/ADXL3xx

 The circuit:
 analog 0: accelerometer self test
 analog 1: z-axis
 analog 2: y-axis
 analog 3: x-axis
 analog 4: ground
 analog 5: vcc

 created 2 Jul 2008
 by David A. Mellis
 modified 30 Aug 2011
 by Tom Igoe

 This example code is in the public domain.

*/

/*
 * Modifications for the https://github.com/neilthomson/slms_vibrationsensor arduino flavour
 * Using the NodeMCU with one single analogue input on NodeMCU pin A0
 * Better option would be multiplex but assuming we want to measure any disturbance, single 
 * channel should do for now.
 * See https://raw.githubusercontent.com/dsikar/tweet-guitar-nano/master/images/TweetGuitarPinouts.png
 * for NodeMCU pinout.
 */
// these constants describe the pins. They won't change:
// const int groundpin = 18;             // analog input pin 4 -- ground
// const int powerpin = 19;              // analog input pin 5 -- voltage
// NodeMCU will output 3V or thereabouts as reference voltage on D1 so should work with ADXL335 module
const int groundpin = 16;             // analog input pin 4 -- ground NB pin D0 on NodeMCU
const int powerpin = 5;              // analog input pin 5 -- voltage NB pin D1 on NodeMCU
const int xpin = A0;                  // x-axis of the accelerometer
const int ypin = A0;                  // y-axis
const int zpin = A0;                  // z-axis (only on 3-axis models)

void setup() {
  // initialize the serial communications:
  Serial.begin(9600);

  // Provide ground and power by using the analog inputs as normal
  // digital pins.  This makes it possible to directly connect the
  // breakout board to the Arduino.  If you use the normal 5V and
  // GND pins on the Arduino, you can remove these lines.
  pinMode(groundpin, OUTPUT);
  pinMode(powerpin, OUTPUT);
  digitalWrite(groundpin, LOW);
  digitalWrite(powerpin, HIGH);
}

void loop() {
  // print the sensor values:
  Serial.print(analogRead(xpin));
  // print a tab between values:
  Serial.print("\t");
  Serial.print(analogRead(ypin));
  // print a tab between values:
  Serial.print("\t");
  Serial.print(analogRead(zpin));
  Serial.println();
  // delay before next reading:
  delay(100);
}
