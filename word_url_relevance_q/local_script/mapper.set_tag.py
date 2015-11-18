import sys
import url_util

for line in sys.stdin:
	vals = line.strip().split("\t")
	if len(vals) >= 4:
		tag = "2"
		query = url_util.regularize_str(vals[0])
		url = url_util.regularize_url(vals[11])
		ori_val = "\1".join(vals)
		print "%s\t%s\t%s\t%s" % (query, url, tag, ori_val)
	elif len(vals) == 3:
		tag = "1"
		string = vals[0]
		url = vals[1]
		rel_q = vals[2]
		try:
			q_val = float(rel_q)
		except e:
			print >> sys.stderr, "Error! relevance q: %s is invalid." % rel_q
			continue
		print "%s\t%s\t%s\t%s" % (string, url, tag, rel_q)
