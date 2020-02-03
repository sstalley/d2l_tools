"""
d2l_cat.py - concatenate specified files from each student into one big file
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

script_name = sys.argv[0]

if (len(sys.argv) < 3):
	print("usage: ", script_name, "<directory> <file extension(s)>")
	sys.exit()
	# example command for running this script:
	# python3 d2l_builder.py HW2 .c "cc -lpd -fdafd " "-o"

root_dir = sys.argv[1]
extensions = sys.argv[2:]

for ext in extensions:
	ext = ext.lower()

submissions = os.listdir(root_dir)

students = 0
f_count = 0
# for every student folder
for sfolder_name in submissions:

	sfolder = os.path.join(root_dir, sfolder_name)
	# print("sfolder:", sfolder)

	# skip files, we only care about folders
	if not os.path.isdir(sfolder):
		continue
	students = students + 1

	logpath = os.path.join(sfolder, "log.log")

	print("Writing \"", logpath, "\"...")
	log = open(logpath, "w")

	sfiles = os.listdir(sfolder)
	for sfile_name in sfiles:
		sfile = os.path.join(sfolder, sfile_name)

		fname, fext = os.path.splitext(sfile)

		# skip other types of files
		if not fext.lower() in extensions:
			continue

		f_count = f_count + 1

		print("Reading \"", sfile, "\"...")
		log.write("Contents of " + sfile + ":")

		rfile = open(sfile, "r", errors='ignore')
		log.write(rfile.read())
		rfile.close()

	log.close()

print("read", f_count, "files for", students, "students")

