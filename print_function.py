person = "Taylor Swift"
city = "Nashville"
value = 23.328

print(person, city, value)
#  str(person) + ' ' + str(city) + ' ' + str(value) + '\n'
print(person)  # implied \n
print(city)  # \n 
print(person, city, value, sep="/")
print(person, city, value, sep="+")
print(person, city, value, sep=", ")
print(person, city, value, sep="")
print()
print(person, end=" ")
# if ...:
#     print(...)
print("====")

print(city + ": " + person)

s = f"{city}: {person}"
print(s)
print(f"{city}: {person}")
print(f"2 + 2 is {2 + 2}")

print(f"{city=}")
print(f"{2 + 2 = }")
print(f"{city = }")   # f"city = {city}"

print(f"this is weird {{}} {5 * 10}")

print(value)
print(f"value is {value}")
print(f"value is {value:.2f}")
