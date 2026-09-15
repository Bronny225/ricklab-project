import time

import serial

# --- CONFIGURATION DE LA LIAISON SÉRIE VERS L'ARDUINO ---
# Sur Raspberry Pi, le port ressemble souvent à '/dev/ttyACM0' ou '/dev/ttyUSB0'
PORT_SERIE = "/dev/ttyACM0"
VITESSE = 9600

try:
  arduino = serial.Serial(PORT_SERIE, VITESSE, timeout=1)
  time.sleep(2)  # Attente de la stabilisation de la connexion
  print("[LAB-C137] Connecté à l'Arduino avec succès.")
except Exception as e:
  print(f"[AVERTISSEMENT] Impossible de joindre l'Arduino : {e}")
  arduino = None


def envoyer_commande(action):
  """Envoie un caractère unique à l'Arduino pour déclencher un composant physique."""
  if arduino and arduino.isOpen():
    arduino.write(action.encode("utf-8"))
    print(f"[COMMANDE] Envoyée à l'Arduino -> '{action}'")
  else:
    print(f"[SIMULATION] Arduino hors ligne. Action '{action}' ignorée.")


if __name__ == "__main__":
  print("--- RICK-OS : ASSISTANT DE LABORATOIRE INITIALISÉ ---")

  while True:
    choix = (
        input(
            "\nEntre une commande (H = Lumière, P = Portail, Q = Quitter) : "
        )
        .strip()
        .upper()
    )

    if choix == "H":
      print("Rick : 'J'ai allumé ce fichu néon.'")
      envoyer_commande("H")
    elif choix == "P":
      print("Rick : 'Ouverture du portail interdimensionnel C-137.'")
      envoyer_commande("P")
    elif choix == "Q":
      print("Rick : 'Je me casse.'")
      if arduino:
        arduino.close()
      break
    else:
      print("Rick : 'T'sais pas taper une lettre correcte ?'")