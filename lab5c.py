#!/usr/bin/env python3
#This function will be dfeined as add
def add(x, y): 
 """This will add two arugments after converting to intergers and will return sum"""
 try:
 #This will convert the interger x and y to return sum value
  return int(x) + int(y)
 except ValueError:
  return "error: could not add numbers"

def read_file(filename):
 """This will read the data.txt file and return list of lines"""
 try:
 #This will open file in read mode and return the lines as a list
  with open(filename, 'r') as file:
   return file.readlines()
 except FileNotFoundError:
  return "error: could not read file"
