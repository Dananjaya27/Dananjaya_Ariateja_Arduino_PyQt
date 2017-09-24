/*
########################################################
#          -Sistem Berbasis Mikrokontroler-            #
# Displaying Ultrasonic Data from Arduino using Python #
#                                                      #
# Modified by   : Dananjaya Ariateja                   #
# Departement   : Electrical Engineering,              #
#                 Universitas Gadjah Mada              #
# Last Modified : 23 September 2017                    #
########################################################
*/
#include <NewPing.h>

#define LED 2
#define TRIGGER_PIN  12  // Arduino pin tied to trigger pin on the ultrasonic sensor.
#define ECHO_PIN     11  // Arduino pin tied to echo pin on the ultrasonic sensor.
#define MAX_DISTANCE 200 // Maximum distance we want to ping for (in centimeters). Maximum sensor distance is rated at 400-500cm.

NewPing sonar(TRIGGER_PIN, ECHO_PIN, MAX_DISTANCE); // NewPing setup of pins and maximum distance.

void setup() {
  Serial.begin(115200);
  pinMode(2, OUTPUT);
}

void loop() {
//  Serial.println(sonar.ping_cm()); 
  
  if (Serial.available()) {
    
    char serialListener = Serial.read();
    
    if (serialListener == 'H') {
      digitalWrite(LED, HIGH);
    }
    else if (serialListener == 'L') {
      digitalWrite(LED, LOW);
    }
    else if (serialListener == 'S') {
      Serial.println(sonar.ping_cm());
    }
  }
}
