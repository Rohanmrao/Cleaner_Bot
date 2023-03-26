//MOTOR1 PINS
int ena = 5;
int in1 = 6;
int in2 = 7;
int in3 = 8;
int in4 = 9;
int enb = 10;

void setup() {
  Keyboard.begin();
  pinMode(ena, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(enb, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);

  //MOTOR_A CLOCKWISE MAX SPEED
  if(Keyboard.press('Q')){
  digitalWrite(in1,HIGH);
  digitalWrite(in2,LOW);
  analogWrite(ena, 255);}
  
  //MOTOR_B CLOCKWISE MAX SPEED
  if(Keyboard.press('W')){
  digitalWrite(in3,HIGH);
  digitalWrite(in4,LOW);
  analogWrite(enb, 255);
  delay(2000);}
  
  //STOP
  if(Keyboard.press('E')){
  digitalWrite(in1,LOW);
  digitalWrite(in2,LOW);
  digitalWrite(in3,LOW);
  digitalWrite(in4,LOW);
  delay(2000);}

  //MOTOR_A COUNTERCLOCKWISE MAX SPEED
  if(Keyboard.press('R')){
  digitalWrite(in1,LOW);
  digitalWrite(in2,HIGH);
  analogWrite(ena, 255);}

  //MOTOR_B COUNTERCLOCKWISE MAX SPEE
  if(Keyboard.press('T'){
  digitalWrite(in3,LOW);
  digitalWrite(in4,HIGH);
  analogWrite(enb, 255);}
 
  delay(2000);

  //STOP
  digitalWrite(in1,LOW);
  digitalWrite(in2,LOW);
  digitalWrite(in3,LOW);
  digitalWrite(in4,LOW);
  delay(2000);
 
}

void loop() {

 
}
