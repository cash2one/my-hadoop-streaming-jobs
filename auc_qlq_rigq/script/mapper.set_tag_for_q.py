import sys

for line in sys.stdin:
	(index, query, url, qlq, rigq, clickq, mark1, mark2, mark3) = line.strip().split("\t")
	print "\t".join(["rigq", rigq, mark1, mark2, mark3])
	print "\t".join(["qlq", qlq, mark1, mark2, mark3])
	print "\t".join(["clickq", clickq, mark1, mark2, mark3])