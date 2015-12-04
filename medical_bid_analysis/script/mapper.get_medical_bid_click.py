import sys
import Filter
import urllib
import url_util

shitu_type = sys.argv[1]

def extract_domain(url):
    url = urllib.unquote(urllib.unquote(urllib.unquote(url)))
    if "http" not in url:
        print >> sys.stderr, "Error 4, http is not in url, invalid url: %s" % url
        return "-1"
    url = url.split("http")[-1]
    if url.startswith("://"):
        url = url.strip("://")
    elif url.startswith("s://"):
        url = url.strip("s://")
    else:
        print >> sys.stderr, "Error 2, error http head, invalid url : %s" % url
        return "-1"
    url = "http://" + url
    if url_util.is_valid_url(url):
        url = url_util.regularize_url(url)
        domain = Filter.domain_url(url)
        if domain == "NULL":
            print >> sys.stderr, "Error 3, domain is null, invalid url : %s" % url
            return "-1"
        return domain
    else:
        print >> sys.stderr, "Error 1, invalid url: %s" % url
        return "-1"
        

for line in sys.stdin:
    line = line.strip()
    if line == "":
        continue
    blocks = line.split("   ")
    if len(blocks) < 2:
        print >> sys.stderr, "shitu log is invalid, Error: len of vals is %s" % len(vals)
        continue
    vals = blocks[2].split("\t")
    if len(vals) < 23:
        print >> sys.stderr, "shitu log is invalid, Error: len of vals is %s" % len(vals)
        continue
    bidword = url_util.regularize_str(urllib.unquote(vals[23]))
    click = vals[1]
    if shitu_type == "wise":
        if len(vals) < 142:
            print >> sys.stderr, "shitu wise log is invalid, Error: len of vals is %s" % len(vals)
            continue
        target_url = vals[92]
        query_trade = vals[123]
        original_bid = vals[141]
    elif shitu_type == "pc":
        if len(vals) < 153:
            print >> sys.stderr, "shitu pc log is invalid, Error: len of vals is %s" % len(vals)
            continue
        target_url = vals[73]
        query_trade = vals[137]
        original_bid = vals[153]    

    try:
        int_click = int(click)
        int_query_trade = int(query_trade)
        int_original_bid = int(original_bid)
        if int_original_bid > 1000000:
            continue
    except Exception as e:
        print >> sys.stderr, "There is an error occured. [click] %s, [query_trade] %s, [original_bid] %s. Error: %s" % (click, query_trade, original_bid, e)
        continue

    domain = extract_domain(target_url)
    if domain == "-1":
        continue
    # Field = 1: Medical
    # Field = 0: Not Medical
    field = str(int(int(query_trade)/10000 == 82))
    print "\t".join((bidword, field, click, original_bid))
