#include <Arduino.h>
#include "dimmer.h"
#include "servoControl.h"
#include "stepperControl.h"
// #include "receiveData.h"

void setup()
{
  Serial.begin(9600);
  dimmerInitialization();
  servoInitialization();
  stepperIntialization();
}

void loop()
{
  //testServo();
  //moveStepper();
}