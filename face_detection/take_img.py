import time

def takePicture():
    import cv2

    cam = cv2.VideoCapture(0)

    time.sleep(1)
    ret, frame = cam.read()

    img_name = "opencv_frame.png"
    cv2.imwrite(img_name, frame)

    cam.release()
    cv2.destroyAllWindows()

takePicture()
