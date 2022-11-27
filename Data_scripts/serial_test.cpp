// Program that simply writes to serial monitor for testing
String datalabel1 = "Power1";
String datalabel2 = "Speed1";

void setup() {
  Serial.begin(9600);
  Serial.print(datalabel1 + ",");
  Serial.println(datalabel1);
}

bool done = false;

void loop() {
  

  if(done == false)
  {
    printer();
    done = true;
  }

}


void printer(void) 
{
  int i = 0;
  while(i < 20) 
  {
    int hold = i;
    Serial.print(hold, DEC);
    Serial.print(",");
    Serial.print(hold + 10, DEC);
    Serial.print(",");
    Serial.println(hold * 3.145, DEC);
    i++;
  }
}
