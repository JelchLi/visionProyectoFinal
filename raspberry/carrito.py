import RPi.GPIO as gpio
import time

#enumeracion del GPIO por posicion del BOARD
gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)


class car():
	def __init__(self, enable1, in1, in2, enable2, in3, in4):
		#declara las variables self para su uso en la clase
		#motor1
		self.enable1 = enable1
		self.in1 = in1
		self.in2 = in2
		#motor2
		self.enable2 = enable2
		self.in3 = in3
		self.in4 = in4
		
		#GPIO salida pwm1, in1, in2
		gpio.setup(self.enable1, gpio.OUT)
		gpio.setup(self.in1, gpio.OUT)
		gpio.setup(self.in2, gpio.OUT)
		#GPIO salida pwm2, in3, in4
		gpio.setup(self.enable2, gpio.OUT)
		gpio.setup(self.in3, gpio.OUT)
		gpio.setup(self.in4, gpio.OUT)
		
		#GPIO pwm1, pwm2 salida PWM
		self.pwm1 = gpio.PWM(self.enable1, 500)
		self.pwm2 = gpio.PWM(self.enable2, 500)
		
		#Define el comienzo del PWM
		self.pwm1.start(0)
		self.pwm2.start(0)
		
	def adelante(self):
		#cambia el DutyCicle a 100%
		self.pwm1.ChangeDutyCycle(20)
		gpio.output(self.in1, gpio.LOW)
		gpio.output(self.in2, gpio.HIGH)
		
		self.pwm2.ChangeDutyCycle(20)
		gpio.output(self.in3, gpio.LOW)
		gpio.output(self.in4, gpio.HIGH)
		print("yendo pa delante")

		
	def derecha(self):
		self.pwm1.ChangeDutyCycle(20)
		gpio.output(self.in1, gpio.LOW)
		gpio.output(self.in2, gpio.HIGH)
		
		self.pwm2.ChangeDutyCycle(10)
		gpio.output(self.in3, gpio.LOW)
		gpio.output(self.in4, gpio.HIGH)
		print("yendo pa la derecha")
		
	def izquierda(self):
		self.pwm1.ChangeDutyCycle(10)
		gpio.output(self.in1, gpio.LOW)
		gpio.output(self.in2, gpio.HIGH)
		
		self.pwm2.ChangeDutyCycle(20)
		gpio.output(self.in3, gpio.LOW)
		gpio.output(self.in4, gpio.HIGH)
		print("yendo pa la izquierda")
		
	def parar(self):
		self.pwm1.ChangeDutyCycle(0)
		self.pwm2.ChangeDutyCycle(0)
		
		gpio.output(self.in1, gpio.LOW)
		gpio.output(self.in2, gpio.LOW)
		gpio.output(self.in3, gpio.LOW)
		gpio.output(self.in4, gpio.LOW)
		print("ya pare")

		

def main():

	car.adelante()
	time.sleep(3)

	car.parar()
	time.sleep(3)

	car.derecha()
	time.sleep(3)

	car.parar()
	time.sleep(3)

	car.izquierda()
	time.sleep(3)

	gpio.cleanup()

if __name__ == "__main__":
		
	enable1 = 11
	in1 = 13
	in2 = 15
	enable2 = 16
	in3 = 18
	in4 = 22
	
	car = car(enable1, in1, in2, enable2, in3, in4)

	main()
