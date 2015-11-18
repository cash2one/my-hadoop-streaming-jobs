# coding:gbk
import sys

cur_index = ""
cur_value = ""
cur_rig_q = ""
cur_click_q = ""

for line in sys.stdin:
	vals = line.strip().split("\t")
	index = vals[0]
	tag = vals[1]
	query = vals[2]
	url = vals[3]
	
	if tag == "2" and index == cur_index:
		cur_value = vals[4]
		output = cur_value.split("\1")
		qlq = output[10]
		mark1 = output[9]
		comment1 = output[4]
		if comment1 == "乱买词":
			mark2 = "0"
			mark3 = "0"
		else:
			mark2 = "1"
			if mark1 != "0":
				mark3 = "1"
			else:
				mark3 = "-1"
		print "\t".join([index, query, url, qlq, cur_rig_q, cur_click_q, mark1, mark2, mark3])
	if tag == "1":
		cur_index = index
		cur_rig_q = vals[4]
		cur_click_q = vals[5]
