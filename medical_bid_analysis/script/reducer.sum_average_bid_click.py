import sys

last_bidword = ""
last_domain = ""
last_field = ""

sum_click = sum_bid = count = 0

for line in sys.stdin:
    (bidword, domain, field, click, original_bid) = line.strip().split("\t")
    
    if bidword == last_bidword and domain == last_domain and field == last_field:
        sum_click += int(click)
        sum_bid += int(original_bid)
        count += 1.0
    elif (bidword != last_bidword or domain != last_domain or field != last_field) and (last_bidword != "" and last_domain != "" and last_field != ""):
        average_bid = float(sum_bid) / count
        print "\t".join((last_bidword, last_domain, last_field, str(sum_bid), str(average_bid), str(sum_click), str(count)))
        sum_click = int(click)
        sum_bid = int(original_bid)
        count = 1
    elif last_bidword == "" or last_domain == "" or last_field == "":
        sum_click = int(click)
        sum_bid = int(original_bid)
        count = 1
    
    last_bidword = bidword
    last_domain = domain
    last_field = field
    
average_bid = float(sum_bid) / count
print "\t".join((last_bidword, last_domain, last_field, str(sum_bid), str(average_bid), str(sum_click), str(count)))


