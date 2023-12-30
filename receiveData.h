#include <Arduino.h>

void receiveCommand(){
    if (Serial.available() > 0) {
    String input = Serial.readStringUntil('\n');  // Read the string until newline character
    input.trim();  // Remove leading/trailing whitespaces

    // Check if the received string is valid and contains instructions
    if (input.length() > 0) {
      if (input == "rotate") {
        // Rotate the stepper motor
        myStepper.step(1); // Step one step in one direction
        // Delay can be adjusted to change the speed of rotation
        Serial.println("stop");
        delay(5);  // Adjust delay time as needed
      } else if (input == "stop") {
        Serial.println("stop");
      }
    }
  }
}