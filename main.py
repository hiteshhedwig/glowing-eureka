from src.config import *
from src.streamer import Streamer
from src.file import generate_filename
from src.utils import Counter
from loguru import logger as log

def loop(streamer, camera_indices):
    counter = Counter(checkpoint=5)
    while True:
        frame = streamer.get_frames(camera_indices[0])
        save = counter.is_checkpoint()
        if frame is not None and save :
            filename = generate_filename(
                purpose    = PURPOSE,
                vehicle    = VEHICLE,
                cameralens = CAMERA_LENS,
                idx        = counter.get_count()
            )
            streamer.save_image(frame, filename)

def main():
    log.info(f"Initiating the logging...")
    streamer = Streamer(CAMERA_CONFIGS)
    log.info(f"SUCCESSFULLY opened {streamer.get_opened_cams()} camera")
    camera_indices = streamer.get_cam_index()
    log.info(f"Camera indices accessed by the system : {camera_indices}")

    loop(streamer, camera_indices)
    


if __name__ == '__main__':
    # 1. Create streamer object
    # 2. Open and get images
    # 3. Save with correct convention
    # log.add("tracebacks/file_{time}.log", format="{time} {level} {message}", level="INFO", rotation="50 MB")
    main()