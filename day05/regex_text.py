import re

coordinate = re.compile('\d,\d')
substring = '0,9 -> 5,9'
coords = coordinate.findall(substring)
print(coords[0])