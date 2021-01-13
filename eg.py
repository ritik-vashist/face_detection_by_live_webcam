import cv2 #imported cv2 library
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') #linked haarcascade file
webcam = cv2.VideoCapture(0) #to take access to your camera
while True:
    successfull_frame_read, frame = webcam.read() #to read the the frame from webcam
    grayscaled_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) # to change image into black-white mode
    face_cordinates = trained_face_data.detectMultiScale(grayscaled_img) #to obtain cordinates of face
    for (x, y, w, h) in face_cordinates: #for loop for multiple faces in image
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0,255,0), 2) #to draw rectangle on face
    cv2.imshow('face detection program',frame) #to show the final frame with face detections
    key=cv2.waitKey(1) #to hold screen
    if key==81 or key ==113: #to exit the frame
        break









