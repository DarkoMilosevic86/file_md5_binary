#!/usr/bin/python3
# Copyright (C) 2023  Darko Milosevic

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


# Library imports
import sys
import hashlib
import base64
import pyperclip
# To use pyperclip module for copying text to the clipboard, you need to install the pyperclip module using the following command
# pip install pyperclip

# Function definition for opening a file, and calculating md5 hash
def calculate_md5(input_file):
    # Opening file and reading
    with open(input_file, 'rb') as f:
        # Reading content of file
        data = f.read()
        # Reading hash from a file
        md5hash = hashlib.md5(data).hexdigest()
    # Returning md5
    return md5hash

# Calling the function, but checking the arguments
if len(sys.argv)!=2:
    # Prints necesary arguments and exits the program
    print(sys.argv[0] + ' file_name')
    sys.exit(0)
# In other case
file_name = sys.argv[1]
# Now calling methods
md5_hex = calculate_md5(file_name)
# Converting the md5_hex to base64
base64_result = base64.b64encode(bytes.fromhex(md5_hex)).decode()
# Copying binary md5 to the clipboard
pyperclip.copy(base64_result)
# Printing the binary md5 to stack
print(base64_result)
