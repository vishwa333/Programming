

def lis_dp(arr: list) -> int:
    n = len(arr)
    LIS = [0]*n
    LIS[0] = 1
    for i in range(1,n):
        tmp_max = 1
        for j in range(i-1,-1,-1):
            if arr[i]>arr[j]:
                tmp_max = max(tmp_max,LIS[j]+1)
        LIS[i]= tmp_max
    return max(LIS)


# This is the main function in python
if __name__ == '__main__':
    test_cases = [[1,2,3,1],[2,7,9,3,1],[3,10,2,1,20]]
    for test_case in test_cases:
        print("------------------")
        print("Testing for test case:",test_case)
        print("Longest increasing SubSequence is of length : ",lis_dp(test_case))
        