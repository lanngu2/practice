def flatten(l):

    try:
        return flatten(l[0]) + (flatten(l[1:]) if len(l) > 1 else []) if type(l) is list else [l]
    except IndexError:
        return []
res = ["a", "b", "c", ["e", "d", "f", ["g", "h", ["k", "l"]], "m", "o"], "p"]
print(flatten(res))