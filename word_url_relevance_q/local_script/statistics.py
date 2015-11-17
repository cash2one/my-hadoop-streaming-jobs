import sys

matrix = []

for line in sys.stdin:
	matrix.append(line.strip().split("\t"))
	
# Average
average_q = 0
for row in matrix:
	average_q += float(row[10])
average_q /= len(matrix)
print "Average Q of all records is %s." % average_q

classes = [
	["comment1", "types when score is 0", 4],
	["mark", "score", 9]
]
for cls in classes:
	name = cls[0]
	desc = cls[1]
	index = cls[2]
	result_comment = {}
	for row in matrix:
		result_comment[row[index]] = {}
	for row in matrix:
		if result_comment[row[index]].has_key("sum"):
			result_comment[row[index]]["sum"] += float(row[10])
		else:
			result_comment[row[index]]["sum"] = float(row[10])
		if result_comment[row[index]].has_key("count"):
			result_comment[row[index]]["count"] += 1.0
		else:
			result_comment[row[index]]["count"] = 1.0 
	print "Class: %s (%s) result are:" % (name, desc)
	for key, value in result_comment.items():
		print "[%s] Average Q is %s" % (key, value["sum"]/value["count"])


