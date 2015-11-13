import sys

relevance_q  = ""
cur_bidword  = ""
cur_url      = ""

for line in sys.stdin:
	val = line.strip().split("\t")
	bidword = val[0]
	url     = val[1]
	tag     = val[2]
	value   = val[3]
	
	if tag == "1":
		relevance_q = value
		cur_bidword = bidword
		cur_url     = url
	
	elif tag == "2" and cur_bidword == bidword and cur_url == url:
		print "%s\t%s\t%s\t%s" % (value, bidword, url, relevance_q)
		
	elif tag == "2" and ( cur_bidword != bidword or cur_url != url ):
		print "%s\t%s\t%s\t%s" % (value, bidword, url, "\N")
		
	
		