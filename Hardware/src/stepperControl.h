#include <Arduino.h>
#include <AccelStepper.h>

const int dirPin = 7;
const int stepPin = 6;

// Define motor interface type
#define motorInterfaceType 1

// Creates an instance
AccelStepper myStepper(motorInterfaceType, stepPin, dirPin);

void stepperIntialization()
{
    myStepper.setMaxSpeed(200);
	myStepper.setAcceleration(1);
	myStepper.setSpeed(100);
}


void moveStepper()
{
    myStepper.runSpeed();
}