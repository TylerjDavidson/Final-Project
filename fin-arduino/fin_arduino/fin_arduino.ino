#include <SimpleDHT.h>
#include <LiquidCrystal.h>
const int rs=12, en=11, d4=6, d5=5, d6=4, d7=3;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

// for DHT11,
//      VCC: 5V or 3V
//      GND: GND
//      DATA: 2
int pinDHT11 = 2;
SimpleDHT11 dht11;

void setup() {
  //set up the LCD's number of columns and rows
  lcd.begin(16,2);
  Serial.begin(9600);
}

void loop() {
  byte temperature = 0;
  byte humidity = 0;
  if(Serial.available()>0){
    char c = Serial.read();
    switch(c){
      case 'p':
      if (dht11.read(pinDHT11, &temperature, &humidity, NULL)) {
        return;
      }
      Serial.print(temperature); Serial.print(",");
      Serial.print(humidity); Serial.println("");
      break;
      case 'l':
      //msg = serial.readString(); //read in cheep
      lcd.clear();//clear screen
      lcd.setCursor(0,0);//top left
      lcd.print("user1: hey");
      break;
    }
  }
}
