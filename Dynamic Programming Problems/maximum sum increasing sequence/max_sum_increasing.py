
def max_sum_dp_only_increasing(arr: list) -> int:
    n = len(arr)
    max_sum = arr[0]
    tmp_max = 0
    for i in range(1,n):
        if(arr[i]>arr[i-1]):
            tmp_max = tmp_max+arr[i]
            max_sum = max(tmp_max,max_sum)
        else:
            tmp_max = arr[i]
    return max_sum

def max_sum_dp(arr: list) -> int:
    n = len(arr)
    LIS = [0]*n
    LIS[0] = 1
    max_sum = [0]*n
    max_sum[0] = arr[0]
    for i in range(1,n):
        tmp_max = 1
        tmp_sum = arr[i]
        for j in range(0,i):
            if arr[i]>arr[j]:
                tmp_max = max(tmp_max,LIS[j]+1)
                #tmp_sum = max(tmp_sum,max_sum[j]+arr[i])
                tmp_sum = max_sum[j] + arr[i]
        max_sum[i] = (tmp_sum)
        LIS[i]= tmp_max
    return max(max_sum)


# This is the main function in python
if __name__ == '__main__':
    test_cases = [[1,101,2,3,100,4,5],[3,4,5,10],[10,5,4,3],[1,101,2,3,4,5]]
    for test_case in test_cases:
        print("------------------")
        print("Testing for test case:" ,test_case)
        print("maximum sum of longest sequence : " ,max_sum_dp(test_case))
