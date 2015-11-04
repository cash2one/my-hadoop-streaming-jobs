import sys

sum_shows = 0
sum_clks = 0
sum_price = 0
sum_bids = 0
ctr3_molecule = 0

cuid_tag = ""
cmatchid_tag = ""
last_cmatchid_tag = "\N"
last_cuid_tag = "\N"


def emit_statistics(cuid_tag, cmatchid_tag, sum_shows, sum_clks, sum_price, sum_bids, ctr3_molecule):
    shows = sum_shows  # Sum of counts of show up
    clks = sum_clks  # Sum of counts of clicks
    prices = sum_price
    # acp   = sum_price / sum_clks,  # ACP : average of prices
    # acb   = sum_bids / sum_clks,  # ACB : average of bids
    ctr2 = sum_clks / sum_shows  # CTR2: (sum of valid clicks / sum of shows up)
    # ctr3  = ctr3_molecule / sum_shows, # CTR3: (sum of valid clicks / counts of search id which has advertisement)
    # cpm2   = sum_price * 1000 / sum_shows  # CPM2: (CTR2*ACP*1000)
    # cpm3  = (ctr3  / sum_shows) * (sum_price / sum_clks) * 1000
    cuid_flag = ""
    if cuid_tag == "0":
        cuid_flag = "none_cuid"
    elif cuid_tag == "1":
        cuid_flag = "cuid"
    else:
        print >> sys.stderr, "WARNING, cuid tag %s was illegal. 0 or 1 was expeceted." % (cuid_tag)

    cmatchid_flag = ""
    if cmatchid_tag == "0":
        cmatchid_flag = "total_cmatch"
    elif cmatchid_tag == "1":
        cmatchid_flag = "222-223_cmatch"
    else:
        print >> sys.stderr, "WARNING, cmatchid tag %s was illegal. 0 or 1 was expeceted." % (cmatchid_tag)

    print "%s\t%s\t%s\t%s\t%s\t%s" % (cuid_flag, cmatchid_flag, clks, shows, prices, ctr2)


for line in sys.stdin:
    (cuid_tag, cmatchid_tag, value) = line.strip().split("\t")
    parse_val = value.split("\1")
    # parse the value
    show = float(parse_val[0])
    clk = float(parse_val[1])
    price = float(parse_val[2])
    bid = float(parse_val[3])
    dis = float(parse_val[4])

    if cuid_tag == last_cuid_tag and cmatchid_tag == last_cmatchid_tag:
        # shows
        sum_shows += show
        # clks
        sum_clks += clk
        # price
        sum_price += price
        # bids
        sum_bids += bid * clk
        # ctr3's molecule
        ctr3_molecule += clk * dis
    elif cuid_tag != last_cuid_tag or cmatchid_tag != last_cmatchid_tag:
        if last_cuid_tag != "\N" or last_cmatchid_tag != "\N":
            # Basic statistics
            emit_statistics(cuid_tag, cmatchid_tag, sum_shows, sum_clks, sum_price, sum_bids, ctr3_molecule)
        # Clear the buffer
        sum_shows = show
        sum_clks = clk
        sum_price = price
        sum_bids = bid * clk
        ctr3_molecule = clk * dis

    last_cmatchid_tag = cmatchid_tag
    last_cuid_tag = last_cuid_tag

emit_statistics(cuid_tag, cmatchid_tag, sum_shows, sum_clks, sum_price, sum_bids, ctr3_molecule)
