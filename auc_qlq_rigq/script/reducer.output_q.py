import sys

q_tag = sys.argv[1]
max_label = 1

for line in sys.stdin:
	(tag, q, mark1, mark2, mark3) = line.strip().split("\t")
	if tag == q_tag and mark3 != "-1":
		print "%s\t%s\t%s" % (q, max_label, mark3)