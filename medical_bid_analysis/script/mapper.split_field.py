import sys

experimental_group = sys.argv[1]
control_group = sys.argv[2]

for line in sys.stdin:
    field, bidword, sum_bid, average_bid, sum_sqrt_bid, std_deviation, sum_click, count, month = line.strip().split("\t")
    tag = ""
    if month == experimental_group:
        tag = "1"
    elif month == control_group: 
        tag = "2"
    else:
        print >> sys.stderr, "Tag %s is invalid, which line is %s" % (tag, line)
        exit(1)
    print "\t".join((field, bidword, tag, sum_bid, average_bid, sum_sqrt_bid, std_deviation, sum_click, count, month))
