/*
 * Developed by Teja Surya
 * Starting Arduino
 */
char send[16]="abc";
int LDR1 =13;
int LDR2 =12;
int LDR3 =11;
int LDR4 =10;
int LDR5 =9;
int LDR6 =8;
int LDR7 =7;
int LDR8 =6;
int LDR9 =5;
int LDR10 =4;
int laser1 = 53;
int laser2 = 52;
int laser3 = 51;
int laser4 = 50;
int laser5 = 49;
int laser6 = 48;
int laser7 = 47;
int laser8 = 46;
int laser9 = 45;
int laser10 = 44;
void setup()
{
  //In Arduino Mega Rx=Rx2,Tx=Tx2
  Serial.begin(9600);
  Serial2.begin(9600); 
  pinMode(LDR1, INPUT);
pinMode(LDR2, INPUT);
pinMode(LDR3, INPUT);
pinMode(LDR4, INPUT);
pinMode(LDR5, INPUT);
pinMode(LDR6, INPUT);
pinMode(LDR7, INPUT);
pinMode(LDR8, INPUT);
pinMode(LDR9, INPUT);
pinMode(LDR10, INPUT);
pinMode(laser1, OUTPUT);
pinMode(laser2, OUTPUT);
pinMode(laser3, OUTPUT);
pinMode(laser4, OUTPUT);
pinMode(laser5, OUTPUT);
pinMode(laser6, OUTPUT);
pinMode(laser7, OUTPUT);
pinMode(laser8, OUTPUT);
pinMode(laser9, OUTPUT);
pinMode(laser10, OUTPUT);
digitalWrite(laser1, HIGH);
digitalWrite(laser2, HIGH);
digitalWrite(laser3, HIGH);
digitalWrite(laser4, HIGH);
digitalWrite(laser5, HIGH);
digitalWrite(laser6, HIGH);
digitalWrite(laser7, HIGH);
digitalWrite(laser8, HIGH);
digitalWrite(laser9, HIGH);
digitalWrite(laser10, HIGH);
 }
void loop()
{ 
  int hitState1 = digitalRead(LDR1);
int hitState2 = digitalRead(LDR2); 
int hitState3 = digitalRead(LDR3);
int hitState4 = digitalRead(LDR4); 
int hitState5 = digitalRead(LDR5);
int hitState6 = digitalRead(LDR6); 
int hitState7 = digitalRead(LDR7);
int hitState8 = digitalRead(LDR8);
int hitState9 = digitalRead(LDR9);
int hitState10 = digitalRead(LDR10);
if( Serial2.available()>0){
  strcpy(send,"\0");
  if (hitState1 == 0)
  {
    Serial2.println("a");
    delay(1);        // delay in between reads for stability
  }
  else if(hitState1 == 1)
  {
    Serial2.println("b");
    delay(1);
   }
  if (hitState2 == 0)
  {
    Serial2.println("c");
    delay(1);        // delay in between reads for stability
  }
  else if(hitState2 == 1)
  {
    Serial2.println("d");
    delay(1);
   }
  if (hitState3 == 0)
  {
    Serial2.println("e");
    delay(1);        // delay in between reads for stability
  }
  else if(hitState3 == 1)
  {
    Serial2.println("f");
    delay(1);
   }
     if (hitState4 == 0)
  {
    Serial2.println("g");
    delay(1);        // delay in between reads for stability
  }
  else if(hitState4 == 1)
  {
    Serial2.println("h");
    delay(1);
   }
  if (hitState5 == 0)
  {
    Serial2.println("i");
    delay(1);        // delay in between reads for stability
  }
  else if(hitState5 == 1)
  {
    Serial2.println("j");
    delay(1);
   }
  if (hitState6 == 0)
  {
    Serial2.println("k");
    delay(1);        // delay in between reads for stability
  }
  else if(hitState6 == 1)
  {
    Serial2.println("l");
    delay(1);
   }
  if (hitState7 == 0)
  {
    Serial2.println("m");
    delay(1);        // delay in between reads for stability
  }
  else if(hitState7 == 1)
  {
    Serial2.println("n");
    delay(1);
   }
   if (hitState8 == 0)
  {
    Serial2.println("o");
    delay(1);        // delay in between reads for stability
  }
  else if(hitState8 == 1)
  {
    Serial2.println("p");
    delay(1);
   } 
     if (hitState9 == 0)
  {
    Serial2.println("q");
    delay(1);        // delay in between reads for stability
  }
  else if(hitState9 == 1)
  {
    Serial2.println("r");
    delay(1);
   }
   if (hitState10 == 0)
  {
    Serial2.println("s");
    delay(1);        // delay in between reads for stability
  }
  else if(hitState10 == 1)
  {
    Serial2.println("t");
    delay(1);
   }
}
}
