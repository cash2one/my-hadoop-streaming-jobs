import sys

cur_bidword = ""
cur_url = ""
cur_value = ""

for line in sys.stdin:
	vals = line.strip().split("\t")
	bidword = vals[0]
	url = vals[1]
	tag = vals[2]
	
	if tag == "2" and bidword == cur_bidword and url == cur_url:
		ori_val = cur_value.split("\1")
		cur_value = vals[3]
		query = ori_val[0]
		index = ori_val[12]
		mark1 = ori_val[8]
		mark2 = ori_val[10]
		mark = ori_val[4]
		comment1 = ori_val[13]
		comment2 = ori_val[14]
		comment = ori_val[15]
		print "%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s" % (bidword, url, query, index, comment1, comment2, comment, mark1, mark2, mark, rel_q)
	if tag == "1":
		cur_bidword = bidword
		cur_url = url
		rel_q = vals[3]
		
