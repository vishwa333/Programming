
def lss_dp(list_of_strings : list) -> int:
    str1, str2 = list_of_strings[0], list_of_strings[1]
    str1 = ["-"]+[x for x in str1]
    str2 = ["-"]+[x for x in str2]
    n = len(str1)
    m = len(str2)
    lss = [[0]*m for i in range(n)]
    direction = [['-']*m]*n
    for i in range(1, n):
        for j in range(1, m):
            if str1[i] == str2[j]:
                lss[i][j] = lss[i-1][j-1]+1
                direction[i][j] = "d"
            else:
                lss[i][j] = lss[i-1][j]
                direction[i][j] = "U"
    ret = -1
    for i in range(n):
        ret = max(ret,max(lss[i]))
    return ret


# This is the main function in python
if __name__ == '__main__':
    test_cases = [["ABCD","BACDBDCD"],["ABDC","BACDBDCD"]]
    for test_case in test_cases:
        print("------------------")
        print("Testing for test case:", test_case)
        print("Longest Common SubSequence is of length : ", lss_dp(test_case))
