#!/usr/bin/env python2
import json
my_data = json.loads(open("data.json.bzfeed").read())

for attribute, value in  my_data.iteritems():
    print '%s \n' % attribute
    print "-:\n";
    print '%s \n' % value
    print "-----------------:\n";
