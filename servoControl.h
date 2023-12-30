#include <Servo.h>
#include <Arduino.h>
#define SERVO_1 1
#define SERVO_2 2
#define SERVO_3 3

Servo Servo1;
Servo Servo2;
Servo Servo3;

void servoInitialize(){
    Servo1.attach(SERVO_1);
    Servo2.attach(SERVO_2);
    Servo3.attach(SERVO_3);
}

