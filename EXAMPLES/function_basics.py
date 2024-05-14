import os

def say_hello():  # Function takes no parameters
    print("Hello, world")
    print()
    # If no return statement, return None

say_hello()  # Call function (arguments, if any, in () )

def get_hello():
    return "Hello, world"  # Function returns value


h = get_hello()  # Store return value in h
print(h)
print()
print(get_hello())


def sqrt(num=0):  # Function takes exactly one argument
    return num ** .5


m = sqrt(1234)  # Call function with one argument
n = sqrt(2)

print(f"m is {m:.3f} n is {n:.3f}")

print(f"{sqrt() = }")

def find_lines(search_term, *file_paths):
    for file_path in file_paths:
        with open(file_path) as file_in:
            for raw_line in file_in:
                if search_term in raw_line:
                    line = raw_line.rstrip()
                    print(os.path.basename(file_path), line)

find_lines("bird", '../DATA/alice.txt', '../DATA/parrot.txt')
print('-' * 60)
find_lines("junk")
find_lines("bird", '../DATA/parrot.txt')

mylist = ['a', 'b', 'c']

def update_list(the_list):
    the_list.append('wombat')

update_list(mylist)
print(f"{mylist = }\n")

king = "Albert"  # (file) global name
x = "wolverine"

def spam():
    x = 100  # x is local to spam()
    print(f"in spam(): x is {x}")
    print(f"in spam(): king is {king}")

m = spam()
print(f"in main: x is {x}")

