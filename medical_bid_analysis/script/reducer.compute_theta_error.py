import sys

last_field = ""

exp_theta_bid = con_theta_bid = 0
exp_std_deviation = con_std_deviation = 0
exp_count = con_count = 0
sum_theta_bid = 0
sum_w = 0
exp_sum_bid = con_sum_bid = 0
exp_average_bid = con_average_bid = 0
exp_sum_count = con_sum_count = 0

for line in sys.stdin:
    field, bidword, tag, sum_bid, average_bid, sum_sqrt_bid, std_deviation, sum_click, count, month = line.strip().split("\t")
    
    if field != last_field:
        if last_field != "":
            average_theta_bid = sum_theta_bid / sum_w
            exp_average_bid = exp_sum_bid / exp_sum_count
            con_average_bid = con_sum_bid / con_sum_count
            print "\t".join((str(last_field), str(exp_average_bid), str(con_average_bid), str(average_theta_bid)))
            average_theta_bid = 0
            sum_theta_bid = 0
            sum_w = 0
            exp_average_bid = exp_sum_count = exp_sum_bid = 0
            con_average_bid = con_sum_count = con_sum_bid = 0

        last_field = field
    
    if tag == "1":
        exp_theta_bid = float(average_bid)
        exp_std_deviation = float(std_deviation)
        exp_count = float(count)
        # Compute Average bid
        exp_sum_count += float(count)
        exp_sum_bid += float(average_bid) * float(count)
    elif tag == "2":
        if exp_theta_bid == 0 or exp_count == 0:
            print >> sys.stderr, "invalid exp value, theta = %s, std = %s, count = %s" % (exp_theta_bid, exp_std_deviation, exp_count)
            #exit(1)
            continue
        con_theta_bid = float(average_bid)
        con_std_deviation = float(std_deviation)
        con_count = float(count)
        # Compute theta
        theta_bid = exp_theta_bid - con_theta_bid
        std_error = 1.0 / exp_count + 1.0 / con_count
        w = 1.0 / std_error
        sum_theta_bid += w * theta_bid
        sum_w += w  
        # Compute Average bid
        con_sum_count += float(count)
        con_sum_bid += float(average_bid) * float(count)
        # Clear
        exp_count = exp_theta_bid = exp_std_deviation = 0
        con_count = con_theta_bid = con_std_deviation = 0

if last_field != "":
    average_theta_bid = sum_theta_bid / sum_w
    exp_average_bid = exp_sum_bid / exp_sum_count
    con_average_bid = con_sum_bid / con_sum_count
    print "\t".join((str(last_field), str(exp_average_bid), str(con_average_bid), str(average_theta_bid)))
    average_theta_bid = 0
    sum_theta_bid = 0
    sum_w = 0
    exp_average_bid = exp_sum_count = exp_sum_bid = 0
    con_average_bid = con_sum_count = con_sum_bid = 0
