/*
  Code that runs the test and puts data into csv format for python to read
  Automatically changes motor speeds

*/

// Libraries and Modules
#include <Servo.h>
#include "HX711.h"
#include "ACS758.h"
#include "LMT87.h"


// Arduino ports
#define LOADCELL_SCK 2
#define LOADCELL_DOUT 3

#define TOP_ESC 6
#define BOTTOM_ESC 5

#define SWITCH_PIN 9
#define POWER_PIN 11  

#define VIN_TOP A1
#define CIN_TOP A0
#define VIN_BOTTOM A3
#define CIN_BOTTOM A2

#define TOP_TEMP_SENSOR A4
#define TOP_TEMP_SENSOR A5


// Load cell presets
#define LOADCELL_SCALE 60000

// Motor presets
#define SPEED_MIN 1000
#define SPEED_MAX 1800
#define SPEED_INC 100

// Power presets
#define VOLTAGE_RATIO_TOP 18.84300
#define CURRENT_RATIO_TOP 18.91505
#define VOLTAGE_RATIO_BOTTOM 18.95842
#define CURRENT_RATIO_BOTTOM 19.33637

// Constants
#define ONE_THOUSAND 1000
#define START_UP_WAIT 3000
#define SLOW_DOWN 15
#define RUN_NUM 5
#define MAX_CURRENT 17

// Globals Variables
unsigned long switch_time = 0;  
unsigned long last_switch_time = 0; 
int speed = 0;
bool done = false;


ACS758 top_motor(CIN_TOP, VIN_TOP, CURRENT_RATIO_TOP, VOLTAGE_RATIO_TOP);
ACS758 bottom_motor(CIN_BOTTOM, VIN_BOTTOM, CURRENT_RATIO_BOTTOM, VOLTAGE_RATIO_BOTTOM);
Servo top_esc;
Servo bottom_esc;
HX711 loadcell;
LMT87 sensor1(A4);
LMT87 sensor2(A5);


void setup() {

  if(SPEED_MAX > 2000) {  // Safety feature so motors speed range cannot go above a pre set limit
    Serial.println("MAX SPEED IS TOO HIGH");
    Serial.println("Aborting");
    abort();
  }

  // Pin set up for switch
  pinMode(POWER_PIN, OUTPUT);
  pinMode(SWITCH_PIN, INPUT_PULLDOWN);
  digitalWrite(POWER_PIN, HIGH);
  attachInterrupt(digitalPinToInterrupt(SWITCH_PIN), emergency_SIR, CHANGE);

  analogReference(EXTERNAL);  // 2.76V

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


void header_setup(void) 
{
  //  Writes headers to serial
  Serial.println("Time: ");
  Serial.println("Motor PWM, Top Voltage (V), Bottom Voltage (V), Top Current (A), Bottom Current (A), Thrust (kg)");
}


void printer(int speed) 
{
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
    delay(1);
  }
}


void motor_speeds(int speed) 
{
  // changes speeds of motor by changing PWM to ESCs
  top_esc.writeMicroseconds(speed);
  bottom_esc.writeMicroseconds(speed);
}



bool check_current() 
{ //  Checks if current is over motor limit. If so will turn them off
  //  and will end the test 
  float top_current = top_motor.current();
  float bottom_current = bottom_motor.current();

  if(top_current > MAX_CURRENT || bottom_current > MAX_CURRENT) {
    Serial.println("MAX CURRENT");
    Serial.println("Shutting down");

    return true;
  } else {
    return false;
  }

}



void turn_off_sequence(int speed)
{
  // Turn off sequence
  if(done != true) {
    for(int ispeed = speed; ispeed >= SPEED_MIN; ispeed -= SLOW_DOWN) {
      motor_speeds(ispeed);
      delay(50);
    }
  }

  done = true;
}


void loop() {
  // The main function
  if (Serial.available() > 0 && done == false) {
    delay(ONE_THOUSAND);              // Allow time to for python to send '1'

    if (Serial.read() == '1') {     // When received 1 start up sequence will begin

      Serial.println("Turing Power On!");
      delay(START_UP_WAIT);           // Delay before start up

      header_setup();
      
      for (speed = SPEED_MIN; speed <= SPEED_MAX; speed += SPEED_INC) {  // Toggles ESC PWM
        motor_speeds(speed);
        done = check_current();
        if(done == true) {
          break;
        }

        delay(300);  
        printer(speed);
      }

      turn_off_sequence(speed);
      // Test finished. Set ESC's to low
      Serial.println("Finished");

      // Turn off sequence

      // remove items in serial for next test
      Serial.flush();
    }
  }

  else {  // Wait time so python can communicate w Arduino
    delay(ONE_THOUSAND);
    Serial.println("Waiting...");
  }

}


void emergency_SIR()
// Interrupt that stops program if switch has been pressed
{
  switch_time = millis();
  if(switch_time - last_switch_time > 500) {
    Serial.println("STOP SWITCH");
    done = true;
    motor_speeds(SPEED_MIN);

    last_switch_time = switch_time;
  }

  abort();
   // Ensures there is no way the motors can start back up as no PWM will be sent
}
