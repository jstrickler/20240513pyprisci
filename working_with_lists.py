cities = []   # empty list

cities.append('Durham')
print(f"{cities = }\n")
cities.append('Toronto')
print(f"{cities = }\n")
cities.insert(0, 'Chicago')
print(f"{cities = }\n")
cities.insert(2, "Mississauga")
print(f"{cities = }\n")
more_cities = ['Guelph', 'Kitchener', 'Hamilton']
cities.extend(more_cities)
print(f"{cities = }\n")

target_city = "Durham"

print(target_city in cities)

#  LIST.append(obj)   LIST.insert(pos, obj)   LIST.extend(iterable)

del cities[1]
print(f"{cities = }\n")

cities.remove('Guelph')  # brute-force
print(f"{cities = }\n")

city = cities.pop()
print(f"{city = }")
print(f"{cities = }\n")

city = cities.pop(1)
print(f"{city = }")
print(f"{cities = }\n")

# del LIST[pos]   LIST.remove(value)   x = LIST.pop(pos=-1)

cities = ['Chicago', 'Durham', 'Mississauga', 'Toronto', 'Guelph', 'Kitchener', 'Hamilton']

print(f"{cities[0] = }")
print(f"{cities[5] = }")
print(f"{cities[-1] = }")
print(f"{cities[-3] = }")

# LIST[start-at:stop-before:count-by]

print(f"{cities[0:3] = }")
print(f"{cities[2:5] = }")
print(f"{cities[:4] = }")
print(f"{cities[3:] = }")
print(f"{cities[:] = }")
print(f"{cities[-3:] = }")
print()

person = "Taylor Swift"
print(f"{person[:6] = }")
print(f"{person[-5:] = }")
print(f"{person[4:6] = }")
print()

print(f"{cities = }\n")

# for VAR ... in ITERABLE:
for city in cities:
    print(city.upper())
print()

for char in person:
    print(char, end="-")
print('\n')

print(f"{cities = }\n")

c0 = []
for c in cities:
    value = c.upper()
    c0.append(value)
print(f"{c0 = }\n")

c1 = [c.upper() for c in cities]   # list comprehension
print(f"{c1 = }\n")

#  [value for var in iterable if condition]

c2 = [c[:3] for c in cities]
print(f"{c2 = }\n")

c2 = []
for c in cities:
    c2.append(c[:3])


c3 = [c.upper() for c in cities if len(c) > 6]
print(f"{c3 = }\n")

c3 = []
for c in cities:
    if len(c) > 6:
        c3.append(c.upper())




nums = [800, 80, 1000, 32, -3, 8, 18, 255, 400, 5, 5000]

f = [float(n) for n in nums if n > 300]
print(f"{f = }\n")

reversed_nums = reversed(nums)
print(f"{reversed_nums = }\n")

for num in reversed_nums:
    print(num)
print()

# list comprehension
upper_cities = [c.upper() for c in cities]

# generator expression
upper_cities_gen = (c.upper() for c in cities)   #  () rather than []

print(f"{upper_cities_gen = }\n")
for city in upper_cities_gen:
    print(city)
print()

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'), 
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Thomas', 'Kurtz', 'BASIC', '1928-02-28'),
    ('Ada', 'Lovelace', 'Analytical Engine', '1815-12-10'),
    ('Grace', 'Hopper', 'COBOL', '1906-12-09'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

products = [p[2] for p in people]
print(f"{products = }\n")

names = ((p[0], p[1]) for p in people)
print(f"{names = }\n")
for name in names:
    print(name)

















