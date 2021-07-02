#include <LiquidCrystal.h>

// set up pins on LCD display
LiquidCrystal lcd(7, 8, 9, 10, 11, 12);
String screen_info;

void setup() {
  Serial.begin(9600);
  Serial.setTimeout(2);
  pinMode(6, INPUT); // set pin 6 to be input to push button down
  pinMode(5, INPUT); // set pin 5 to be input to push button right
  pinMode(4, INPUT); // set pin 4 to be input to push button select
  pinMode(3, INPUT); // set pin 3 to be input to push button left
  pinMode(2, INPUT); // set pin 2 to be input to push button up
  
  lcd.begin(16, 2);
  lcd.setCursor(0, 0);
  lcd.print("    Welcome   ");
}

void selectButton (){
  Serial.print("SELECT\n");
  delay(250);
}

void rightButton(){
  Serial.print("RIGHT\n");
  delay(250);
}

void leftButton(){
  Serial.print("LEFT\n");
  delay(250);
}

void upButton(){
  Serial.print("UP\n");
  delay(250);
}

void downButton(){
  Serial.print("DOWN\n");
  delay(250);
}

void loop() {
  
  // button detection 
  if (digitalRead(5) > 0)
    rightButton();
 
  else if (digitalRead(4) > 0)
    selectButton();

  else if (digitalRead(3) > 0)
    leftButton();

  else if (digitalRead(2) > 0)
    upButton();

  else if (digitalRead(6) > 0)
    downButton();
  
  // serial communication with python
  if (Serial.available() > 0)
  {
    screen_info = Serial.readString();

    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print(screen_info);
  }
}
