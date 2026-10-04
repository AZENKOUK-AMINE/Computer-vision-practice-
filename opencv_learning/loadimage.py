import cv2 as cv 

img = cv.imread('C:\\Users\\amine\\OneDrive\\Desktop\\Coputer vision\\opencv_learning\\images\\par.jpg')

if img is None:
    print("image not found")
else :
    print("image found")
    print(img.shape)


cv.imshow("parfume", img)
cv.waitKey(3000)
