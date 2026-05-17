import os
from pathlib import Path
import shutil

source_folder = input("Enter a valid Path for source folder: ")       #input path from user

source_folder = Path(source_folder)     #converting string to path object


course_list = []
course_name = ""

while(course_name != 'done'):
    course_name = input("Enter course name (Enter 'done' to finish): ")
    if course_name == 'done':
        break
    course_list.append(course_name)

print(f"These are all the courses: {course_list}")


for names in course_list:
    os.makedirs(names, exist_ok = True)
    print(f"folder created: {names}")








#for file in source_folder.iterdir():
#    print(file.name)

