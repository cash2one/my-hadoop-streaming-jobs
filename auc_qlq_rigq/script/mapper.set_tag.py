import sys
import url_util
import urllib

for line in sys.stdin:
	vals = line.strip().split("\t")
	if len(vals) <= 11:
		tag = "2"
		index = vals[3]
		url = vals[1]
		query = vals[2]
		ori_val = "\1".join(vals)
		print "%s\t%s\t%s\t%s\t%s" % (index, tag, query, url, ori_val)
	elif len(vals) > 140:
		tag = "1"
		index = vals[0]
		query = url_util.regularize_str(vals[4])
		url = urllib.unquote(vals[93])
		if not url_util.is_valid_url(url):
			continue
		url = url_util.regularize_url(url)
		rig_q = vals[140].split("#")[0]
		click_q = vals[150].split("%")[3]
		try:
			rig_q_val = float(rig_q)
			click_q_val = float(click_q)
		except:
			print >> sys.stderr, "Error! rig q: %s or click q: %s is invalid." % (rig_q, click_q)
			continue
		print "\t".join([index, tag, query, url, rig_q, click_q])
