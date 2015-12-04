import sys

last_bidword = ""
cur_line = ""
check_flag = False

for line in sys.stdin:
    bidword, tag, field, sum_bid, average_bid, sum_sqrt_bid, std_deviation, sum_click, count, month = line.strip().split("\t")
    if bidword == last_bidword:
        if tag == "2" and check_flag == True:
            _bidword, _tag, _field, _sum_bid, _average_bid, _sum_sqrt_bid, _std_deviation, _sum_click, _count, _month = cur_line.strip().split("\t")
            if _field == field:
                print "\t".join((_field, _bidword, _sum_bid, _average_bid, _sum_sqrt_bid, _std_deviation, _sum_click, _count, _month))
                print "\t".join((field, bidword, sum_bid, average_bid, sum_sqrt_bid, std_deviation, sum_click, count, month))
            check_flag = False
    elif bidword != last_bidword:
        if tag == "1":
            cur_line = line
            check_flag = True
        elif tag == "2":
            check_flag = False
        else:
            print >> sys.stderr, "Tag %s is invalid, which line is %s" % (tag, line.strip().split("\t"))
            exit(1)

    last_bidword = bidword

