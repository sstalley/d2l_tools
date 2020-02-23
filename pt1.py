import subprocess
import re

threads = range(1,17)
runs = 3

runtimes = list()
fname = "./_grading_output.txt"

for thread in threads:
	total = 0.0
	print(thread, " threads")
	for run in range(runs):
		print("run ", run)
		
		p = subprocess.check_output(["mpirun", "--oversubscribe", "-H", "localhost", "-np", str(thread), "./temp"])
		time = re.findall("\d*\.\d*", p)

		print("thread ", thread, ", run ", run, ", time: ", time[-1])
		total += float(time[-1])
	average = total / runs
	runtimes.append(average)

f = open(fname, "w+")

for i, thread in enumerate(threads):
	f.write(str(thread) + "\t" + str(runtimes[i]) + "\t" + str(runtimes[0]/runtimes[i]) + "\n")

f.close()
