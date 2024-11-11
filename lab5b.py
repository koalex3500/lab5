#!/usr/bin/env python3
#This function will be defined as read_file_string
def read_file_string(filename):
 """This will read the entire file  as a string and returns the string"""
 try:
  with open(filename, 'r') as file:
  #This line will read the entire data.txt file as a single string.
   content = file.read() 
   return content
 except FileNotFoundError:
 #This part will return file cannot be found 
  return "File cannot be found"

#This function will be defined as read_file_list
def read_file_list(filename):
 """THis  will read the file line by line and return the list of lines"""
 try:
  with open (filename, 'r') as file:
   lines = [line.strip() for line in file]
   return lines
 except FileNotFoundError:
  return ["File cannot be found"] 

#This function will be defined as append_file_string
def append_file_string(filename, string):
 """This will append a string to the data.txt file"""
 try:
  with open(filename, 'a') as file:
   file.write(string)
 except Exception as e:
  return f"Error occurred: {e}"

#This function will be defineda s write_file_list
def write_file_list(filename, lines):
 """This will write a list of strings to the file  as new lines."""
 try:
 #This will open the file in write mode to overwrite
  with open(filename, 'w') as file:
   for line in lines:
    file.write(line + '\n')
 except Exception as e:
  return f"Error occurred: {e}"

#This function will be defined as copy_file_add_line_numbers
def copy_file_add_line_numbers(filename, new_filename):
 """This will copy the content of data.txt file  to a new file with each line numbered"""
 try:
  #This will open the file in read mode and desstination file in write mode
  with open(filename, 'r') as read_file:
   with open(new_filename, 'w') as write_file:
    for index, line in enumerate(read_file, start=1):
     write_file.write(f"{index}:{line}")
 except FileNotFoundError:
  return "File cannot be found"

