"""
d2l_builder.py - compiles all the specified files in the directory created by d2l_formatter.py
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

if (len(sys.argv) != 5):
	print("usage: ", script_name, "<directory> <filetype> <compiler string> <output string>")
	sys.exit()
	# example command for running this script:
	# python3 d2l_builder.py HW2 .c "cc -lpd -fdafd " "-o"


root_dir = sys.argv[1]
ftype = sys.argv[2]
ccstring = sys.argv[3]
outstring = sys.argv[4]


submissions = os.listdir(root_dir)

students = 0
cc_count = 0
# for every student folder
for sfolder_name in submissions:

	sfolder = os.path.join(root_dir, sfolder_name)
	print("sfolder:", sfolder)

	# skip files, we only care about folders
	if not os.path.isdir(sfolder):
		continue
	students = students + 1

	sfiles = os.listdir(sfolder)
	for sfile_name in sfiles:
		sfile = os.path.join(sfolder, sfile_name)

		fname, fext = os.path.splitext(sfile)

		# skip other types of files
		if not ftype.lower() == fext.lower():
			continue
		cc_count = cc_count + 1

		cmd_str = ccstring + " \"" + sfile + "\" " + outstring + " \"" + fname + "\""

		print("Running \"", cmd_str, "\"...")
		stream = os.popen(cmd_str)
		cc_output = stream.read()
		
		logpath = fname + ".clog"
		cc_log = open(logpath, "w")
		cc_log.write(cc_output)
		cc_log.close()

print("compiled", cc_count, ftype, "files for", students, "students")
