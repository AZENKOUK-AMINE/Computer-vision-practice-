import cv2 as cv


img = cv.imread('C:\\Users\\amine\\OneDrive\\Desktop\\Coputer vision\\opencv_learning\\images\\par.jpg')


# rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

cv.imshow('Gray Image', gray)




cv.waitKey(0)
cv.destroyAllWindows()