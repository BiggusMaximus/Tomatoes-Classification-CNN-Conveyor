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
   String receivedData = receiveString();
   Serial.println("Data received : " + receivedData);
   moveServo(receivedData);
   conveyorStepper(1);
}