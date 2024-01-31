#include <Adafruit_CircuitPlayground.h>
#include <Adafruit_Circuit_Playground.h>
#include <Wire.h>
#include <SPI.h>
//decide whether or not the timer is 1 minute or more (like 2 or 3) maybe give them the option
float X, Y, Z;
float beatCount = 0;
uint16_t alarmThreshold = 20;  // adjust to change alarm sensitivty
bool triggered = false;        // becomes true when diary removed
bool running = true;
float total_time = 60000;
float delta_time = total_time / 10;
float previous = 10;
int bpm;
void setup() {
  Serial.begin(9600);
  CircuitPlayground.begin();
}

void loop() {
  for (int p=0; p<120; p+=1) {
		delay(500);
  //X = CircuitPlayground.motionX();
  Y = CircuitPlayground.motionY();
  //Z = CircuitPlayground.motionZ();
  Serial.println(Y);
  if (Y > 0.15) {
      beatCount += 1;
    }

}
if (beatCount > 205) { //add time variable limit
    triggered = true;
    Serial.println("Baby's heart rate is too high");
    Serial.print("BPM is ");
    Serial.println(beatCount);
    }
if (beatCount < 100) { //add time variable limit
    triggered = true;
    Serial.println("Baby's heart rate is too low.");
    bpm = beatCount / 60;
    Serial.print("BPM is ");
    Serial.println(beatCount);
    }
else {
    Serial.println("Heartbeat is normal.");
    Serial.print("BPM is ");
    Serial.println(beatCount);
}
if (triggered) {
		CircuitPlayground.playTone(445, 50);
		delay(1000);
		CircuitPlayground.playTone(445, 50);
		delay(1000);
		CircuitPlayground.playTone(445, 50);
		delay(1000);
    CircuitPlayground.playTone(445, 50);
		delay(1000);
    CircuitPlayground.playTone(445, 50);
		delay(1000);
  }
}
