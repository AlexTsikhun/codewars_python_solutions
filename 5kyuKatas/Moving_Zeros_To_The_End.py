
def move_zeros(array):
    z = 0
    for a in array:
        if a == 0 and type(a) is int:
            array.remove(a)
            z += 1

    return array, z

print(move_zeros([2, False,1,0,1,2,0,1,3,"a"]))
# assert move_zeros([False,1,0,1,2,0,1,3,"a"]) == [False,1,1,2,1,3,"a",0,0]
print([2, False,1,0,1,2,0,1,3,"a"])