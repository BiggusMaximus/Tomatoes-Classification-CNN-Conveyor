#include <VarSpeedServo.h>
#include <Arduino.h>
#define SERVO_1 11
#define SERVO_2 10
#define SERVO_3 9

VarSpeedServo Servo1;
VarSpeedServo Servo2;
VarSpeedServo Servo3;

int position_state[4][3] = {
    {111, 120, 128},
    {46 , 120, 128},
    {46, 70, 128},
    {46, 70, 82},
};
void servoInitialization()
{
    Servo1.attach(SERVO_1);
    Servo2.attach(SERVO_2);
    Servo3.attach(SERVO_3);
    Servo1.write(position_state[0][0], 50);
    Servo2.write(position_state[0][1], 50);
    Servo3.write(position_state[0][2], 50);
}

void servoCalibration(String which_servo)
{
    int angle1 = 90;
    int angle2 = 90;
    int angle3 = 90;
    pinMode(A0, INPUT);
    int angle = analogRead(A0);
    if (which_servo == "Servo 1"){
        angle1 = angle;
        angle1 = map(angle1, 0, 1023, 0, 180);
        Servo1.write(angle1);
    }else if(which_servo == "Servo 2"){
        angle2 = angle;
        angle2 = map(angle2, 0, 1023, 0, 180);
        Servo2.write(angle2);
    }else{
        angle3 = angle;
        angle3 = map(angle3, 0, 1023, 0, 180);
        Servo3.write(angle3);
    }
    Serial.println(which_servo + " | Angle 1 : " + String(angle1) + " | Angle 2 : " + String(angle2) + " | Angle 3 : " + String(angle3));
}


void testServo(){

    Serial.println("0");
    Servo1.write(80);
    Servo2.write(80);
    Servo3.write(125);

    delay(3000);
    Serial.println("1");
    Servo1.write(120);
    Servo2.write(80);
    Servo3.write(125);

    delay(3000);
    Serial.println("2");
    Servo1.write(120);
    Servo2.write(140);
    Servo3.write(125);
    delay(3000);
    Serial.println("3");
    Servo1.write(120);
    Servo2.write(140);
    Servo3.write(170);
    delay(3000);
    
}

void moveServo(String command)
{
    int state = command.toInt();
    Serial.println("State : " + String(state)
    + " | Angle-1 : " + String(position_state[state][0])
    + " | Angle-2 : " + String(position_state[state][1])
    + " | Angle-3 : " + String(position_state[state][2]));

    Servo1.write(position_state[state][0], 50);
    Servo2.write(position_state[state][1], 50);
    Servo3.write(position_state[state][2], 50);
    
}
