def summation(start, end):
    difference = abs(end - start)
    summation = (difference * (difference + 1)) / 2
    return round(summation)

print(summation(5, 14))