from carrito import car
import teclado
import time
import RPi.GPIO as gpio

enable1, in1, in2 = 11, 13, 15
enable2, in3, in4 = 16, 18, 22

car = car(enable1, in1, in2, enable2, in3, in4)

teclado.init()


def main():
	if teclado.getkey("UP"):
		car.adelante()
	if teclado.getkey("LEFT"):
		car.izquierda()
	if teclado.getkey("RIGHT"):
		car.derecha()
	elif teclado.getkey("DOWN"):
		car.parar()
	elif teclado.getkey("q"):
		print("valio verga")
		gpio.cleanup()
		teclado.close()

		on = False

if __name__ == "__main__":
	on = True
	while on:
		main()
	print("si sali bro")
