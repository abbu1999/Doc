"""
  colum
    j---------->
    I  * * * * * 
row |  * * * * * 
    |  * * * * * 
    |  * * * * *
    |  * * * * *
"""

"""
for i in range(1, 6):
    for j in range(1, 6):
        print("*", end=" ")
    print()


for i in range(1, 6):
    for j in range(1, 6):
        print(j, end=" ")
    print()

for i in range(1, 6):
    for j in range(1, 6):
        print(i, end=" ")
    print()

for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

n = 10
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

for i in range(1, 6):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

"""

"""
5
4 5
3 4 5
2 3 4 5
1 2 3 4 5
"""

# for i in range(5, 0, -1):
#     for j in range(i, 6):
#         print(j, end=" ")
#     print()

n = 8
for i in range(n, 0, -1):
    for j in range(i, n + 1):
        print(j, end=" ")
    print()
