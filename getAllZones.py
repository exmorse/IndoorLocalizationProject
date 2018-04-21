import json

if __name__ == '__main__':
	with open('raw_dataset.json') as infile:
		dataset = json.load(infile)

	zonelist = set([])

	for el in dataset:
		zonelist.add(el['zone'])

	print zonelist
	
	with open('zonelist.json', 'w+') as outfile:
		json.dump(list(zonelist), outfile, indent=4, sort_keys=True)
