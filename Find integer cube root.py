# The integer cube root of a positive number  𝑛 is the smallest number  𝑖 such that  𝑖3≤𝑛 but  (𝑖+1)3>𝑛 . For
# instance, the integer cube root of  100 is  4 since  43≤100 but  53>100 . Likewise, the integer cube root of  1000
# is  10 .

# Write a function integerCubeRootHelper(n, left, right) that searches for the integer cube-root of n between left
# and right given the following pre-conditions:

# - 𝑛≥1
# - left < right
# - left3 < 𝑛
# - right3 > 𝑛


def integerCubeRootHelper(n, left, right):
    def cube(x):
        return x * x * x

    assert(n >= 1)
    assert(left < right)
    assert(left >= 0)
    assert(right < n)
    assert(cube(left) < n), f'{left}, {right}'
    assert(cube(right) > n), f'{left}, {right}'

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
    print(n)
    mid = (left + right) // 2
    if cube(mid) == n:
        return mid

    if cube(mid) >= n:

        if cube(mid +1) < n:
            return mid
        else:
            return integerCubeRootHelper(n, left, mid)
    if cube(mid) < n:
        if cube(mid + 1) == n:
            return mid + 1
        if cube(mid + 1) > n:
            return mid
        if cube(mid + 1) < n:
            return integerCubeRootHelper(n, mid+1, right)

def integerCubeRoot(n):
    assert( n > 0)
    if (n == 1):
        return 1
    if (n == 2):
        return 1
    return integerCubeRootHelper(n, 0, n-1)


assert (integerCubeRoot(1) == 1)
assert (integerCubeRoot(2) == 1)
assert (integerCubeRoot(4) == 1)
assert (integerCubeRoot(7) == 1)
assert (integerCubeRoot(8) == 2)
assert (integerCubeRoot(20) == 2)
assert (integerCubeRoot(26) == 2)
for j in range(27, 64):
    assert (integerCubeRoot(j) == 3)
for j in range(64, 125):
    assert (integerCubeRoot(j) == 4)
for j in range(125, 216):
    assert (integerCubeRoot(j) == 5)
for j in range(216, 343):
    assert (integerCubeRoot(j) == 6)
for j in range(343, 512):
    assert (integerCubeRoot(j) == 7)
print('Congrats: All tests passed! (10 points)')
