from functools import singledispatch


@singledispatch
def mysum(iterable):
    return sum(iterable)

@mysum.register
def _(iterable: str):
    try:
        return sum(map(int, iterable))
    except ValueError:
        raise TypeError

@mysum.register
def _(iterable: dict):
    return sum(iterable.values())


print(mysum([1, 2, 3, 4, 5]))
print(mysum((1, 2, 3, 4, 5)))
print(mysum({1, 2, 3, 4, 5}))
print(mysum({"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}))
print(mysum("12345"))
try:
    print(mysum("abc12345"))
except TypeError:
    print("Caught")