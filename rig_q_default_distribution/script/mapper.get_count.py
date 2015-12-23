import sys

count_dict = {}
init_array = []


for line in sys.stdin:
    # Init variable
    tag = "\N"
    init_array = []
    for i in range(0, 101):
        init_array.append(0)

    # Get data
    if line == "":
        continue
    line = line.strip().split("\t")
    rig_q = line[139]
    ovl_exp = line[72]
    
    # Label the tag of current line
    for _tag in ovl_exp.split("#"):
        if "534" in _tag: 
            tag = _tag
            break
    
    # Select the exp tag (tag contains "534")
    if tag != "\N":
        value = int(float(rig_q.split("#")[0]) * 100)
        if value > 100 or value < 0:
            value = 100
        if count_dict.has_key(tag):
            count_dict[tag][1] += 1
            count_dict[tag][2][value] += 1 
        else:
            init_array[value] = 1
            count_dict[tag] = [tag, 1, init_array]

for item in count_dict.values():
    distribution_array = "\1".join(map(lambda x: str(x), item[2]))
    print "\t".join((str(item[0]), str(item[1]), distribution_array))
