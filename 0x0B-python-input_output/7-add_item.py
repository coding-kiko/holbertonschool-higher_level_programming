#!/usr/bin/python3
"""modules containing that reads text and prints"""


import json
from os import path
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
"""import jssasonn utilities"""

if path.isfile("add_item.json"):
    actual = load_from_json_file("add_item.json")
else:
    actual = []
for i in range(1, len(argv)):
    actual.append(argv[i])
save_to_json_file(actual, "add_item.json")
