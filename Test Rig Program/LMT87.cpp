//=========================================================================
//  Author: Reuben Campbell
//  Date Created: 10/01/2023
//  Description: Returns infomation about the temperature value from the 
//               LMT87 sensors
//=========================================================================

#include "LMT87.h"

#define ADC_SCALE 2.76 / 1023.0
#define OFFSET 2.637
#define TEMP_COEFFICIENT 0.0136

LMT87::LMT87(int pin) {
  PIN = pin;
}

float LMT87::temp(int times = 10) {
  float sum = 0;
  for (int i = 0; i < times; i++) {
    sum += analogRead(PIN);
    delay(3);
  }
  float avg = sum / times;
  return (OFFSET - (avg * ADC_SCALE)) / TEMP_COEFFICIENT;
}