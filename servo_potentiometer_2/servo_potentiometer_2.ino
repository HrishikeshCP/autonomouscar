#include <Servo.h>  // add servo library

Servo servo;  // create servo object to control a servo

int pot = 0;  // analog pin used to connect the potentiometer
int temp;     // variable to read the value from the analog pin

void setup() {
  Serial.begin(9600);       // Begin serial communication
  servo.attach(2);          //D4
  servo.write(0);
}

void loop() {
  temp = analogRead(pot);            // reads the value of the potentiometer (value between 0 and 1023)
  Serial.println(temp);
  temp = map(temp, 0, 1023, 0, 180); // scale it to use it with the servo (value between 0 and 180)
//  temp = 270;
  servo.write(temp);                 // sets the servo position according to the scaled value
  delay(50);                         // waits for the servo to get there
}
