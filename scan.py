import pprint
import iwlist
import json

INTERFACE = 'wlan0'
FILENAME = 'scan.json'
FIELD_TO_IGNORE = [
	'cellnumber',
	'encryprtion',
	'frequency',
	'frequency_units',
	'mode',
	'essid',
	'signal_total'
]


scans = []
pp = pprint.PrettyPrinter(indent=4)

for i in range(5):
	content = iwlist.scan(interface=INTERFACE)
	cells = iwlist.parse(content)

	for el in cells:
		for field in FIELD_TO_IGNORE:
			el.pop(field, None)

	scans.append(cells)
	#pp.pprint(cells)
	
with open(FILENAME, 'w+') as outfile:
	json.dump(scans, outfile)
