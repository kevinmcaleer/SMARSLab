// SMARS Bluetooth remote control
// Kevin McAleer
// April 2019

//int ch_A_Brake = 9;
//int ch_B_Brake = 8;
int ch_A_Direction = 12;
int ch_B_Direction = 13;
int ch_A_speed = 10;
int ch_B_speed = 11;
char state = 0;
int delaylength = 1000;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600, SERIAL_8N1);
  Serial.println("SMARSFan OS 1.0");
  Serial.println("---------------");

  // establish motor direction toggle pins
  pinMode(ch_A_Direction, OUTPUT);
  pinMode(ch_B_Direction, OUTPUT);

  // establish motor brake pins
  //  pinMode(ch_A_Brake, OUTPUT);
  //  pinMode(ch_B_Brake, OUTPUT);
}

void forward() {
  // Move Forward
  digitalWrite(ch_A_Direction, LOW); // set direction to forward
  digitalWrite(ch_B_Direction, HIGH); // set direction to forward

  analogWrite(ch_A_speed, 255); // full speed ahead
  analogWrite(ch_B_speed, 255); // full speed ahead

  delay(delaylength);

  analogWrite(ch_A_speed, 0); // stop
  analogWrite(ch_B_speed, 0); // stop


  //  Serial.flush();
}

void backward() {
  // Move Backward

  digitalWrite(ch_A_Direction, HIGH); // set direction to backward
  digitalWrite(ch_B_Direction, LOW); // set direction to backward

  analogWrite(ch_A_speed, 255); // full speed ahead
  analogWrite(ch_B_speed, 255); // full speed ahead

  delay(delaylength);

  analogWrite(ch_A_speed, 0); // stop
  analogWrite(ch_B_speed, 0); // stop

  //  Serial.flush();
}

void left() {
  // Move left

  digitalWrite(ch_A_Direction, HIGH); // set direction to left
  digitalWrite(ch_B_Direction, HIGH); // set direction to left

  analogWrite(ch_A_speed, 255); // full speed ahead
  analogWrite(ch_B_speed, 255); // full speed ahead

  delay(delaylength);

  analogWrite(ch_A_speed, 0); // stop
  analogWrite(ch_B_speed, 0); // stop

  //  Serial.flush();
}

void right() {
  // Move right

  digitalWrite(ch_A_Direction, LOW); // set direction to right
  digitalWrite(ch_B_Direction, LOW); // set direction to right

  analogWrite(ch_A_speed, 255); // full speed ahead
  analogWrite(ch_B_speed, 255); // full speed ahead

  delay(delaylength);

  analogWrite(ch_A_speed, 0); // stop
  analogWrite(ch_B_speed, 0); // stop

  //  Serial.flush();
}

void fullstop() {
  // stop!

  digitalWrite(ch_A_Direction, HIGH); // set direction to right
  digitalWrite(ch_B_Direction, HIGH); // set direction to right

  analogWrite(ch_A_speed, 0); // full speed ahead
  analogWrite(ch_B_speed, 0); // full speed ahead

  delay(delaylength);

  //  Serial.flush();
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0 ) {
    state = Serial.read();
    Serial.println(state);

    if (state == 'u') {
      Serial.println("MOTORS: UP");
      forward(); // move forward
      state = 0;
    }

    else if (state == 'd') {
      Serial.println("MOTORS: DOWN");
      backward();
      state = 0;
    }

    else if (state == 'l') {
      Serial.println("MOTORS: LEFT");
      left();
      state = 0;
    }

    else if (state == 'r') {
      Serial.println("MOTORS: RIGHT");
      right();
      state = 0;
    }

    else if (state == "s") {
      Serial.println("MOTORS: STOP");
      fullstop();
      state = 0;

    }
  }
}
