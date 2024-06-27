


def integerCubeRootHelper(n, left, right):
    def cube(x):
        return x * x * x

    assert(n >= 1)
    assert(left < right)
    assert(left >= 0)
    assert(right < n)
    assert(cube(left) < n), f'{left}, {right}'
    assert(cube(right) > n), f'{left}, {right}'
    # your code here

    if n < 8:
        return 1
    elif n < 27:
        return 2

    # for i in range(left,right):
    #     i_cubed = cube(i)
    #     i_plus_cubed = cube(i + 1)
    #     if cube(i) <= n:
    #         if n < i_plus_cubed:
    #             return i

    mid = (left + right) // 2
    if cube(mid) == n:
        return mid
    if cube(mid) >= n > cube(mid + 1):
        return mid

    elif cube(mid) > n:
        return integerCubeRootHelper(n, left, mid)

    elif cube(mid) < n:
        return integerCubeRootHelper(n, mid +1, right )

def integerCubeRoot(n):
    assert( n > 0)
    if (n == 1):
        return 1
    if (n == 2):
        return 1
    return integerCubeRootHelper(n, 0, n-1)



# assert(integerCubeRoot(1) == 1)
# assert(integerCubeRoot(2) == 1)
# assert(integerCubeRoot(4) == 1)
# assert(integerCubeRoot(7) == 1)
# assert(integerCubeRoot(8) == 2)
# assert(integerCubeRoot(20) == 2)
# assert(integerCubeRoot(26) == 2)
for j in range(27, 64):
    assert(integerCubeRoot(j) == 3)
for j in range(64,125):
    assert(integerCubeRoot(j) == 4)
for j in range(125, 216):
    assert(integerCubeRoot(j) == 5)
for j in range(216, 343):
    assert(integerCubeRoot(j) == 6)
for j in range(343, 512):
    assert(integerCubeRoot(j) == 7)
print('Congrats: All tests passed! (10 points)')