/*
  Arduino code to be used with test rig GUI

*/

//---------------------------------------------------------------------------------------

#include <Servo.h>
#include "HX711.h"
#include "ACS758.h"
#include "LMT87.h"

//---------------------------------------------------------------------------------------

// Arduino connection pins
#define LOADCELL_SCK 2
#define LOADCELL_DOUT 3

#define TOP_ESC 6
#define BOTTOM_ESC 5

#define VIN_TOP A1
#define CIN_TOP A0
#define VIN_BOTTOM A3
#define CIN_BOTTOM A2

#define TIN_TOP A4
#define TIN_BOTTOM A5

//---------------------------------------------------------------------------------------

//Load cell presets
#define LOADCELL_SCALE 60000

//Motor presets
#define SPEED_MIN 1000
#define SPEED_MAX 1800
#define SPEED_INC 100
#define RAMP_UP_DELAY 5
#define RAMP_DOWN_DELAY 5

//Power presets
#define VOLTAGE_RATIO_TOP 18.84300 //MT-16422
#define CURRENT_RATIO_TOP 18.91505
#define VOLTAGE_RATIO_BOTTOM 18.95842 //MT-16426
#define CURRENT_RATIO_BOTTOM 19.33637

//---------------------------------------------------------------------------------------

ACS758 top_motor(CIN_TOP, VIN_TOP, CURRENT_RATIO_TOP, VOLTAGE_RATIO_TOP);
ACS758 bottom_motor(CIN_BOTTOM, VIN_BOTTOM, CURRENT_RATIO_BOTTOM, VOLTAGE_RATIO_BOTTOM);
LMT87 top_temp(TIN_TOP);
LMT87 bottom_temp(TIN_BOTTOM);
Servo top_esc;
Servo bottom_esc;
HX711 loadcell;

//---------------------------------------------------------------------------------------

void setSpeed(int speed, bool top_motor_enabled, bool bottom_motor_enabled) {
  if (top_motor_enabled) {
    top_esc.writeMicroseconds(speed);
  }
  if (bottom_motor_enabled) {
    bottom_esc.writeMicroseconds(speed);
  }
}

//---------------------------------------------------------------------------------------

void disarm(int speed, bool top_motor_enabled, bool bottom_motor_enabled) {
  for (speed; speed >= SPEED_MIN; speed--) {
    setSpeed(speed, top_motor_enabled, bottom_motor_enabled);
    delay(RAMP_DOWN_DELAY);
    //Send data back
  }
}

//---------------------------------------------------------------------------------------

void sendData(int speed) {
  float thrust = 0;
  float top_motor_voltage = 0;
  float top_motor_current = 0;
  float bottom_motor_voltage = 0;
  float bottom_motor_current = 0;

  for (int i = 0; i < 10; i++) {
    thrust += loadcell.get_units(2);
    delay(3);
    top_motor_voltage += top_motor.voltage();
    delay(3);
    top_motor_current += top_motor.current();
    delay(3);
    bottom_motor_voltage += bottom_motor.voltage();
    delay(3);
    bottom_motor_current += bottom_motor.current();
    delay(3);
  }
  
  thrust /= 10;
  top_motor_voltage /= 10;
  top_motor_current /= 10;
  bottom_motor_voltage /= 10;
  bottom_motor_current /= 10;

  Serial.print(speed);
  Serial.print(",");
  Serial.print(thrust);
  Serial.print(",");
  Serial.print(top_motor_voltage);
  Serial.print(",");
  Serial.print(top_motor_current);
  Serial.print(",");
  Serial.print(bottom_motor_voltage);
  Serial.print(",");
  Serial.print(bottom_motor_current);
  Serial.print(",");
  Serial.print(top_temp.temp());
  Serial.print(",");
  Serial.println(bottom_temp.temp());
}

//---------------------------------------------------------------------------------------

void manualControl(bool top_motor_enabled, bool bottom_motor_enabled) {
  int speed = SPEED_MIN;
  String data_in;
  int value;
  while (true) {
    if (Serial.available()) {
      data_in = Serial.readString();
      data_in.trim();
      value = data_in.toInt();
      if (SPEED_MIN <= value && value <= SPEED_MAX) {
        for (speed; speed > value; speed--) {
          setSpeed(speed, top_motor_enabled, bottom_motor_enabled);
          delay(RAMP_DOWN_DELAY);
          //Send data back
        }
        for (speed; speed <= value; speed++) {
          setSpeed(speed, top_motor_enabled, bottom_motor_enabled);
          delay(RAMP_UP_DELAY);
          //Send data back
        }
      } else if (data_in == "DARM") {
        disarm(speed, top_motor_enabled, bottom_motor_enabled);
        break;
      }
    }
    sendData(speed);
  }
}

//---------------------------------------------------------------------------------------

void rampTest(bool top_motor_enabled, bool bottom_motor_enabled) {
  int speed = SPEED_MIN;
  int speed_set = SPEED_MIN; // Change to (speed % inc == 0)
  for (speed; speed <= SPEED_MAX; speed++) {
    if (Serial.available()) {
      String data_in = Serial.readString();
      data_in.trim();
      if (data_in == "DARM") {
        break;
      }
    }
    setSpeed(speed, top_motor_enabled, bottom_motor_enabled);
    delay(RAMP_UP_DELAY);
    if (speed == speed_set + SPEED_INC) {
      speed_set += SPEED_INC;
      delay(1500);
      sendData(speed);
      delay(1);
    }
  }
  disarm(speed, top_motor_enabled, bottom_motor_enabled);
}

//---------------------------------------------------------------------------------------

void setup() {
  //Initialise load cell
  loadcell.begin(LOADCELL_DOUT, LOADCELL_SCK);
  loadcell.set_scale(LOADCELL_SCALE);
  loadcell.tare(10);

  //Initialise ESCs
  top_esc.attach(TOP_ESC);
  bottom_esc.attach(BOTTOM_ESC);
  top_esc.writeMicroseconds(SPEED_MIN);
  bottom_esc.writeMicroseconds(SPEED_MIN);

  //Initialise Arduino
  analogReference(EXTERNAL);
  Serial.begin(115200);
}

//---------------------------------------------------------------------------------------

void loop() {
  String data_in;
  bool top_motor_enabled = false;
  bool bottom_motor_enabled = true;
  if (Serial.available()) {
    data_in = Serial.readString();
    top_motor_enabled = data_in.substring(5, 9) == "M1ON";
    bottom_motor_enabled = data_in.substring(10, 14) == "M2ON";
    if (data_in.substring(0, 4) == "MARM") {
      manualControl(top_motor_enabled, bottom_motor_enabled);
    } else if (data_in.substring(0, 4) == "STAR") {
      rampTest(top_motor_enabled, bottom_motor_enabled);
    }
  }
}
