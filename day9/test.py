from collections import defaultdict
import pandas as pd


# array = [6,17,2,6,2,34]
# # max_value = max(array)
# # max_index = array.index(max_value)

# # print(max_index)
# print(array)
# new_array = array.copy()
# new_array.remove(2)
# print(new_array)
# print(array)

# df = pd.DataFrame(index = range(5), columns = range(10))
# print(df)

d = defaultdict()
d["a"] = 1
d["b"] = 2
d["c"] = 2
try:
    d["c"] += 1
except KeyError:
    d["c"] = 0
 
print(d)

