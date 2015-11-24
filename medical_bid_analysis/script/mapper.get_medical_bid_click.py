import sys
import Filter
import urllib

shitu_type = sys.argv[1]

for line in sys.stdin:
    line = line.strip()
    if line == "":
        continue
    blocks = line.split("   ")
    if len(blocks) < 2:
        continue
    vals = blocks[2].split("\t")
    if len(vals) < 23:
        continue
    bidword = vals[23]
    click = vals[1]
    if shitu_type == "wise":
        if len(vals) < 142:
            continue
        target_url = vals[92]
        query_trade = vals[123]
        original_bid = vals[141]
    elif shitu_type == "pc":
        if len(vals) < 153:
            continue
        target_url = vals[73]
        query_trade = vals[137]
        original_bid = vals[153]    

    domain = Filter.domain_url(urllib.unquote(target_url).split("http://")[-1])
    # Field = 1: Medical
    # Field = 0: Not Medical
    field = str(int(int(query_trade)/10000 == 82))
    print "\t".join((bidword, domain, field, click, original_bid))
