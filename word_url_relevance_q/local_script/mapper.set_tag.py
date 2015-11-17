import sys

for line in sys.stdin:
	vals = line.strip().split("\t")
	if len(vals) > 12:
		tag = "1"
		bidword = vals[1]
		url = vals[11]
		ori_val = "\1".join(vals)
		print "%s\t%s\t%s\t%s" % (bidword, url, tag, ori_val)
	elif len(vals) == 3:
		tag = "2"
		bidword = vals[0]
		url = vals[1]
		rel_q = vals[2]
		try:
			q_val = float(rel_q)
		except e:
			print >> sys.stderr, "Error! relevance q: %s is invalid." % rel_q
			continue
		print "%s\t%s\t%s\t%s" % (bidword, url, tag, rel_q)
