
def lrs_dp(list_of_strings : list) -> int:
    str1, str2 = list_of_strings[0], list_of_strings[1]
    str1 = ["-"]+[x for x in str1]
    str2 = ["-"]+[x for x in str2]
    n = len(str1)
    m = len(str2)
    lrs = [[0]*m for i in range(n)]
    direction = [['-']*m]*n
    for i in range(1, n):
        for j in range(1, m):
            if str1[i] == str2[j] and i != j:
                lrs[i][j] = lrs[i-1][j-1]+1
                direction[i][j] = "d"
            elif lrs[i-1][j] > lrs[i][j-1]:
                lrs[i][j] = lrs[i-1][j]
                direction[i][j] = "U"
            else:
                lrs[i][j] = lrs[i][j-1]
                direction[i][j] = "D"
    return lrs[n-1][m-1]


# This is the main function in python
if __name__ == '__main__':
    test_cases = ["aabebcdd","BANANA","abab","axxxy","aaxxxy"]
    for test_case in test_cases:
        print("------------------")
        print("Testing for test case:", test_case)
        print("Longest Common SubSequence is of length : ", lrs_dp([test_case,test_case]))
