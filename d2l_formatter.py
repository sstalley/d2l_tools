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
import re

script_name = sys.argv[0]

if (len(sys.argv) != 3):
	print("usage: ", script_name, " <Zip file from d2l> <name of folder to create>")
	sys.exit()

zfile = sys.argv[1]
destination = sys.argv[2]

print("Running ", script_name, " ...")

# Make a folder to store all the submissions
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


submissions = os.listdir(destination)

students = 0
# Make a folder for every student
for sfile in submissions:

	# every submitted file is in the format "<some ID number> <student name> <filename>.<extention>"
	# we create a folder for each student in the format "<some ID number> <student name>" and put all their files into it
	smatch =  re.match("^(\d+\-\d+)(.+?)(?=\s\S+$)", sfile)
	if (smatch is None):
		continue
	else:
		sname = smatch[0]

	spath = os.path.join(destination, sname)

	if not (os.path.exists(spath)):
		students = students + 1
		print("creating ", spath, "...")
		try:
			os.mkdir(spath)
		except OSError:
			print("Error: Cannot create", spath)
			sys.exit()

	# move file into folder
	newfile = str.lstrip(str.replace(sfile, sname, ""))
	oldpath = os.path.join(destination, sfile)
	newpath = os.path.join(spath, newfile)
	print("Moving", oldpath, "to", newpath)
	os.rename(oldpath, newpath)
	
print("created folders for", students, "students")

# For every submission:
	# Create a folder

# For every zip file:
	#Unzip it

	#Place all files in root directory

# For every student that submitted files individually:
	#Create a folder for them
	#Place individual files into folder
