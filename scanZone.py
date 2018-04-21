import pprint
import iwlist
import json
import sys
import time

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

pp = pprint.PrettyPrinter(indent=4)

if __name__ == '__main__':

	if (len(sys.argv) != 3):
		print "Usage: " + sys.argv[0] + " ZoneName " + "SampleNumber"
		exit()

	zoneName = sys.argv[1]
	try:
		sampleNumber = int(sys.argv[2])
	except:
		print "Non valid sample number"
		exit()
	res = []

	for i in range(sampleNumber):
		print "Scanning " + str(i+1) + "/" + str(sampleNumber)
		content = iwlist.scan(interface=INTERFACE)
		cells = iwlist.parse(content)

		for el in cells:
			for field in FIELD_TO_IGNORE:
				el.pop(field, None)

		# Corrupted data with positive dBm
		for sample in cells:
			if int(sample['signal_level_dBm']) > 0:
				print 'Adjusting corrupted dBm'
				sample['signal_level_dBm'] = "-100"		

		obj = {}
		obj['scan'] = cells
		obj['zone'] = zoneName		
		if cells != []:
			res.append(obj)
		else:
			print 'Failed scan'
		time.sleep(2)

	#pp.pprint(res)
	
	with open(zoneName + '.json', 'w+') as outfile:
		json.dump(res, outfile, indent=4, sort_keys=True)
