import sys

last_tag = "\N"
total_count = 0
distribution = []
for i in range(0, 101):
    distribution.append(0)

def accumulate_dis(dis1, dis2):
    if len(dis1) != len(dis2):
        print >> sys.stderr, "Invalid distribution emerged. dis1_len=%s, dis2_len=%s" % (len(dis1), len(dis2))
        exit(1)
    new_dis = []
    for i in range(0, len(dis1)):
        new_dis.append(str(int(dis2[i]) + int(dis1[i])))
    return new_dis

for line in sys.stdin:
    tag, _total_count, _distribution = line.strip().split("\t")
    _distribution = _distribution.strip().split("\1")

    if tag == last_tag:
        total_count += int(_total_count)
        distribution = accumulate_dis(_distribution, distribution)
    elif tag != last_tag and last_tag != "\N":
        print "#".join((last_tag, str(total_count), "\t".join(distribution)))
        total_count = int(_total_count)
        distribution = _distribution
    elif last_tag == "\N":
        total_count = int(_total_count)
        distribution = _distribution

    last_tag = tag

print "#".join((last_tag, str(total_count), "\t".join(distribution)))

