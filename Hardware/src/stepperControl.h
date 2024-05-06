#include <Arduino.h>
#define SPEED_MOVING 500

const int dirPin = 7;
const int stepPin = 6;
const int stepsPerRevolution = 200;

void moveStepper()
{
    digitalWrite(dirPin, HIGH);
	digitalWrite(stepPin, HIGH);
	delayMicroseconds(SPEED_MOVING);
	digitalWrite(stepPin, LOW);
	delayMicroseconds(SPEED_MOVING);
}
void stopStepper()
{
    digitalWrite(stepPin, LOW);
}

void stepperIntialization()
{
	pinMode(stepPin, OUTPUT);
	pinMode(dirPin, OUTPUT);
}




