s1 = "spam\n"   # all 4 are the same
s2 = 'spam\n'
s3 = """spam\n"""
s4 = '''spam\n'''

print("Guido's the ex-BDFL of Python")
print()
print('Guido is the ex-"BDFL" of Python')
print()
print("""Guido's the ex-"BDFL" of Python""")
print('''Guido's the ex-"BDFL" of Python''')

query = """
select first_name, last_name, zip_code
from customers
where state = "IA"
order by zip_code
"""

s5 = r"spam\n"
print(s5)
