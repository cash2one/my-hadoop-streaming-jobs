#!/usr/bin/env python
import sys

def calculate_ele(dz, di, flag):
	click_q = (di[flag][3] - dz[flag][3])/di[flag][3]
	bad_click_rate = (di[flag][4] - dz[flag][4])/di[flag][4]
	return (click_q, bad_click_rate)

if __name__ == "__main__":
	
	c_d = {
		"d0_clkqs_pc": {"baidu": [], "other": [], "integrity": []},
		"d1_clkqs_pc": {"baidu": [], "other": [], "integrity": []},
		"dz_clkqs_ps": {"baidu": [], "other": [], "integrity": []},
		"other_pc": {"baidu": [], "other": [], "integrity": []}
	}
	
	# Read click info into a dict
	for line in sys.stdin:
		tag, flag, sum_good_click, sum_bad_click, sum_total_click, click_q = line.strip().split("\t")
		bad_click_rate = float(sum_bad_click) / float(sum_total_click)
		c_d[tag][flag] = [float(sum_good_click), float(sum_bad_click), float(sum_total_click), float(click_q), float(bad_click_rate)]
		
	# Calculate integrity
	for key, value in c_d.iteritems():
		value["integrity"].append(value["baidu"][0] + value["other"][0])
		value["integrity"].append(value["baidu"][1] + value["other"][1])
		value["integrity"].append(value["baidu"][2] + value["other"][2])
		value["integrity"].append((value["integrity"][0] + value["integrity"][2] - value["integrity"][1])/(2*value["integrity"][2]))
		value["integrity"].append(value["integrity"][1]/value["integrity"][2])
		
	# Calculate matrix
	# - For autonomy:
	autonomy_matrix = [
		# --- d0 and dz : click_q , bad_click_rate
		calculate_ele(c_d["dz_clkqs_ps"], c_d["d0_clkqs_pc"], "baidu"),
		# --- d1 and dz : click_q , bad_click_rate
		calculate_ele(c_d["dz_clkqs_ps"], c_d["d1_clkqs_pc"], "baidu")
	]
	print autonomy_matrix
	# - For integrity:
	integrity_matrix = [
		# --- d0 and dz : click_q , bad_click_rate
		calculate_ele(c_d["dz_clkqs_ps"], c_d["d0_clkqs_pc"], "integrity"),
		# --- d1 and dz : click_q , bad_click_rate
		calculate_ele(c_d["dz_clkqs_ps"], c_d["d1_clkqs_pc"], "integrity")
	]
	print integrity_matrix
	
	
	
		 
	
	
