import cv2
import numpy as np

def onTrackbarChange(max_slider):
    cimg = np.copy(img)
    p1 = max_slider
    p2 = max_slider * 0.4
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, cimg.shape[0]/64, param1=p1, param2=p2, minRadius=25, maxRadius=50)
    if circles is not None:
        cir_len = circles.shape[1]
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            cv2.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)
            cv2.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)
    else:
        cir_len = 0
    cv2.imshow('Image', cimg)    
    edges = cv2.Canny(gray, p1, p2)
    cv2.imshow('Edges', edges)
if __name__ == "__main__":
    img = cv2.imread(R'C:\Users\...\Py\teste\imagem.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.namedWindow("Edges")
    cv2.namedWindow("Image")
    initThresh = 105 
    maxThresh = 200 
    cv2.createTrackbar("Threshold", "Image", initThresh, maxThresh, onTrackbarChange)
    onTrackbarChange(initThresh)
    while True:
        key = cv2.waitKey(1)
        if key == 27:
            break
    cv2.destroyAllWindows()