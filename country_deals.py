# import pymssql
# conn = pymssql.connect('db=foo;host=bar;user=blah;pw=buzz')
# cursor = conn.cursor()

countries_with_values = [
    'Switzerland', 'Italy', 'Spain', 'Indonesia', 'France', 'Peru', 'India', 'Kenya', 'Portugal',
    'Thailand'
]

countries_liked = ['Italy', 'Thailand', 'Kenya', 'Peru', 'Armenia', 'Croatia', 'Kazakhstan']

values = set(countries_with_values)
like = set(countries_liked)

print(f"{values = }")
print(f"{like = }\n")

to_visit = values & like # intersection (common elements)
print(f"{to_visit = }\n")

not_interested = values ^ like   # XOR (non-common elements)
print(f"{not_interested = }\n")

all_countries = values | like   # union (all unique elements)
print(f"{all_countries = }\n")

only_values = values - like   # remove elements of like from values
print(f"{only_values = }\n")

# cursor.execute('select c1, c2 from table where ....')
# set1 = set(conn.fetchall())
# cursor.close()


