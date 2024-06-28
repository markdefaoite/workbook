"""
Implement an algorithm that will implement the  𝑘   way merge by calling twoWayMerge repeatedly as follows:
1. Call twoWayMerge on consecutive pairs of lists twoWayMerge(lists[0], lists[1]), ... , twoWayMerge(lists[k-2], lists[k-1])
(assume k is even).

2. Thus, we create a new list of lists of size k/2.

3. Repeat steps 1, 2 until we have a single list left.

"""

def twoWayMerge(lst1, lst2):
    # Implement the two way merge algorithm on
    #          two ascending order sorted lists
    # return a fresh ascending order sorted list that
    #          merges lst1 and lst2
    # your code here

    # given a list_of_lists as input,
    #   if list_of_lists has 2 or more lists,
    #        compute 2 way merge on elements i, i+1 for i = 0, 2, ...
    #   return new list of lists after the merge
    #   Handle the case when the list size is odd carefully.



def oneStepKWayMerge(list_of_lists):
    if (len(list_of_lists) <= 1):
        return list_of_lists
    ret_list_of_lists = []
    k = len(list_of_lists)
    for i in range(0, k, 2):
        if (i < k - 1):
            ret_list_of_lists.append(twoWayMerge(list_of_lists[i], list_of_lists[i + 1]))
        else:
            ret_list_of_lists.append(list_of_lists[k - 1])
    return ret_list_of_lists


# Given a list of lists wherein each
#    element of list_of_lists is sorted in ascending order,
# use the oneStepKWayMerge function repeatedly to merge them.
# Return a single merged list that is sorted in ascending order.
def kWayMerge(list_of_lists):
    k = len(list_of_lists)
    if k == 1:
        return list_of_lists[0]
    else:
        new_list_of_lists = oneStepKWayMerge(list_of_lists)
        return kWayMerge(new_list_of_lists)



# BEGIN TESTS
lst1= kWayMerge([[1,2,3], [4,5,7],[-2,0,6],[5]])
assert lst1 == [-2, 0, 1, 2, 3, 4, 5, 5, 6, 7], "Test 1 failed"

lst2 = kWayMerge([[-2, 4, 5 , 8], [0, 1, 2], [-1, 3,6,7]])
assert lst2 == [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8], "Test 2 failed"

lst3 = kWayMerge([[-1, 1, 2, 3, 4, 5]])
assert lst3 == [-1, 1, 2, 3, 4, 5], "Test 3 Failed"

print('All Tests Passed = 15 points')
#END TESTS