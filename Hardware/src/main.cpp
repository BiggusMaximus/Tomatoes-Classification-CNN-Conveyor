#include <Arduino.h>
#include "servoControl.h"
#include "stepperControl.h"

void setup()
{
  Serial.begin(9600);
  servoInitialize();
  stepperIntialization();
}

void loop()
{
  // moveServo("0");
  // delay(1000);
  // moveServo("1");
  // delay(1000);
  // moveServo("2");
  // delay(1000);
  // moveServo("3");
  // delay(1000);
  conveyorStepper.step(1);
}