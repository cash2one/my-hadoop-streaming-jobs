# Function for loading word dictionary into a dict.
def load_dict(dir_name):
	fin=open(dir_name, "r")
	my_dict = {}
	for line in fin:
		flist = line.strip().split("\t")
		key = flist[0]
		my_dict[key] = flist[2]
	fin.close()
	return my_dict

if __name__ == "__main__":
	my_dict = load_dict("../resource/20150922_cn_dict.txt")
	for key, value in my_dict.iteritems():
		print key, value