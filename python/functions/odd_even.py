# return (Exit The function)
def even_odd_check(num: int) -> str:
    if num % 2 == 0:
        print("Even")
        # return "EVEN"
    print("Odd")
    # return "ODD"


ans = even_odd_check(60)
print(ans)


def vote(age: int) -> str:
    if age < 18:
        return "you can not vote"
    return "you can vote"


x = vote(30)
print(x)


def vote(age: int) -> str:
    if age < 18:
        print("you can not vote")
        return
    print("you can vote")


x = vote(30)
print(x)
