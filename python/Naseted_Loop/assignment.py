"""
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5

for i in range(1, 6):
    for j in range(1, 6):
        print(j, end=" ")
    print()

1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

5
4 5
3 4 5
2 3 4 5
1 2 3 4 5

for i in range(1, 6):
    for j in range(6 - i, 6):
        print(j, end=" ")
    print()
5
5 4
5 4 3
5 4 3 2
5 4 3 2 1
"""

for i in range(1, 6):
    for j in range(6, 6 - i):
        print(j, end=" ")
    print()
