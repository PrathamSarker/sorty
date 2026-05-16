import os
from pathlib import Path
import shutil

source_folder = input("Enter a valid Path for source folder: ")       #input path from user

source_folder = Path(source_folder)     #converting string to path object

for file_name in source_folder.iterdir():
    print(file_name.name)