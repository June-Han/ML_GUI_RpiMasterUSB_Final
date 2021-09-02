
#include <Servo.h>
const int buzzer = 6; //buzzer to arduino pin 6
const int sw = 8;

Servo Myservo;

void setup()
{
  Serial.begin(9600);
  pinMode(13, OUTPUT); // Fan
  pinMode(12, OUTPUT); // Pump
  pinMode(11, OUTPUT); // LED Light Strips
  pinMode(10, OUTPUT); // LED RED
  pinMode(9, OUTPUT); // LED GREEN
  // Switch [Not Required For RSPB Master- Arduino Slave] pinMode(sw, INPUT); 
  Myservo.attach(7); //servo.attach(pin) set pin to motor
  pinMode(6, OUTPUT); // buzzer 
}

void loop() {  
  
  if (Serial.available() > 0) {  
  
    String data = (Serial.readStringUntil('\n'));  
  
    Serial.print("Status ");   
    Serial.println(data);  
  
    if (data.equals("Wash")) {  
      washing();
      drying();
    } 
    else if(data.equals("StartSter"))
    {
      ster();
      done(); 
    }
    else if(data.equals("Abort")) 
    { 
      exit(0);
    }
    else if(data.equals("DHTERROR")) 
    { 
      digitalWrite(10, HIGH); // Red LED ON (Component Error)
      buzz();
      Serial.println("DHT ERROR, Please check component");
    }  
    else if(data.equals("LIGHTERROR")) 
    { 
      digitalWrite(10, HIGH); // Red LED ON (Component Error)
      buzz();
      Serial.println("LIGHT ERROR, Please check component");
    } 
}
}

void washing ()
{
  // Start of Operation (WASHING)
  delay (5000);
  Myservo.write(90);
  Serial.println("Closing Lid\n");
  delay (3000);
  Serial.println("Lid Closed and Secured\n"); 
  
  Serial.println("Job Operation Starts\n"); 
  Serial.println("Process 1: Washing Starts");
  delay (2000);      
  digitalWrite(13, LOW); // Fan off (WASHING)
  digitalWrite(11, LOW); // LED Light Strips off
  digitalWrite(9, LOW);  // Green LED off (In Process)
  digitalWrite(12, HIGH); // Pump on (WASHING)
  digitalWrite(10, HIGH); // Red LED ON (In Process)
      
  delay(20000); // Wait for x min (WASHING)
  Serial.println("Process 1: Washing Completed\n");
        
}

void drying ()
{
  // Washing Done, Now Drying
  Serial.println("Process 2: Drying Starts");
  Serial.println("Drying Starts -> Both Fan ON");
        
  digitalWrite(13, HIGH); // Fan ON (DRYING)
  digitalWrite(10, HIGH); // Red LED ON (In Process)
  digitalWrite(12, LOW); // Pump off (DRYING)
  digitalWrite(11, LOW); // LED Light Strips off (DRYING)
  digitalWrite(9, LOW); // Green LED off (In Process)
      
  delay(20000); // Wait for x min (DRYING)
  Serial.println("Process 2: Drying Completed\n");
  Serial.println("Completed\n");
  digitalWrite(13, LOW); // Fan ON (DRYING)
  delay(10000);         
}

void ster ()
{
  // Drying Done, Now Sterilisation
  delay(3000);
  Serial.println("Process 3: Sterilisation Starts");
  Serial.println("Sterilisation Starts -> UV Lights ON");
        
  digitalWrite(13, LOW); // Fan off (Sterilisation)
  digitalWrite(12, LOW); // Pump off (Sterilisation)
  digitalWrite(11, HIGH); // LED Light Strips off (Sterilisation)
  digitalWrite(10, HIGH); // Red LED ON (In Process)
  digitalWrite(9, LOW); // Green LED off (In Process)
        
  delay(20000); // Wait for x min (Sterilisation)
  Serial.println("Process 3: Sterilisation Completed\n");
  
}

        
void done ()
{
  // Sterilisation Done, Process Completed
  Serial.println("Job Operation Completed");
  digitalWrite(13, LOW); // Fan off (Sterilisation)
  digitalWrite(12, LOW); // Pump off (Sterilisation)
  digitalWrite(11, LOW); // LED Light Strips off (Sterilisation)
  digitalWrite(10, LOW); // Red LED ON (In Process)
  digitalWrite(9, HIGH); // Green LED off (In Process)
  delay(5000);
        
  Myservo.write(0); // Original Position (No Process Currently)
  buzz();
  Serial.println("JCompleted\n");
}


void buzz()
{
  tone(buzzer, 1000); // Alarm buzzer
  Serial.println("Alarm ON : Please collect your syringes");
  delay(5000);        // alarm for 3s
  noTone(buzzer); // stop alarm
  delay(3000);
}
