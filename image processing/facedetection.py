import cv2
fd = cv2.CascadeClassifier( cv2.data.haarcascades + "haarcascade_frontalface_default.xml ")
#to read video using web camera
vid = cv2.VideoCapture(0)

#loop to read and show image until we bereak the loop 
while True:
    flag , img = vid.read()
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
 
    # if flag is true then only show image
    if flag:
        faces = fd.detectMultiScale(img_gray,1.1,5)
        for x,y,w,h in faces:
           # Draw a rectangle on img
            cv2.rectangle(img , pt1 =(x,y), pt2 =(x+w,y+h), color = (255, 100,0), thickness = 3 )
        cv2.imshow("webcam_image",img)
        key = cv2.waitKey(1)
        if key == ord("v"):
            break
    else:
        break
cv2.destroyAllWindows()
vid.release()