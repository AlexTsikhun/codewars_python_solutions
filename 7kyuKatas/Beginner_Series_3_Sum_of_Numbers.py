def get_sum(a,b):
    if b < a:
        return sum([i for i in range(b, a+1)])
    return sum(i for i in range(a, b+1))



print(get_sum(1, 2))

if __name__ == "__main__":
    assert get_sum(1, 0) == 1   # 1 + 0 = 1
    assert get_sum(1, 2) == 3   # 1 + 2 = 3
    assert get_sum(0, 1) == 1   # 0 + 1 = 1
    assert get_sum(1, 1) == 1   # 1 Since both are same
    assert get_sum(-1, 0) == -1    #-1 + 0 = -1
    assert get_sum(-1, 2) == 2     # -1 + 0 + 1 + 2 = 2
    print("ALL test passed!")