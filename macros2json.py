#!/usr/bin/env python3

with open("experiments/macros_SERVICES.txt","r") as f:
    data = f.readlines()

# data formatted as:
# ------------------
# HOSTACTIONURL : https://192.168.1.2:10000/
# HOSTADDRESS : 192.168.1.2
# HOSTALIAS : Bogus Host 1
# ------------------

# nm = nagios macro
nm = dict()

for l in data:
    # l is short for line, k=key, v=value
    l = l.strip()
    k, v = l.split(":", 1)
    k = k.strip()
    v = v.strip()
    nm.update({k:v})

import json
print(json.dumps(nm))

# from pprint import pprint
# pprint(nm)

