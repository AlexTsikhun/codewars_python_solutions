
def wave(people):
    res = []
    for p in range(len(people)):
        upper = people[p].upper()
        str_with_upper = people.replace(people[p], upper)
        print(people[p], upper)
        res.append(str_with_upper)
    return res


# print(wave("hello"))
assert wave("hello") == ["Hello", "hEllo", "heLlo", "helLo", "hellO"]

