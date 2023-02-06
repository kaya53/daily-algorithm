
import sys

a = []
for x in range(30):
    a.append(x)
    print(sys.getsizeof(a))