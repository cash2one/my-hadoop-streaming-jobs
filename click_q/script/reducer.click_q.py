#!/usr/bin/env python
import sys

if __name__ == "__main__":
    sum_good_click  = 0
    sum_bad_click   = 0
    sum_total_click = 0
    
    last_tag  = ""
    last_flag = ""
    for line in sys.stdin:
        tag, flag, good_click, bad_click, total_click = line.strip().split("\t")
        
        if (tag == last_tag and flag == last_flag) or (last_flag == "" and last_tag == ""):
            sum_good_click  += float(good_click)
            sum_bad_click   += float(bad_click)
            sum_total_click += float(total_click)
            
        elif tag != last_tag or flag != last_flag:
            # Calculate ClickQ
            if sum_total_click == 0:
                click_q = -1
            else:
                click_q = (sum_good_click - sum_bad_click + sum_total_click) / (2 * sum_total_click)
            print "%s\t%s\t%s\t%s\t%s\t%s" % \
                (last_tag, last_flag, sum_good_click, sum_bad_click, sum_total_click, click_q)
            # Clear buffer    
            sum_good_click  = float(good_click)
            sum_bad_click   = float(bad_click)
            sum_total_click = float(total_click)
            
        last_tag  = tag
        last_flag = flag
        
    # Calculate ClickQ
    if sum_total_click == 0:
        click_q = -1
    else:
        click_q = (sum_good_click - sum_bad_click + sum_total_click) / (2 * sum_total_click)
    print "%s\t%s\t%s\t%s\t%s\t%s" % \
        (last_tag, last_flag, sum_good_click, sum_bad_click, sum_total_click, click_q)
