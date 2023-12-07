import datetime
import random
import string
import os
from loguru import logger as log
from src.config import *

def folder_name(purpose, vehicle, cameralens):
    current_date = datetime.datetime.now().strftime("%y%m%d")
    foldername = FORMAT_FOLDER.format(
        date=current_date,
        purpose=purpose, 
        vehicle=vehicle, 
        cameralens=cameralens,
        iteration=ITERATION
    )
    return f"{PREFIX_PATH}{foldername}"

def generate_folder(purpose, vehicle, cameralens):
    folder = folder_name(purpose, vehicle, cameralens)
    create_folder(f"{folder}")

def create_folder(path):
    if os.path.exists(path):
        log.warning(f"{path} already exists! Reusing it")
        return True
    else :
        os.makedirs(path)
        log.success(f"folder created : {path}")
        return False

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
    foldername = folder_name(purpose=purpose, 
                             vehicle=vehicle, 
                             cameralens=cameralens, 
                             )
    
    return f"{foldername}/{filename}"

if __name__ == '__main__':
    generate_folder("try","f5","8mm", "1")
    print(generate_filename("try","f5","8mm", "1"))