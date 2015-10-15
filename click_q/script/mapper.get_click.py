#!/usr/bin/env python
import sys
import utils

if __name__ == "__main__":
	# Validation of the number of parameters
	if len(sys.argv) != 2:
		raise
	# Read dictionary file path from first command parameter
	dict_file_path = sys.argv[1]
	# Load word dictionary into 'my_dict'
	my_dict = utils.load_dict(dict_file_path)
	# Map
	for line in sys.stdin:
		asp, ubs, aries = ("", "", "")
		# Extract useful infomation.
		try:
			asp, ubs, aries = line.strip().split("   ")
		except:
			continue
		# - which tag does the tuple belong to 
		tag = ""
		OVLEXP_ID_LIST  = aries[95].split("#")
		if "207L-1011" in OVLEXP_ID_LIST:
			tag = "d0_clkqs_pc"
		elif "207L-1010" in OVLEXP_ID_LIST:
			tag = "d1_clkqs_pc"
		elif "207L-dz" in OVLEXP_ID_LIST:
			tag = "dz_clkqs_ps"
		else:
			tag = "other_pc"
		# - Whether cn is baidu or other
		cn = aries[5]
		is_baidu_other = ""
		if cn in my_dict:
			if my_dict[cn] == "organic" or my_dict[cn] == "union2baidu":
				is_baidu_other = "baidu"
			else:
				is_baidu_other = "other"
		else:
			is_baidu_other = "null"
		# - info of click
		ubs_val     = ubs.split("\t")
		good_click  = int(ubs_val[5])
		bad_click   = int(ubs_val[6])
		total_click = good_click + bad_click
		# Output result to stdin    
		click_info = (tag, is_baidu_other, good_click, bad_click, total_click)
		if is_baidu_other != "null":
			print "%s\t%s\t%s\t%s\t%s" % click_info