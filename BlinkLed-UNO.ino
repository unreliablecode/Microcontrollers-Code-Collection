// Define the LED pin
const int ledPin = 13;

void setup() {
  // Initialize the LED pin as an output
  pinMode(ledPin, OUTPUT);
}

void loop() {
  // Turn the LED on
  digitalWrite(ledPin, HIGH);
  
  // Wait for a short period
  delay(1000); // 1000 milliseconds (1 second)
  
  // Turn the LED off
  digitalWrite(ledPin, LOW);
  
  // Wait for a short period
  delay(1000); // 1000 milliseconds (1 second)
}
