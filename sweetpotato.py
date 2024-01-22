# sweetpotato.py - Got this from RealPython.com

import yaml
from pprint import pprint

def show_spud(filename):
    with open(filename, mode="rb") as file:
        result = yaml.safe_load(file)
        #pprint(result, indent=2, sort_dicts=False)
        return result