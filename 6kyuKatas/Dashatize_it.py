# Solution 1
def dashatize(n):
    if isinstance(n, int):
        _str = ""
        for i in str(n):
            if int(i) % 2 != 0 and : # and next not odd set `-`. if last not set -
                _str += f"-{i}-"
            else:
                _str += i
        return _str



if __name__ == "__main__":
    print(dashatize(6815))

    # assert dashatize(274) == '2-7-4'
    # assert dashatize(6815) == '68-1-5'
    #
    # print("ALL test passed!")
