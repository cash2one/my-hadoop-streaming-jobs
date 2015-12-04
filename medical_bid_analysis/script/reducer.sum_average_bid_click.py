import sys

month = sys.argv[1]

last_bidword = ""
last_field = ""

sum_sqrt_bid = sum_click = sum_bid = count = 0

for line in sys.stdin:
    (bidword, field, click, original_bid) = line.strip().split("\t")
    
    if bidword == last_bidword and field == last_field:
        sum_click += int(click)
        sum_bid += int(original_bid)
        sum_sqrt_bid += pow(float(original_bid), 2)
        count += 1.0
    else:  
        if last_bidword != "" and last_field != "":
            if count == 0:
                print >> sys.stderr, "invalid count = 0, line: %s" % line
                exit(1)
            average_bid = float(sum_bid) / count
            std_deviation = (sum_sqrt_bid - count * pow(average_bid, 2)) / count
            print "\t".join((last_bidword, last_field, str(sum_bid), str(average_bid), str(sum_sqrt_bid), str(std_deviation), str(sum_click), str(count), month))
        sum_click = int(click)
        sum_bid = float(original_bid)
        sum_sqrt_bid = pow(float(original_bid), 2)
        count = 1
        
        last_bidword = bidword
        last_field = field

if last_bidword != "" and last_field != "":
    if count == 0:
        print >> sys.stderr, "invalid count = 0, line: %s" % line
        exit(1)
    average_bid = float(sum_bid) / count
    std_deviation = (sum_sqrt_bid - count * pow(average_bid, 2)) / count
    print "\t".join((last_bidword, last_field, str(sum_bid), str(average_bid), str(sum_sqrt_bid), str(std_deviation), str(sum_click), str(count), month))

