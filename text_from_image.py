import cv2
import pytesseract
import matplotlib.pyplot as  plt
img=cv2.imread("mobcam.png")
text=pytesseract.image_to_string(img)
print(text)
print("-------------------------------------Method 2 with image reshaping")
img2=cv2.imread("mobcam.png")
img2= cv2.resize(img2,None, fx=.5, fy=0.5)
print(img2.shape)
fig= plt.figure(figsize= [10,10])
plt.imshow(img2)
gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY) #convert to gray scale
fig = plt.figure(figsize= [20,20])
plt.imshow(gray)
text=pytesseract.image_to_string(img2)
print(text)