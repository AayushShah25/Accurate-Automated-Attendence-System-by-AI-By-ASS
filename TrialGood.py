import face_recognition

import numpy as np
from numpy import array,float32

import cv2
from keras.models import load_model
import matplotlib.pyplot as plt


model=load_model('./DATA/facenet_keras.h5')


all_face_encodings = {}
#same = []

img1 = cv2.imread("./10.png")
img1 = cv2.resize(img1, (160,160))
img1 = img1.reshape((1,160,160,3))
img1 = img1 / 255.0


all_face_encodings["Person1"] = model.predict(img1)[0]

img2 = cv2.imread("./18.png")
img2 = cv2.resize(img2, (160,160))
img2 = img2.reshape((1,160,160,3))
img2 = img2/255.0


same = []
same.append(model.predict(img2)[0])
same.append(model.predict(img2)[0])

all_face_encodings["Person2"] = model.predict(img2)[0]


# Grab the list of names and the list of encodings
face_names = list(all_face_encodings.keys())

face_encodings = np.array(list(all_face_encodings.values()))

kaka = face_encodings.__repr__()
len(kaka)



backArray = eval(kaka)




len(list(all_face_encodings.values()))
# Try comparing an unknown image





unknown_image = cv2.imread("./70.png")
unknown_image = cv2.resize(unknown_image, (160,160))
unknown_image = unknown_image.reshape((1,160,160,3))
unknown_image = unknown_image / 255.0

unknown_face = model.predict(unknown_image)[0]

result = face_recognition.compare_faces(face_encodings, unknown_face)
result

# Print the result as a list of names with True/False
names_with_result = list(zip(face_names, result))
print(names_with_result)