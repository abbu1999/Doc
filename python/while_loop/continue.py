# continue (esc below code and rerun the rest the code)
# Continue : Breaks the iteration and start with the next iteration
"""
i = 1
while i <= 10:
    print(i)
    if i == 5:
        continue
    i += 1
"""

"""
i = 1
while i <= 10:
    if i == 5:
        continue
    print(i)
    i += 1
"""

"""
i = 1
while i <= 10:
    print(i)
    i += 1
    if i == 5:
        continue
"""

i = 1
while i <= 10:
    if i == 5:
        i += 1
        continue
    print(i)
    i += 1
