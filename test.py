import os
from pathlib import Path
import shutil

source_folder = input("Enter a valid Path for source folder: ")       #input path from user

source_folder = Path(source_folder)     #converting string to path object


course_dict = {}
course_name = ""
input_string = ""
value_string = ""

#course and keywords entry in the dictionary
while(input_string != 'done'):
    input_string = input("Enter course name (Enter 'done' to finish): ")
    if input_string == 'done':
        break
    course_dict[input_string] = [] 
    while (value_string != 'done'):
        value_string = input(f"Enter keywords for {input_string} (Enter 'done' to finish): ")
        if value_string == 'done':
            break
        course_dict[input_string].append(value_string)
    value_string = ""


print(f"\nThese are all the courses: {course_dict}")

#folder creation for the courses
for keys in course_dict:
    if os.path.exists(keys):
        print(f"Folder *{keys}* already exists")
    else:
        os.makedirs(keys, exist_ok= True)
        print(f"Folder created for *{keys}*")



print("\n\n.................Executing the transfer......................\n")

#transfer of files
for file in source_folder.iterdir():
    file_name = file.name.lower().strip()
    if 'pdf' not in file_name:      #scanning through PDF filetype only
        continue
    for course, keywords in course_dict.items():
        for keyword in keywords:
            if keyword in file_name:  
                print(f"\nMatch found for *{course}*")
                course_folder = Path(course)
                shutil.move(file, course_folder / file_name)
                print(f"Moved *{file_name}* from *{source_folder.name}* to *{course_folder.name}*")
                break

print("\n.....................Transfer complete.......................")
