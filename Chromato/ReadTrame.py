###############################################################################
# Module informations
###############################################################################
__project__ = "ECOTRON IDF - Entrer la trame et l'enregistrer "
__author__ = "Kadir Yildirim (yildirim4002@gmail.com)"
__modifiers__ = ""
__history__ = """
    - Revision 1.0 (2024/06/04) : First Version.
              """
__date__ = "2024/06/04"
__version__ = "1.0.0"


###############################################################################
import json
import serial

# Name of the file where all trames will be stored
fichier_trames = "toutes_les_trames.json"
# Serial port and communication speed
port_serie = "/dev/serial0"  
vitesse_serie = 9600  

# Function to add a new trame and save it to the file
def add_trame(trame):
    # Convert string to list
    chaine_a_verifier = trame.split(";")
    
    # Save the new trame to the file, each trame on a new line
    with open(fichier_trames, "a") as fichier:
        fichier.write(json.dumps(chaine_a_verifier) + "\n")

    # Update the display
    check_chaine(chaine_a_verifier)

# Function to check the string and update the status of the bell
def check_chaine(chaine_a_verifier):
    # Extract the stream number at position "04; 09" (index 9)
    num_stream = chaine_a_verifier[9]

    # Check and display bell status based on stream number
    if num_stream == "09":
        print("Bell : Open ")
    elif num_stream == "08":
        print("Bell : Close ")
    else:
        print("Bell : Unknown ")

    # Show Stream Number
    print(f"Numéro de stream : {num_stream}")

    # View Updated String
    updated_chaine = ";".join(chaine_a_verifier)
    print(f"Chaîne actuelle : {updated_chaine}")

# Function to read trames from the serial port
def read_trames():
    with serial.Serial(port_serie, vitesse_serie) as ser:
        while True:            
            trame = ser.readline().decode()
            print(trame)
            trame = trame.strip()
            print(trame)
            add_trame(trame)

# Start reading trames from the serial port
read_trames()
