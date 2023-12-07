from src.camera import Camera

class Streamer(object):
    def __init__(self, configs = []):
        self.cameras = {}
        for config in configs:
            self.cameras[config['index']] = Camera(**config)

    def get_frames(self, index):
        return self.cameras[index].get_frame()
    
    def get_opened_cams(self):
        return len([cam for _, cam in self.cameras.items() if cam.is_opened()])
    
    def get_cam_index(self):
        return [idx for idx, cam in self.cameras.items() if cam.is_opened()]

    def save_image(self, image, filename):
        self.cameras[self.get_cam_index()[0]].save_image(image, filename)

    def get_cameras(self):
        return self.cameras
    
    def __len__(self):
        return len(self.cameras)