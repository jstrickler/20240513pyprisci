d1 = dict()  # empty dict
d2 = {'m': 99, 'x': 15, 'a': 45}  # assign literal dict
d3 = {}   # empty dict

d2['t'] = 95
d2['v']= 8

print(f"{d2 = }\n")

index = 5
d2[index] = "wombat"

d2['wombat'] = [1, 2, 3]

print(f"{d2 = }\n")

airports = {
   'EWR': 'Newark',
   'YYZ': 'Toronto',
   'SJU': 'San Juan',
   'MCI': 'Kansas City',
   'SFO': 'San Francisco',
   'RDU': 'Raleigh-Durham',
   'LTN': 'London',  # (Luton)
   'LGW': 'London',  # (Gatwick)
   'LHR': 'London',  # (Heathrow)
   'SJC': 'San Jose',
   'MCO': 'Orlando',
   'YCC': 'Calgary',
   'ABQ': 'Albuquerque',
   'OAK': 'Oakland',
   'SMF': 'Sacramento',
   'YOW': 'Ottawa',
   'IAD': 'Dulles',
}

print(f"{airports['YCC'] = }\n")
airports['LAX'] = "Los Angeles"
print(f"{airports = }\n")
airports['RDU'] = 'Durham-Raleigh'
print(f"{airports = }\n")

print(f"{airports['SMF'] = }")

if 'LGA' in airports:
    print(f"{airports['LGA'] = }")

print(f"{airports.get('LGA') = }")
print(f"{airports.get('LGA', 'N/A') = }")
print(f"{airports.get('RDU', 'N/A') = }")
print()

# for key, value in ANY_DICT.items():
for code, city in airports.items():
    print(code, city)
print()

print(f"{airports.items() = }\n")


