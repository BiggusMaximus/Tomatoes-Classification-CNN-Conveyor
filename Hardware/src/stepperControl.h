#include <Stepper.h>
#include <Arduino.h>

#define RPM_VAL 30
const int stepsPerRevolution = 200;
Stepper conveyorStepper(stepsPerRevolution, A2, A3, A4, A5); // IN1, IN2, IN3, IN4

void stepperIntialization()
{
    conveyorStepper.setSpeed(RPM_VAL);
}

void stopStepper()
{
    conveyorStepper.step(0);
}

void moveStepper()
{
    conveyorStepper.step(10);
}