#include <Arduino.h>
#include "dimmer.h"
#include "servoControl.h"
#include "stepperControl.h"
#include "receiveData.h"
#include "ultrasonic.h"
#include "kalman.h"

String status = "N";
unsigned long previousMillis = 0;  
const long interval = 10000;        
bool tomat_baru = true;

uint8_t count = 0;
String servos[3] = {"Servo 1", "Servo 2", "Servo 3"};

void setup()
{
  Serial.begin(115200);
  dimmerInitialization();
  servoInitialization();
  stepperIntialization();
  moveStepper();
}

void loop()
{

  if(Serial.available() > 0){
    moveStepper();
    long unsigned int sensor_reading[2] = {sonar1.ping_cm(), sonar2.ping_cm()};
    float *kalman_distance = kalmanFilter(sensor_reading);
    if ((kalman_distance[0] < 6) and (tomat_baru)){
      Serial.println("Detected");
      stopStepper();
      String tomat_class = Serial.readStringUntil('\n');
      moveServo(tomat_class);
      tomat_baru = false;
    }

    if (kalman_distance[1] < 6){
      tomat_baru = true;
  }
  /*
    F : Found
    X : Not Found
    D : Done
    S : Search
  */
  // if (Serial.available() > 0) {
  //   if (measure_distance() <= 7){ // Check if an object is detected within 7 units
  //     Serial.println("P");  // Send 'P' signal to Raspberry Pi
  //     stopStepper(); // Stop stepper
  //     String tomat_class = Serial.readStringUntil('\n');
  //     moveServo(tomat_class);
  //     Serial.println("R");  // Send acknowledgment to Raspberry Pi after classification
  //     moveStepper(); // Move stepper
  //   } else {
  //     moveStepper(); // Continue moving the stepper if no object is detected
  //   }
  // } else {
  //   moveStepper(); // Continue moving the stepper if no data is received from Raspberry Pi
  // }
  // int d = sonar.ping_cm();
  // if ((d <= 5) and (can_read)){
  //   can_read = false;
  //   stopStepper();
  //   Serial.println("F");  
  //   String tomat_class = Serial.readStringUntil('\n');
  //   moveServo(tomat_class);
  //   Serial.println("D");  // Send acknowledgment to Raspberry Pi after classification
  //   moveStepper(); // Move stepper

  // }else{
  //  // Serial.println(d);  // Send 'P' signal to Raspberry Pi
  //   moveStepper();
  // }

  
  // Servo Calibration
  // unsigned long currentMillis = millis();
  // if (currentMillis - previousMillis >= interval) {
  //   previousMillis = currentMillis;
  //   count += 1;
  // }

  // if (currentMillis - previousMillis >= interval-1000) {
  //   Serial.println("Ganti servo 1s");
  // }

  // if (count == 3){
  //   count = 0;
  // }
  // servoCalibration(servos[count]);
  
  // //Test Servo state
  // for (int i = 0; i < 4; i++)
  // {
  //   moveServo(String(i));
  //   delay(2000);
  //   /* code */
  // }
  
}