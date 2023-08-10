#include "HX711.h"
#include <Wire.h>
#include <LiquidCrystal_I2C.h>

const int LOADCELL_DOUT_PIN = 2;
const int LOADCELL_SCK_PIN = 3;

HX711 scale;
const float calibration_factor = 420;
LiquidCrystal_I2C lcd(0x27, 16, 2);  

void setup() {
  Serial.begin(57600);
  scale.begin(LOADCELL_DOUT_PIN, LOADCELL_SCK_PIN);
  scale.set_scale(calibration_factor); 

  lcd.begin(16, 2);  
  lcd.backlight();   
  lcd.setCursor(0, 0);
  lcd.print("Berat: ");
}

void loop() {

  if (scale.is_ready()) {
    float reading = scale.get_units();
    lcd.setCursor(8, 0);      
    lcd.print("      ");      
    lcd.setCursor(8, 0);
    lcd.print(reading, 2);    
    lcd.print(" kg");
  } else {
    Serial.println("HX711 not found.");
    lcd.setCursor(0, 1);
    lcd.print("HX711 not found."); 
  }

  delay(1000);
}
