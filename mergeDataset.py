import json
import sys

if __name__ == '__main__':
	files = sys.argv[1:]

	res = []

	for f in files:
		with open(f) as content:
			dataset = json.load(content)

			for el in dataset:
				res.append(el)


	with open('raw_dataset.json', 'w+') as outfile:
		json.dump(res, outfile, indent=4, sort_keys=True)


