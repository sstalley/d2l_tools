"""
!!! TODO SOS: Add name and description of this file
Copyright (C) 2020 Sean O. Stalley

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import sys
import os
import zipfile

script_name = sys.argv[0]

if (len(sys.argv) != 3):
	print("usage: ", script_name, " <Zip file from d2l> <name of folder to create>")
	sys.exit()

zfile = sys.argv[1]
destination = sys.argv[2]

print("Running ", script_name, " ...")

if not (os.path.exists(destination)):
	# Make a folder to put all the unzipped stuff
	try:
		os.mkdir(destination)
	#except FileExistsError:
	#	print(destination, " already exists, continuing...")
	except OSError:
		print("Error: Cannot create ", destination)
		sys.exit()

# Unzip file from d2l
with zipfile.ZipFile(zfile, 'r') as zip_ref:
	zip_ref.extractall(destination)


#For every zip file:
	#Unzip it

	#Place all files in root directory

# For every student that submitted files individually:
	#Create a folder for them
	#Place individual files into folder
