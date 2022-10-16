import cv2 as cv
img = cv.imread('C:/Users/Tabibyte/Desktop/shinji.jpg')
down_points = (400, 300)
shinji = cv.resize(img, down_points, interpolation = cv.INTER_LINEAR)
cv.imshow('shinjisass', shinji)

shinji_gray = cv.cvtColor(shinji, cv.COLOR_BGR2GRAY)
shinji_blur = cv.GaussianBlur(shinji_gray, (3, 3), 0)
cv.imshow('shinjisassgray', shinji_gray)
cv.imshow('shinjisassblurry', shinji_blur)


sobelx = cv.Sobel(src=shinji_blur, ddepth=cv.CV_64F, dx=1, dy=0, ksize=5)
sobely = cv.Sobel(src=shinji_blur, ddepth=cv.CV_64F, dx=0, dy=1, ksize=5)
sobelxy = cv.Sobel(src=shinji_blur, ddepth=cv.CV_64F, dx=1, dy=1, ksize=5)


cv.imshow('Sobel X', sobelx)
cv.imshow('Sobel Y', sobely)
cv.imshow('Sobel X Y using Sobel() function', sobelxy)

# Canny Edge Detection
shinjis_edges = cv.Canny(image=shinji_blur, threshold1=100, threshold2=200)  # Canny Edge Detection
# Display Canny Edge Detection Image
cv.imshow('Canny Edge Detection', shinjis_edges)
cv.waitKey()