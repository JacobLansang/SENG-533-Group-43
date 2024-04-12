# Generates Redis tables using data from json files. These file names are stored as a list and are not loaded dynamically.
# Please note that running this script multiple times will not create duplicate keys.

import redis
import json
from redis.commands.json.path import Path

r = redis.Redis(host='localhost', port=6379)
files = ['clinics.json', 'owners.json', 'petrecords.json']

for file_name in files:
	file = open('tables/' + file_name)
	content = json.load(file)

	for i, data in enumerate(content):
#		print(data)
		# Creating a key based on the file name without the extension and a counter (ex. "owner-1")
		key = file_name.split('.')[0] + '-' + str(i + 1)
		r.json().set(key, Path.root_path(), data)

	file.close()

print('Script completed!')
