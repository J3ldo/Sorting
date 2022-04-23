import random


randomlist = []
sortedlist = []

for i in range(500):
	randomlist.append(random.randint(0, 500))


for i, item in enumerate(randomlist):
	for b, sorteditem in enumerate(sortedlist):
		if item < sorteditem:
			sortedlist.insert(b, item)
			break

	else:
		sortedlist.append(item)

print(sortedlist)
