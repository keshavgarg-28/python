import re
from functools import reduce

data = ["a10", "b", "c30", "xyz"]
filtered = list(filter(lambda x: re.search(r"\d+", x), data))

numbers = list(map(lambda x: int(re.search(r"\d+", x).group()), filtered))

total = reduce(lambda a, b: a + b, numbers)
print(total)