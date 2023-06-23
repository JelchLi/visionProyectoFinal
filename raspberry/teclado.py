import pygame

def init():
	pygame.init()
	win = pygame.display.set_mode((100, 100))

def getkey(key):
	ans = False
	for eve in pygame.event.get():pass
	keyinput = pygame.key.get_pressed()
	mykey = getattr(pygame, f"K_{key}")
	
	if keyinput[mykey]:
		ans = True
		
	pygame.display.update()

	return ans
	
def close():
	pygame.quit()
	
def main():
	if getkey("a"):
		print("apretaste la a")
	if getkey("b"):
		print("apretaste la b")
	if getkey("c"):
		print("valiste verga")
		close()	
	
if __name__ == "__main__":
	init()
	while True:
		main()
	
