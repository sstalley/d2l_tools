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
import threading

script_name = sys.argv[0]

if (len(sys.argv) > 5):
	print("usage: ", script_name, "<directory> <file containing arguments> <runs per argument> <optional command prefix>")
	sys.exit()

root_dir = sys.argv[1]
argfile  = sys.argv[2]
repeats  = int(sys.argv[3])

if (len(sys.argv) > 4):
	prefix = int(sys.argv[4])
else:
	prefix = None

with open(argfile) as f:
	args = f.readlines()

submissions = os.listdir(root_dir)

students = 0
time_count = 0
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
		if not fext.lower() == ".out":
			continue

		runtimes = list()
		errlog = list()
		outlog = list()
		# Run the program and time everything
		for arg in args:
			runtime = 0.0
		
			print("running ", sfile, arg, "...")
		
			# Note this is kind of hacky - if there is a prefix we put the arguments from the file after the prefix instead of after the command itself
			# Probably would be considered a bug for most use cases, but it solves my one niche usecase cleanly :)
			cmd = list()
			if prefix is not None:
				cmd.append(prefix)
				cmd.extend(arg.split())

			cmd.append(sfile)
			if prefix is None:
				cmd.extend(arg.split())

			for run in range(repeats):
				start_time = time.time()

				proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
				timeout = threading.Timer(120, proc.kill)
				try:
					#result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, start_new_session=True, timeout=120)
					timeout.start()
					stdout, stderr = proc.communicate()
				except:
					print("something bad happened...")
				else:
					outlog.append(stdout)
					errlog.append(stderr)
					#outlog.append(result.stdout)
					#errlog.append(result.stderr)
				finally:
					timeout.cancel()

				end_time = time.time()
				runtime = runtime + (end_time - start_time)
				
		
			runtimes.append(runtime/repeats)
		
		# Write a timing log
		log = open(fname + ".tlog", "w+")

		
		for i, arg in enumerate(args):
			# The output format is a tab seperated table of : <arguments> <Average runtime> <Speedup compared to first row>
			log.write(arg.strip() + "\t" + str(runtimes[i]) + "\t" + str(runtimes[0]/runtimes[i]) + "\n")
		
		log.close()
	
		# Write the output and error logs
		log = open(fname + ".errlog", "wb+")
		for err in errlog:
			log.write(err)
		log.close()
		log = open(fname + ".outlog", "wb+")
		for out in outlog:
			log.write(out)
		log.close()

		time_count = time_count + 1

print("wrote", time_count, "timing logs for", students, "students")
