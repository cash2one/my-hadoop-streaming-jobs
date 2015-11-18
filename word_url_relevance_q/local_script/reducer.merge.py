import sys

cur_query = ""
cur_url = ""
cur_value = ""
cur_rel_q = ""

for line in sys.stdin:
	vals = line.strip().split("\t")
	query = vals[0]
	url = vals[1]
	tag = vals[2]
	
	if tag == "2" and query == cur_query and url == cur_url:
		cur_value = vals[3]
		ori_val = cur_value.split("\1")
		bidword = ori_val[1]
		index = ori_val[12]
		mark1 = ori_val[8]
		mark2 = ori_val[10]
		mark = ori_val[4]
		comment1 = ori_val[13]
		comment2 = ori_val[14]
		comment = ori_val[15]
		print "\t".join([bidword, url, query, index, comment1, comment2, comment, mark1, mark2, mark, cur_rel_q])
	if tag == "1":
		cur_query = query
		cur_url = url
		cur_rel_q = vals[3]
		
