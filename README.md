# Sorty

Sorty is a small Python script I built to organize my academic files by course.

During the semester, I downloaded a lot of PDFs, notes, assignments, and other class files whenever I needed them. Most of them ended up sitting in my Downloads folder, and I did not really organize them at the time. After a while, the folder became messy, so I wanted to make a simple script that could help sort those files automatically.

This project was also good practice for learning basic file management in Python.

## What It Does

Sorty takes a folder path from the user through the terminal. It then checks the files in that folder and sorts them into course folders based on keywords entered by the user.

For example, if a file name contains a course number like `426`, and the user has added that as a keyword for a course, the program can identify the match and move the file into the correct course folder.

The sorted course folders are created in the folder where the script is being run.

## Current Features

* Takes a source folder path as user input
* Lets the user enter course names and related keywords
* Scans file names from the selected folder
* Creates folders for each course
* Moves matching files into the correct course folder
* Works through the terminal
* Displays input prompts and output messages in the terminal

## Why I Made This

I made this because my Downloads folder was full of academic files from different classes. I wanted a faster way to organize them instead of manually checking and moving every file one by one.

This script helped me sort those files much more quickly, and it gave me practical experience with Python file management using modules like `pathlib` and `shutil`.

## Current Limitations

This is still a simple script, so there are some edge cases I still need to handle.

Some examples:

* The program does not fully handle invalid folder paths yet
* File names must contain matching keywords for the program to sort them correctly
* Files without matching keywords may not be organized the way I want yet
* The program currently depends completely on terminal input and output
* There is no graphical interface
* The sorting accuracy depends on how clear the course keywords are

## Status

This is a completed basic version of the script. It works for my current use case, but I may improve it later by adding better error handling and making the sorting process safer and more flexible.
