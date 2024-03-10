#include <Arduino.h>
#include "dimmer.h"
#include "servoControl.h"
#include "stepperControl.h"
#include "receiveData.h"

String messageRaspberry;

unsigned long previousMillis = 0;  
const long interval = 5000;        
bool change = true;


void setup()
{
  Serial.begin(115200);
  dimmerInitialization();
  servoInitialization();
  stepperIntialization();
}

void loop()
{
  if (Serial.available() > 0) {
    String status = Serial.readStringUntil('\n');
    Serial.print("You sent me: ");
    Serial.println(status);
    moveStepper(status);
  }
  
}