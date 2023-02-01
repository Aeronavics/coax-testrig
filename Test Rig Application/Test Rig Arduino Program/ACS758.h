#ifndef ACS758_h
#define ACS758_h

#include <Arduino.h>

class ACS758
{
  private:
    int CIN;
    int VIN;
    float CURRENT_RATIO;
    float VOLTAGE_RATIO;

  public:
    ACS758(int cin, int vin, float current_ratio, float voltage_ratio);
    float voltage(int times = 10);
    float current(int times = 20);
};

#endif