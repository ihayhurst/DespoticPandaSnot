#!/usr/bin/env python3
import json

my_data = json.loads(open("buzzdata2.json").read())
 #dict- where 'itemListElement' contains list of dicts where 'item' is a dict containing 'name', 'type', 'image' and 'url elements

my_list =my_data['itemListElement']
for idx,li in enumerate(my_list):
	print(li['item']['name'])
