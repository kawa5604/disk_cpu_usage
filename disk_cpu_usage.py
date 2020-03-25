#!/usr/bin/env python3

import shutil	
import psutil


#simple test for disk usage 
def check_disk_usage(disk):
	disk_usage = shutil.disk_usage(disk)
	free = disk_usage.free / disk_usage.total *100
	print("Current free disk space is {:.2f}%".format(free))
	return free > 10

#simple test for cpu usage
def check_cpu_usage():
	cpu = psutil.cpu_percent(1)
	print("Current CPU usage is at {:.2f}%".format(cpu))
	return cpu < 60


if not check_disk_usage("/") or not check_cpu_usage():
	print("ERROR")

else:
	print("Everything is ok")

