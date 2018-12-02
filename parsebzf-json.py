#!/usr/bin/python
import demjson

#json = '{"a":1,"b":2,"c":3,"d":4,"e":5}';

#text = demjson.decode(json)
#print  text
#import json
#$from pprint import pprint

with open('data.json.bzfeed') as data_file:    
    data = demjson.decode(data_file)
   # data = data_file
#print data
