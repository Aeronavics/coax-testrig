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