import sys
import json

if __name__ == '__main__':
	fileName = sys.argv[1]

	with open(fileName) as content:
		dataset = json.load(content)

	print len(dataset)
