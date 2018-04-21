from random import randint
import copy
from torch.autograd import Variable
import torch
import json

model = torch.load("home_model")

with open("aplist.json") as ap_file:
	aplist = json.load(ap_file)

with open("zonelist.json") as zone_file:
	zonelist = json.load(zone_file)

with open("raw_dataset.json") as dataset_file:
	dataset = json.load(dataset_file)

#test_sample = dataset[30]


with open("scan.json") as scan_file:
	test_data = json.load(scan_file)

total = [0] * len(zonelist)
test_input = [None] * len(aplist) * 2

for sample in test_data:
	for i in range(len(aplist)):
		test_input[i] = -100
		test_input[i + len(aplist)] = -100
	
		# For each scan sample in scan
		for j in range(len(sample)):
			if sample[j]['mac'] == aplist[i]:
				test_input[i] = 100
				test_input[i + len(aplist)] = int(sample[j]['signal_level_dBm'])
				if test_input[i + len(aplist)] > 0:
					test_input[i + len(aplist)] == -100

	estimation = model(Variable(torch.Tensor([test_input]))).data[0]

	selected = 0
	for i in range(len(estimation)):
		if estimation[i] > estimation[selected]:
			selected = i

	print estimation
	print "\tZone: " + str(zonelist[selected])
	total[selected] = total[selected] + 1


selected = 0
for i in range(len(total)):
	if total[i] > total[selected]:
		selected = i
print "Result: " + str(zonelist[selected])
