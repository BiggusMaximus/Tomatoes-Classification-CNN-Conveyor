#include <Arduino.h>

String receiveString() {
  String receivedString = "";
  static char buffer[64];  // Buffer to store incoming characters

  while (Serial.available() > 0) {
    char incomingChar = Serial.read();

    // Check for the end of the string (newline character)
    if (incomingChar == '\n') {
      buffer[0] = '\0';  // Null-terminate the buffer
      receivedString = String(buffer);
      break;
    }

    // Append the incoming character to the buffer
    strncat(buffer, &incomingChar, 1);
  }

  return receivedString;
}