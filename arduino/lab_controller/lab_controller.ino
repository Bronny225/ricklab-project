#include <Servo.h>

// --- CONFIGURATION DES BROCHES (PINS) ---
const int PIN_SERVO = 9;   // Le servomoteur pour le portail interdimensionnel
const int PIN_LED = 13;    // Une LED témoin pour l'état du labo

Servo monPortail;
char commandeRecue = ' ';

void setup() {
  // Initialisation de la liaison série à la même vitesse que le Raspberry Pi
  Serial.begin(9600);
  
  // Configuration du matériel
  monPortail.attach(PIN_SERVO);
  pinMode(PIN_LED, OUTPUT);
  
  // Position initiale du portail (fermé à 0 degré)
  monPortail.write(0);
  digitalWrite(PIN_LED, LOW);
  
  Serial.println("ARDUINO_PRET");
}

void loop() {
  // Vérifie si des données sont disponibles sur le port série
  if (Serial.available() > 0) {
    commandeRecue = Serial.read();

    // Traitement de la commande reçue
    if (commandeRecue == 'H') {
      digitalWrite(PIN_LED, HIGH);
      Serial.println("ACTION_OK: LED ALLUMEE");
    } 
    else if (commandeRecue == 'P') {
      Serial.println("ACTION_OK: OUVERTURE PORTAIL");
      monPortail.write(90);  // Ouvre le portail
      delay(3000);           // Laisse ouvert 3 secondes
      monPortail.write(0);   // Referme le portail
      Serial.println("ACTION_OK: FERMETURE PORTAIL");
    }
  }
}