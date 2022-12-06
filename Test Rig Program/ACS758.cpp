#include "ACS758.h"

#define ADC_SCALE 3.25 / 1023.0

ACS758::ACS758(int cin, int vin, float current_ratio, float voltage_ratio, float current_offset) {
  CIN = cin;
  VIN = vin;
  CURRENT_RATIO = current_ratio;
  VOLTAGE_RATIO = voltage_ratio;
  CURRENT_OFFSET;
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

float ACS758::current(int times = 100) {
  float sum = 0.0;
  for (int i = 0; i < times; i++) {
    sum += analogRead(CIN);
    delay(3);
  }
  float avg = sum / times;
  return ((avg * ADC_SCALE) * CURRENT_RATIO) - CURRENT_OFFSET;
}