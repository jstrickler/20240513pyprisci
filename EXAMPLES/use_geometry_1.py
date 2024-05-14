import sys
# find my_package/mathstuff/geometry.py
import my_package.mathstuff.geometry as geometry

a1 = geometry.circle_area(8)
a2 = geometry.rectangle_area(10, 12)
a3 = geometry.square_area(7.9)
print(a1, a2, a3)

# module search locations
# 1. current folder
# 2. folders in PYTHONPATH
# 3. folders in sys.prefix/lib
print(f"{sys.prefix = }\n")
for path in sys.path:
    print(path)
