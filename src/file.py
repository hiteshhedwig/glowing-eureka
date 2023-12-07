import datetime
import random
import string
from src.config import *

def generate_filename(purpose, vehicle, cameralens, idx):
    current_date = datetime.datetime.now().strftime("%y_%m_%d_%H%M%S")
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=4))
    filename = FORMAT_FILENAME.format(
        date=current_date, 
        purpose=purpose, 
        vehicle=vehicle, 
        cameralens=cameralens, 
        randomstring=random_string,
     
        idx = idx
    )
    return f"{PREFIX_PATH}{filename}"

if __name__ == '__main__':
    print(generate_filename("try","f5","8mm","1"))