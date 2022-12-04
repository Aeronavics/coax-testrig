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
#define SPEED_MAX 1900
#define SPEED_INC 100

//Power presets
#define VOLTAGE_RATIO_TOP 18.84300
#define CURRENT_RATIO_TOP 18.91505
#define VOLTAGE_RATIO_BOTTOM 18.95842
#define CURRENT_RATIO_BOTTOM 19.33637
#define CURRENT_OFFSET_TOP 0.165
#define CURRENT_OFFSET_BOTTOM 0

#define ONE_THOUSAND 1000
#define START_UP_WAIT 3000
#define SLOW_DOWN 30
#define RUN_NUM 4

ACS758 top_motor(CIN_TOP, VIN_TOP, CURRENT_RATIO_TOP, VOLTAGE_RATIO_TOP, CURRENT_OFFSET_TOP);
ACS758 bottom_motor(CIN_BOTTOM, VIN_BOTTOM, CURRENT_RATIO_BOTTOM, VOLTAGE_RATIO_BOTTOM, CURRENT_OFFSET_BOTTOM);
Servo top_esc;
Servo bottom_esc;
HX711 loadcell;

void setup() {

  if(SPEED_MAX > 2000) {  // Safety feature so motors speed range cannot go above a pre set limit
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

  // baud rate init
  Serial.begin(9600);

}

void header_setup(void) {
  //  Writes headers to serial
  Serial.println("Time: ");
  Serial.println("Motor PWM, Top Voltage (V), Bottom Voltage (V), Top Current (A), Bottom Current (A), Thrust (kg)");
}

void printer(int speed) {
  // Prints results into csv friendly format
  for(int reps = 0; reps < RUN_NUM; reps++) {
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


void motor_speeds(int speed) {
  // changes speeds of motor by changing PWM to ESCs
  top_esc.writeMicroseconds(speed);
  bottom_esc.writeMicroseconds(speed);
}

bool done = false;
bool SAFE = true;
int speed = 0;

void loop() {
  // The main function
  if (Serial.available() > 0) {       // 
    delay(ONE_THOUSAND);              // Allow time to for python to send '1'

    if (Serial.read() == '1') {       // When received 1 start up sequence will begin
      Serial.println("Turing Power On!");
      delay(START_UP_WAIT);           // Delay before start up

      while(!done) {
        header_setup();
        
        for (speed = SPEED_MIN; speed <= SPEED_MAX; speed += SPEED_INC) { // Toggles ESC PWM
          motor_speeds(speed);
          delay(300);
          printer(speed);
        }

        // Test finished. Set ESC's to low
        Serial.println("Finished");
        done = true;
      }
      for(speed = SPEED_MAX; speed >= ONE_THOUSAND; speed -= SLOW_DOWN) {
        motor_speeds(speed);
        delay(50);
      }

      // remove items in serial for next test
      Serial.flush();
    }
  }

  else {  // Wait time so python can communicate w Arduino
    delay(ONE_THOUSAND);
    Serial.println("Waiting...");
  }

}
