const int ledPin = 2;  // Pin number where the LED is connected

void setup() {
  pinMode(ledPin, OUTPUT);  // Set the LED pin as an output
}

void loop() {
  // Increase LED brightness gradually
  for (int brightness = 0; brightness <= 255; brightness++) {
    analogWrite(ledPin, brightness);  // Set LED brightness using PWM
    delay(10);  // Delay for a short period
  }
  
  // Decrease LED brightness gradually
  for (int brightness = 255; brightness >= 0; brightness--) {
    analogWrite(ledPin, brightness);  // Set LED brightness using PWM
    delay(10);  // Delay for a short period
  }
}
