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

const int maxSpeed = 1500; // maximum speed

const int acceleration = 700; // max acceleration

const int numPartition = 20;  // number of partitions

const int partitionVal = stepMax / (numPartition-1);

void setup() {
  Serial.begin(9600);
  stepper.setMaxSpeed(maxSpeed);
  stepper.setAcceleration(acceleration);
}

void loop() {
  if (Serial.available()) {
    char positionChar = Serial.read();
    switch (positionChar) {
      case 'a':
        stepper.moveTo(0*partitionVal);
        break;

      case 'b':
        stepper.moveTo(1*partitionVal);
        break;

      case 'c':
        stepper.moveTo(2*partitionVal);
        break;

      case 'd':
        stepper.moveTo(3*partitionVal);
        break;
        
      case 'e':
        stepper.moveTo(4*partitionVal);
        break;
        
      case 'f':
        stepper.moveTo(5*partitionVal);
        break;  
        
      case 'g':
        stepper.moveTo(6*partitionVal);
        break;
              
      case 'h':
        stepper.moveTo(7*partitionVal);
        break;
              
      case 'i':
        stepper.moveTo(8*partitionVal);
        break;
              
      case 'j':
        stepper.moveTo(9*partitionVal);
        break;
              
      case 'k':
        stepper.moveTo(10*partitionVal);
        break;
              
      case 'l':
        stepper.moveTo(11*partitionVal);
        break;
        
      case 'm':
        stepper.moveTo(12*partitionVal);
        break;
        
      case 'n':
        stepper.moveTo(13*partitionVal);
        break;
        
      case 'o':
        stepper.moveTo(14*partitionVal);
        break;
        
      case 'p':
        stepper.moveTo(15*partitionVal);
        break;
        
      case 'q':
        stepper.moveTo(16*partitionVal);
        break;
        
      case 'r':
        stepper.moveTo(17*partitionVal);
        break;
        
      case 's':
        stepper.moveTo(18*partitionVal);
        break;
        
      case 't':
        stepper.moveTo(19*partitionVal);
        break;
        
      default:
        stepper.run();
        break;

    }  // end switch
    
    stepper.run();
    
  }  // end if Serial.available
  
  else if (stepper.run())   {
    stepper.runToPosition();
  }
  
  else if (!stepper.run())  {
    stepper.moveTo(0);
    stepper.run();
  }

  stepper.run();
}
