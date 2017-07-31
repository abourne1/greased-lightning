#include<Servo.h>

Servo servo;

void setup() {
  Serial.begin(14400);
  servo.attach(9);
  servo.write(90);
}

void loop() {
  delay(100);
  int numDigits = Serial.available();
  if (numDigits > 0) {
    int serialData = Serial.parseInt();
    Serial.println(serialData);
    servo.write(serialData);
  }
}
