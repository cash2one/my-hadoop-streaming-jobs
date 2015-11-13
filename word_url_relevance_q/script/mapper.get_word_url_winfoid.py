import sys
import url_util

SOURCE = "word_url_winfoid"

for line in sys.stdin:
    val = line.strip().split("\t")
	level    = val[0]
	winfoid  = val[1]
	bidword  = url_util.regularize_url(val[6])
	pc_url   = url_util.regularize_url(val[13])
	wise_url = url_util.regularize_url(val[15])
	
	if level == "4":
		if pc_url != "DFT":
			print "%s\t%s\t%s\t%s" % (bidword, pc_url, SOURCE, winfoid)
		if wise_url != "DFT":
			print "%s\t%s\t%s\t%s" % (bidword, wise_url, SOURCE, winfoid)