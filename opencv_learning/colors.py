import cv2 as cv


img = cv.imread('C:\\Users\\amine\\OneDrive\\Desktop\\Coputer vision\\opencv_learning\\images\\par.jpg')


rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
# cv.imshow('RGB Image', rgb)
cv.imshow('RGB Image', img)

cv.waitKey(0)
cv.destroyAllWindows()