#include <Servo.h>
#include <Arduino.h>
#define SERVO_1 9
#define SERVO_2 10
#define SERVO_3 11

Servo Servo1;
Servo Servo2;
Servo Servo3;

void servoInitialize()
{
    Servo1.attach(SERVO_1);
    Servo2.attach(SERVO_2);
    Servo3.attach(SERVO_3);
    Servo1.write(100);
    Servo2.write(100);
    Servo3.write(105);
}

void servoCalibration()
{
    int angle1 = analogRead(A0);
    int angle2 = analogRead(A1);
    int angle3 = analogRead(A2);
    angle1 = map(angle1, 0, 1023, 0, 180);
    angle2 = map(angle2, 0, 1023, 0, 180);
    angle3 = map(angle3, 0, 1023, 0, 180);
    Servo1.write(angle1);
    Servo2.write(angle2);
    Servo3.write(angle3);
    Serial.println("Angle 1 : " + String(angle1) + " | Angle 2 : " + String(angle2) + " | Angle 3 : " + String(angle3));
}

void moveServo(String command)
{
    Serial.println("Command Servo : " + command);
    if (command == "0")
    {
        Servo1.write(120);
        Servo2.write(130);
        Servo3.write(120);
    }
    else if (command == "1")
    {
        Servo1.write(85);
        Servo2.write(130);
        Servo3.write(120);
    }
    else if (command == "2")
    {
        Servo1.write(85);
        Servo2.write(70);
        Servo3.write(120);
    }
    else if (command == "3")
    {
        Servo1.write(85);
        Servo2.write(70);
        Servo3.write(90);
    }
}
