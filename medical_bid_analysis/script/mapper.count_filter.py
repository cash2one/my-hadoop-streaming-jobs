import sys

threshold = sys.argv[1]
experimental_group = sys.argv[2]
control_group = sys.argv[3]

for line in sys.stdin:
    bidword, field, sum_bid, average_bid, sum_sqrt_bid, std_deviation, sum_click, count, month = line.strip().split("\t")
    tag = ""
    if month == experimental_group:
        tag = "1"
    elif month == control_group:
        tag = "2"
    else:
        print >> sys.stderr, "mapper_tag: month - %s, experimental_group - %s, control_group - %s" % (month, experimental_group, control_group)
        exit(1)
    if float(count) >= float(threshold):
        print "\t".join((bidword, tag, field, sum_bid, average_bid, sum_sqrt_bid, std_deviation, sum_click, count, month))
