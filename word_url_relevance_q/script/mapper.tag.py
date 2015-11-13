import sys

for line in sys.stdin:
    val = line.strip().split("\t")
	bidword = val[0]
	url     = val[1]
	q_or_source = val[2]
	
	if q_or_source == "word_url_winfoid":
		print "%s\t%s\t2\t%s" % (bidword, url, val[3])
	else:
		print "%s\t%s\t1\t%s" % (bidword, url, q_or_source)