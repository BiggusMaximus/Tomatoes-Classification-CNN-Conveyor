#include <Arduino.h>
#define LED_PIN A5

void dimmerInitialization(){
    pinMode(LED_PIN, OUTPUT);
    analogWrite(LED_PIN, 130);
}

void testDimmer(){
    for (size_t i = 120; i < 255; i+=5)
    {

        analogWrite(LED_PIN, i);
        Serial.println("PWM : " + String(i));
        delay(1000);
    }
    
}