

def lis_dp(arr: list) -> int:
    n = len(arr)
    LIS = [0]*n
    LIS[0] = 1
    for i in range(1,n):
        tmp_max = 1
        for j in range(i-1,-1,-1):
            if arr[i][0]>arr[j][1]:
                tmp_max = max(tmp_max,LIS[j]+1)
        LIS[i]= tmp_max
    return max(LIS)


# This is the main function in python
if __name__ == '__main__':
    test_cases = [[[5,24],[39,60],[15,28],[27,40],[50,90],[106,111]]]
    for test_case in test_cases:
        print("------------------")
        print("Testing for test case:",test_case)
        print("Max. Length Chain paris is of length : ",lic_dp(test_case))
        