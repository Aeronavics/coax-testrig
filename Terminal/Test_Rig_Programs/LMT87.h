//=========================================================================
//  Author: Reuben Campbell
//  Date Created: 10/01/2023
//  Description: Returns infomation about the temperature value from the 
//               LMT87 sensors
//=========================================================================

#ifndef LMT87_h
#define LMT87_h

#include <Arduino.h>

class LMT87
{
  private:
    int PIN;
  
  public:
    LMT87(int pin);
    float temp(int times = 10);
};

#endif