# file_md5_binary
file_md5_binary is Python script for calculating binary MD5 64 of a file.
This python script can function either Linux, or Windows OS.

# Requirements
This script requires the pyperclip module for copying base64 of MD5 to clipboard

# Installation
To use this script, you need to clone the file_md5_binary from it's repository:
```
git clone https://github.com/DarkoMilosevic86/file_md5_binary
```
After cloning of the repository, you need to install the pyperclip module using the following command:
```
pip install pyperclip
```
This module is necesary to copy base64 of MD5 to the clipboard

# Usage
To use the file_md5_binary python script, you need to call the script by passing a file name as argument, eg:
```
file_md5_binary.py test.txt
```
Also, you can specify a full file path, eg:
```
file_md5_binary.py /home/test.txt
```
