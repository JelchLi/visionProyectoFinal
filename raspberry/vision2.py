import cv2
import CNN
from torchvision import transforms
import torch

def init():
	capture = cv2.VideoCapture(0)
	print(capture)
	capture.set(cv2.CAP_PROP_FRAME_WIDTH, 224)
	capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 224)
	capture.set(cv2.CAP_PROP_FPS, 20)
	capture.set(10, 50)

	modelDeep = CNN.get_cnn()

	etiquetas_clase = ['adelante', 'derecha', 'izquierda'] 

	while True:
		success, img = capture.read()
		cv2.imshow("video", img)

		transform = transforms.Compose([
            transforms.Resize((224, 224)),  # Ajusta el tamaño de la imagen según sea necesario
            transforms.ToTensor()  # Convierte la imagen a un tensor
        ])

		img = transform(img)

		output = modelDeep.forward(img.unsqueeze(0))
		indice_prediccion = torch.argmax(output, dim=1).item()
		clase_predicha = etiquetas_clase[indice_prediccion]

		if clase_predicha == "adelante":
			print("adelante")
		if clase_predicha == "derecha":
			print("derecha")
		if clase_predicha == "izquierda":
			print("izquierda")

		if cv2.waitKey(1) & 0xFF == ord("q"):
			break

