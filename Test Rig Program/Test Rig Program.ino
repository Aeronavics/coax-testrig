/*
  Code that runs the test and puts data into csv format for python to read
  // Automatically changes motor speeds

*/


#include <Servo.h>
#include "HX711.h"
#include "ACS758.h"

#define LOADCELL_SCK 2
#define LOADCELL_DOUT 3

#define TOP_ESC 6
#define BOTTOM_ESC 5

#define VIN_TOP A1
#define CIN_TOP A0
#define VIN_BOTTOM A3
#define CIN_BOTTOM A2

//Load cell presets
#define LOADCELL_SCALE 90900

//Motor presets
#define SPEED_MIN 1100
#define SPEED_MAX 1700
#define SPEED_INC 100

//Power presets
#define VOLTAGE_RATIO_TOP 18.84300
#define CURRENT_RATIO_TOP 18.91505
#define VOLTAGE_RATIO_BOTTOM 18.95842
#define CURRENT_RATIO_BOTTOM 19.33637
#define CURRENT_OFFSET_TOP 0.165
#define CURRENT_OFFSET_BOTTOM 0

ACS758 top_motor(CIN_TOP, VIN_TOP, CURRENT_RATIO_TOP, VOLTAGE_RATIO_TOP, CURRENT_OFFSET_TOP);
ACS758 bottom_motor(CIN_BOTTOM, VIN_BOTTOM, CURRENT_RATIO_BOTTOM, VOLTAGE_RATIO_BOTTOM, CURRENT_OFFSET_BOTTOM);
Servo top_esc;
Servo bottom_esc;
HX711 loadcell;

void setup() {

  if(SPEED_MAX > 2000) {
    Serial.println("MAX SPEED IS TOO HIGH");
    Serial.println("Aborting");
    abort();
  }
  //Initialise load cell
  loadcell.begin(LOADCELL_DOUT, LOADCELL_SCK);
  loadcell.set_scale(LOADCELL_SCALE);
  loadcell.tare(10);

  //Initialise ESCs
  top_esc.attach(TOP_ESC);
  bottom_esc.attach(BOTTOM_ESC);
  top_esc.writeMicroseconds(1000);
  bottom_esc.writeMicroseconds(1000);

  Serial.begin(9600);
  Serial.println("Time:");

  
}

void printer(int speed) {
  // Prints results into csv friendly format
  for(int reps = 0; reps < 5; reps++) {
    Serial.print(speed);
    Serial.print(",");
    Serial.print(top_motor.voltage());
    Serial.print(",");
    Serial.print(bottom_motor.voltage());
    Serial.print(",");
    Serial.print(top_motor.current());
    Serial.print(",");
    Serial.print(bottom_motor.current());
    Serial.print(",");  
    Serial.println(loadcell.get_units(10));
  }
}

bool done = false;

void loop() {
  // Waits for '1' to be sent from python code
  if (Serial.available() > 0) {
    delay(1000);
    if (Serial.read() == '1') {
      Serial.println("Turing Power On!");
      delay(3000);

      while(!done) {
        Serial.println("Motor PWM, Top Voltage (V), Bottom Voltage (V), Top Current (A), Bottom Current (A), Thrust (kg)");
        for (int speed = SPEED_MIN; speed <= SPEED_MAX; speed += SPEED_INC) { // Toggles ESC PWM
          top_esc.writeMicroseconds(speed);
          bottom_esc.writeMicroseconds(speed);
          delay(400);
          printer(speed);
        }
        top_esc.writeMicroseconds(1000);
        bottom_esc.writeMicroseconds(1000);
        Serial.println("Finished");
        done = true;
      }

      Serial.flush();
    }
  }
  else {  // Wait time so python can communicate w Arduino
    delay(1000);
    Serial.println("Waiting...");
  }

}