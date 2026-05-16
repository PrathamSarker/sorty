# Course File Sorter

Course File Sorter is an early-stage Python project for organizing academic files by course.

The goal of this project is to help sort files from a selected folder, such as a Downloads folder, into course-specific categories based on keywords in the file names.

## Current Progress

At this stage, the program can:

- Ask the user to enter a folder path
- Convert the entered path into a `Path` object
- Scan through the files and folders inside the given path
- Print the names of the items found in that folder

## Project Goal

The final goal is to build a script that can automatically organize academic files into folders for different courses.

For example, files with course-related keywords in their names, such as course numbers or course codes, can later be moved into matching course folders.

## Planned Features

- Detect course keywords from file names
- Create folders for each course
- Move matching files into the correct course folder
- Keep unmatched files separate
- Add safer testing before moving files
- Add a keyword configuration system later

## Status

This project is currently in the beginning stage.  
Right now, the focus is on safely reading a folder path and listing the files inside it before adding any file-moving features.
