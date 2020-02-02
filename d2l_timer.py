"""
d2l_timer.py - run a program multiple times with multiple parameters and compare the speed
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
import subprocess
import time

script_name = sys.argv[0]

if (len(sys.argv) != 4):
	print("usage: ", script_name, "<executable> <file containing arguments> <runs per argument>")
	sys.exit()

program = sys.argv[1]
argfile = sys.argv[2]
repeats = int(sys.argv[3])


with open(argfile) as f:
	args = f.readlines()

runtimes = list()
# Run the program and time everything
for arg in args:
	runtime = 0.0

	print("running ", program, arg, "...")

	cmd = list()
	cmd.append(program)
	cmd.extend(arg.split())
	for run in range(repeats):
		start_time = time.time()
		subprocess.run(cmd)
		end_time = time.time()
		runtime = runtime + (end_time - start_time)

	runtimes.append(runtime/repeats)

# Write a timing log
log = open(program + ".tlog", "w+")

for i, arg in enumerate(args):
	# The output format is a tab seperated table of : <arguments> <Average runtime> <Speedup compared to first row>
	log.write(arg.strip() + "\t" + str(runtimes[i]) + "\t" + str(runtimes[0]/runtimes[i]) + "\n")

log.close()
