# 🔬 RickLab / Rick-OS: Advanced Laboratory Automation & Biometric Security System

> *"Empreinte vocale validée. Bienvenue dans le labo, chef."* — Rick-OS

---

## 📋 Présentation du Projet
**RickLab** est un système intelligent de contrôle d'accès et d'automatisation de laboratoire hautement sécurisé, inspiré de l'univers de *Rick & Morty*. Développé dans le cadre d'un projet collaboratif, il combine l'intelligence artificielle sur **Raspberry Pi**, l'électronique embarquée sur **Arduino**, et une **Interface Graphique (GUI)** synchronisée.

---

## 🚀 Fonctionnalités Clés & Architecture

### 1. 🎙️ Sécurité Biométrique Vocale (Raspberry Pi & Core System)
* Développé et piloté par **LOLOGBO MARC**, le système écoute en temps réel la voix de l'utilisateur via le Raspberry Pi.
* Pipeline d'analyse spectrale et d'embedding vectoriel par **similarité cosinus** pour authentifier ou rejeter l'accès.
* **En cas de succès :** Validation et ouverture du portail/vortex.
* **En cas d'intrusion :** Déclenchement d'une alarme critique (buzzer et flash de LED rouges).

### 2. 💡 Éclairage Progressif par Détection de Proximité
* Capteur de présence relié au système Arduino.
* Plus l'utilisateur avance dans le laboratoire, plus les lumières s'allument séquentiellement.

### 3. 🌀 Contrôle du Vortex Interdimensionnel
* Intégration d'un mini-ventilateur piloté par le kit Arduino pour simuler l'ouverture/fermeture d'un vortex.

### 4. 🖥️ Synchronisation LCD & Interface Graphique (GUI)
* Un écran LCD physique affiche les messages d'accueil de la machine (ex: *"Bonjour Rick"*).
* Une **Interface Graphique (GUI)** dédiée est synchronisée en temps réel pour refléter exactement les mêmes statuts sur poste de travail.

---

## 📂 Structure du Dépôt GitHub

```text
ricklab-project/
│
├── raspberry_pi/             # Cœur du système & Reconnaissance vocale (LOLOGBO MARC)
│   ├── main.py               # Script principal d'écoute et de pilotage série
│   └── enregistrer_ref.py    # Enrôlement de l'empreinte vocale de référence
│
├── gui/                      # Interface Graphique synchronisée (Développé par l'équipe)
│   └── app_gui.py            # Application GUI (messages et états du labo)
│
├── arduino/                  # Code embarqué (Actionneurs physiques)
│   └── ricklab_controller.ino# Gestion du LCD, LEDs, buzzer, mini-ventilateur & capteurs
│
├── docs/                     # Livrables administratifs & académiques
│   ├── cahier_des_charges.pdf# Cahier des charges du projet
│   ├── presentation.pptx     # Support de présentation (PowerPoint)
│   └── ...                   # Autres documents de suivi
│
├── requirements.txt          # Dépendances Python globales
└── README.md                 # Documentation officielle du dépôt
