import cv2
from loguru import logger as log

class Camera(object):
    def __init__(self, **kwargs):
        # Set default values
        index = kwargs.get('index', 0)
        width = kwargs.get('width', 640)
        height = kwargs.get('height', 480)

        self.cap = cv2.VideoCapture(index)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        log.info(f"Opened camera with index: {index}, width  : {self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)}, height : {self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)}, FPS : {self.cap.get(cv2.CAP_PROP_FPS)},")

    def get_frame(self):
        ret, frame = self.cap.read()
        if ret:
            return frame
        else:
            return None
        
    def save_image(self, image, filename):
        ok = cv2.imwrite(filename, image)
        if ok:
            log.info(f"saving image to path {filename}")
        else :
            log.warning(f"facing an error while saving image to {filename}")

    def is_opened(self):
        return self.cap.isOpened()

    def release(self):
        self.cap.release()

if __name__ == '__main__':
    cam = Camera()
    print(cam.is_opened())
