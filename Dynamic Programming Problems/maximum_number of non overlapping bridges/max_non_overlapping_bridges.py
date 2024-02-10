import sys
# caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1, '../longest_increasing_subsequence')

from lis import *


def sort_list(list1, list2):
    zipped_pairs = zip(list2, list1)
    #print(zipped_pairs)
    #print(sorted(zipped_pairs))
    z = [x for _, x in sorted(zipped_pairs)]
   #print(z)
    return z


def mnob(city_banks) -> int:
    bank_a = city_banks[0]
    bank_b = city_banks[1]
    sorted_list_b = sort_list(bank_b,bank_a)
    #print(sorted_list_b)
    return lis_dp(sorted_list_b)


# This is the main function in python
if __name__ == '__main__':
    test_cases = [[[8, 1, 4, 3, 5, 2, 6, 7], [1, 2, 3, 4, 5, 6, 7, 8]]]


    for test_case in test_cases:
        print("------------------")
        print("Testing for test case:",test_case)
        print("Maximum number of Overlapping birdges : ",mnob(test_case))