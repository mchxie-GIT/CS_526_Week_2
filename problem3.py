def ways(n):
    # One way to finish when no steps remain; none if we overshoot.
    if n == 0:
        return 1
    if n < 0:
        return 0
    return ways(n - 1) + ways(n - 2) + ways(n - 3)


if __name__ == '__main__':
    print('ways(3) =', ways(3))
    print('ways(5) =', ways(5))
    print('ways(10) =', ways(10))
