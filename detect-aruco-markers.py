import cv2

cap = cv2.VideoCapture(0)

dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_250)
parameters = cv2.aruco.DetectorParameters()
detector = cv2.aruco.ArucoDetector(dictionary, parameters)

while True:
    ret, frame = cap.read()

    markerCorners, markerIds, rejectedCandidates = detector.detectMarkers(frame)
  
    new_frame = cv2.aruco.drawDetectedMarkers(frame, markerCorners, markerIds)

    cv2.imshow('Found markers', new_frame)

    if cv2.waitKey(2) & 0xFF == ord('q'):
        break
