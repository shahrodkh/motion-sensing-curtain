#include <AccelStepper.h>
/*
create a stepper motor with driver
pin 8 -> pul
pin 9 -> dir
*/

AccelStepper stepper(AccelStepper::DRIVER, 8, 9);

const int stepSize = 2; // check microstep setting on driver e.g. 1/2, 1/8, etc.

const int stepMax = 600; // total length of curtain

const int camMax = 1280; // camera resolution

const int maxSpeed = 1500.0; // maximum speed

const int acceleration = 700.0; // max acceleration

void setup() {
  Serial.begin(9600);
  stepper.setMaxSpeed(maxSpeed);
  stepper.setAcceleration(acceleration);
}

void loop() {
  int val = 0;
  int temp1 = 0;
  int temp2 = 0;
  if (Serial.available()) {
    temp1 = Serial.parseInt();
    if (temp1 >= 0 && temp1 <= camMax) {
      temp2 = map(temp1, 0, camMax, 0, stepMax);
      if (temp2 >= 0 && temp2 <= stepMax) {
        val = temp2;
      }
    }
  }

  stepper.runToNewPosition(val * stepSize);
}
