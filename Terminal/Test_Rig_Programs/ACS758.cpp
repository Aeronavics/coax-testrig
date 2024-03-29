//=========================================================================
//  Author: Reuben Campbell
//  Date Created: 21/11/2022
//  Description: Returns infomation about the current and voltage from the
//               the ACS758 sensors
//=========================================================================

#include "ACS758.h"

#define ADC_SCALE 2.76 / 1023.0

ACS758::ACS758(int cin, int vin, float current_ratio, float voltage_ratio) {
  CIN = cin;
  VIN = vin;
  CURRENT_RATIO = current_ratio;
  VOLTAGE_RATIO = voltage_ratio;
  pinMode(CIN, INPUT);
  pinMode(VIN, INPUT);
}

float ACS758::voltage(int times = 10) {
  float sum = 0.0;
  for (int i = 0; i < times; i++) {
    sum += analogRead(VIN);
    delay(3);
  }
  float avg = sum / times;
  return (avg * ADC_SCALE) * VOLTAGE_RATIO;
}

float ACS758::current(int times = 80) {
  float sum = 0.0;
  for (int i = 0; i < times; i++) {
    sum += analogRead(CIN);
    delay(3);
  }
  float avg = sum / times;
  return ((avg * ADC_SCALE) * CURRENT_RATIO);
}