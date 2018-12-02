#!/usr/bin/env python3

import requests
response = requests.get('https://jsonplaceholder.typicode.com/todos/1')

# print the header information from the response
#print(response.headers)
print(response.json())
