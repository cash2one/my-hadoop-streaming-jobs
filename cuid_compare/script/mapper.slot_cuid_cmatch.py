import sys

for line in sys.stdin:
    val = line.strip().split("\t")
    cuid = val[80]
    # cuid_tag = 0
    # represents that cuid is not existed.
    cuid_tag = 0
    # cuid_tag = 1
    # represents that cuid is existed.
    if cuid != "" and cuid != "-":
        cuid_tag = 1

    cmatchid = val[9]
    # cmatch_tag = 0
    # represents that cmatchid is not 222 or 223
    cmatchid_tag = 0
    # cmatch_tag = 1
    # represents that cmatchid is 222 or 223
    if cmatchid in ["222", "223"]:
        cmatchid_tag = 1
    # cmatch_tag = 2
    # represents that cmatchid is arbitrary

    new_val = (
        val[0],  # 0: show
        val[1],  # 1: clk
        val[2],  # 2: price
        val[19],  # 3: bid
        val[8],  # 4: dis
    )
    # No matter which cmatchid tag is, print the current result which represents the total cmatch.
    print "%s\t%s\t%s" % (cuid_tag, 2, "\1".join(new_val))
    # print the result of 222 or 223 cmatch.
    if cmatchid_tag == 1:
        print "%s\t%s\t%s" % (cuid_tag, cmatchid_tag, "\1".join(new_val))
