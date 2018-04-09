#include <wiringPi.h>

int main (void)
{
  wiringPiSetup();
  pinMode(0, OUTPUT);

  return 0;
}
