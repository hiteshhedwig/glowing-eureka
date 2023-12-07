# CAMERA
ITERATION = "1"


ENABLE_TRACEBACK_SAVE = False

CAMERA_CONFIGS = [
    {
        'index' : 0,
        'width' : 640,
        'height' : 480,
        'FPS ' : 30
    }
]

# iteration is basically a counter
FORMAT_FOLDER = "{date}-{purpose}-{vehicle}-{cameralens}-{iteration}"

FORMAT_FILENAME = "{date}-{purpose}-{vehicle}-{cameralens}-{randomstring}-{idx}.png"
PURPOSE = "demo"
VEHICLE = "f8"
CAMERA_LENS = "webcam"

PREFIX_PATH = "data/"

