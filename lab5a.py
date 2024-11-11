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

#This section is for me to test if it works.
#if __name__ == "__main__":
 #filename = 'data.txt'

 #Testing mmy function read_file_string
# print("Reading file to convert o single string")
# print(read_file_string(filename))

 #Testing my function read_file_list
 #print("\nReading file line by line  into a list:")
# print(read_file_list(filename))

