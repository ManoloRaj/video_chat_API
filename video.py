import cv2

class Video (object):
    
    def __init__(self):
        self.cap=cv2.VideoCapture(0)
    
    def __del__(self):
        self.cap.release()
    
    def get_frame(self):
        _,image=self.cap.read()
        ret, jpeg = cv2.imencode('.jpg',image)
        return jpeg.tobytes()

if __name__ == '__main__':
    vid = Video()