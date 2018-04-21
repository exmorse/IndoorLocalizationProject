import json

if __name__ == '__main__':
	with open('raw_dataset.json') as infile:
		dataset = json.load(infile)

	aplist = set([])

	for el in dataset:
		for ap in el['scan']:
			aplist.add(ap['mac'])

	print aplist
	
	with open('aplist.json', 'w+') as outfile:
		json.dump(list(aplist), outfile, indent=4, sort_keys=True)
