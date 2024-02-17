#include <Arduino.h>
#include "servoControl.h"
#include "stepperControl.h"
#include "receiveData.h"

void setup()
{
  Serial.begin(9600);
  servoInitialize();
  stepperIntialization();
}

void loop()
{
  String receivedMessage = Serial.readStringUntil('\n'); // Read the incoming message until a newline character
  if (receivedMessage.length() > 0) {
      Serial.println("Data received : " + receivedMessage);
      moveServo(receivedMessage);
  }
}