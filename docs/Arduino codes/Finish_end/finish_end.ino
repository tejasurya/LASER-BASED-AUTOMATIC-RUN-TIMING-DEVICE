#include<string.h>
char send[16]="abc";
/*
 * Developed by Teja Surya 
 * Finish line Arduino
 */
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
int LDR11 =3;
int LDR12 =2;
int LDR13 =1;
int LDR14 =0;
int LDR15 =14;
int LDR16 =15;
int LDR17 =18;
int LDR18 =19;
int LDR19 =20;
int LDR20 =21;
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
int laser11 = 43;
int laser12 = 42;
int laser13 = 41;
int laser14 = 40;
int laser15 =39;
int laser16 = 38;
int laser17 = 37;
int laser18= 36;
int laser19 =35;
int laser20 = 34;
void setup() {
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
pinMode(LDR11, INPUT);
pinMode(LDR12, INPUT);
pinMode(LDR13, INPUT);
pinMode(LDR14, INPUT);
pinMode(LDR15, INPUT);
pinMode(LDR16, INPUT);
pinMode(LDR17, INPUT);
pinMode(LDR18, INPUT);
pinMode(LDR19, INPUT);
pinMode(LDR20, INPUT);
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
pinMode(laser11, OUTPUT);
pinMode(laser12, OUTPUT);
pinMode(laser13, OUTPUT);
pinMode(laser14, OUTPUT);
pinMode(laser15, OUTPUT);
pinMode(laser16, OUTPUT);
pinMode(laser17, OUTPUT);
pinMode(laser18, OUTPUT);
pinMode(laser19, OUTPUT);
pinMode(laser20, OUTPUT);
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
digitalWrite(laser11, HIGH);
digitalWrite(laser12, HIGH);
digitalWrite(laser13, HIGH);
digitalWrite(laser14, HIGH);
digitalWrite(laser15, HIGH);
digitalWrite(laser16, HIGH);
digitalWrite(laser17, HIGH);
digitalWrite(laser18, HIGH);
digitalWrite(laser19, HIGH);
digitalWrite(laser20, HIGH);
}
void loop() {
  // put your main code here, to run repeatedly:
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
int hitState11 = digitalRead(LDR11);
int hitState12 = digitalRead(LDR12); 
int hitState13 = digitalRead(LDR13);
int hitState14 = digitalRead(LDR14); 
int hitState15 = digitalRead(LDR15);
int hitState16 = digitalRead(LDR16); 
int hitState17 = digitalRead(LDR17);
int hitState18 = digitalRead(LDR18); 
int hitState19 = digitalRead(LDR19);
int hitState20 = digitalRead(LDR20); 
//LDR goes low when it has been hit
if( Serial2.available()>0){
strcpy(send,"\0");
  if (hitState1 == 0)
  {
    strcat(send,"a");
    delay(1);
  }
  else if(hitState1 == 1)
  {
    strcat(send,"b");
    delay(1);
  }
  if (hitState2 == 0)
  {
    strcat(send,"c");
    delay(1);
  }
  else if(hitState2 == 1)
  {
    strcat(send,"d");
   delay(1);
   }
  if (hitState3 == 0)
  {
    strcat(send,"e");
  delay(1);
  }
  else if(hitState3 == 1)
  {
    strcat(send,"f");
   delay(1);
   }
   
     if (hitState4 == 0)
  {
    strcat(send,"g");
  delay(1);
  }
  else if(hitState4 == 1)
  {
    strcat(send,"h");
delay(1);
   }
   Serial2.println(send);
strcpy(send,"\0");
    if (hitState5 == 0)
  {
    strcat(send,"i");
  delay(1);
  }
  else if(hitState5 == 1)
  {
    strcat(send,"j");
   delay(1);
   }
  if (hitState6 == 0)
  {
    strcat(send,"k");
  delay(1);
  }
  else if(hitState6 == 1)
  {
    strcat(send,"l");
   delay(1);
   }
  if (hitState7 == 0)
  {
    strcat(send,"m");
  delay(1);
  }
  else if(hitState7 == 1)
  {
    strcat(send,"n");
   delay(1);
   }
     if (hitState8 == 0)
  {
    strcat(send,"o");
  delay(1);
  }
  else if(hitState8 == 1)
  {
    strcat(send,"p");
   delay(1);
   }
    Serial2.println(send);
strcpy(send,"\0"); 
   if (hitState9 == 0)
  {
    strcat(send,"q");
  delay(1);
  }
  else if(hitState9 == 1)
  {
    strcat(send,"r");
   delay(1);}
  if (hitState10 == 0)
  {
    strcat(send,"s");
  delay(1);}
  else if(hitState10 == 1)
  {
    strcat(send,"t");
   delay(1);}
  if (hitState11 == 0)
  {
    strcat(send,"u");
  delay(1);}
  else if(hitState11 == 1)
  {
    strcat(send,"v");
   delay(1);}
     if (hitState12 == 0)
  {
    strcat(send,"w");
  delay(1);}
  else if(hitState12 == 1)
  {
    strcat(send,"x");
   delay(1);}
    Serial2.println(send);
strcpy(send,"\0");
     if (hitState13 == 0)
  {
    strcat(send,"y");
  delay(1);}
  else if(hitState13 == 1)
  {
    strcat(send,"z");
   delay(1);}
  if (hitState14 == 0)
  {
    strcat(send,"1");
  delay(1);}
  else if(hitState14 == 1)
  {
    strcat(send,"2");
   delay(1);}
  if (hitState15 == 0)
  {
    strcat(send,"3");
  delay(1);}
  else if(hitState15 == 1)
  {
    strcat(send,"4");
   delay(1);}
     if (hitState16 == 0)
  {
    strcat(send,"5");
  delay(1);}
  else if(hitState16 == 1)
  {
    strcat(send,"6");
   delay(1);
   }
    Serial2.println(send);
  strcpy(send,"\0"); 
   if (hitState17 == 0)
  {
    strcat(send,"7");
  delay(1);
  }
  else if(hitState17 == 1)
  {
    strcat(send,"8");
   delay(1);}
  if (hitState18 == 0)
  {
    strcat(send,"9");
  delay(1);}
  else if(hitState18 == 1)
  {
    strcat(send,"!");
   delay(1);}
  if (hitState19 == 0)
  {
    strcat(send,"@");
  delay(1);}
  else if(hitState19 == 1)
  {
    strcat(send,"#");
   delay(1);}
     if (hitState20 == 0)
  {
    strcat(send,"$");
  delay(1);}
  else if(hitState20 == 1)
  {
    strcat(send,"%");
   delay(1);}
Serial2.println(send);
Serial.println(send);
}
}
