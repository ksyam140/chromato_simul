import serial

port_serie = "/dev/serial0"
vitesse_serie = 9600

try:
    ser = serial.Serial(port_serie, vitesse_serie)
    trame = "a;390;01;08;02;00;03;0674020;04;09;05;72.0540P;06;26.6146P;07\r\n"
    ser.write(trame.encode())  # encode() est nécessaire pour convertir la chaîne en bytes
    print("Trame envoyée avec succès")
except serial.SerialException as e:
    print(f"Erreur de communication avec le port série: {e}")
finally:
    ser.close()