# Importamos la libreira de PySerial
import serial

# Abrimos el puerto del arduino a 9600
PuertoSerie = serial.Serial('COM13', 9600)
# Creamos un buble sin fin
while True:
  # leemos hasta que encontarmos el final de linea
  sArduino = int(PuertoSerie.readline())
  # Mostramos el valor leido y eliminamos el salto de linea del final
  print ("Valor Arduino: " + str(sArduino))