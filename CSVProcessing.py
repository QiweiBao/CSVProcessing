# coding: utf-8

import csv
data = '1993'

readfilename = 'csv_test.csv'
writefilename = 'csv_test_select1993.csv'
selectItem = 'age'

f = file(readfilename, 'r')
f2 = file(writefilename, 'wb+')
c = []
b = []
d = []
i = 0

writer = csv.writer(f2)
#writer.writerow(['name', 'age', 'tele'])
f_csv = csv.DictReader(f)
for line in f_csv:
	if line.has_key(selectItem) == False:
		print "err"
		pass
		print "err1"
	elif line[selectItem]:
		temp = line[selectItem]
		if temp.find(data) == 0 :
			print line
			for key, value in line.items():
				c.append(value)
				b.append(key)
			#writer.writerow(b)
			d = b
			writer.writerow(c)
			c = []
			b = []
writer.writerow(d)
f2.close
f.close()
