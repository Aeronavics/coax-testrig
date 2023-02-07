//=========================================================================
//  Author: Reuben Campbell
//  Date Created: 21/11/2022
//  Description: Returns infomation about the current and voltage from the
//               the ACS758 sensors
//=========================================================================

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
    float current(int times = 80);
};

#endif