from os import listdir
import os
import shutil
from time import sleep

current_user = os.getlogin

source_path = f"C:/Users/{current_user}/Desktop"
target_path = f"C:/Users/{current_user}/Desktop/Training"
files = listdir(source_path)
filetypes = [
    '.txt',
    '.sql',
    '.png'
]


while True:
    print("Checking...")
    for file in files:
        file_path = os.path.join(source_path, file)
        file_name, file_extension = os.path.splitext(file_path)
        if (os.path.isfile(file_path)): 
            if(file_extension in filetypes):
                print(f"Moving {file}")
                shutil.move(file_path, target_path)
    print("Completed, waiting 5 minutes.")
    sleep(300)
