# break(Exit The Loop) ;
def pattern():
    i = 1
    while i < 10:
        print(i)
        i += 1
        if i == 5:
            break

    print("Done1")
    print("Done2")


pattern()
