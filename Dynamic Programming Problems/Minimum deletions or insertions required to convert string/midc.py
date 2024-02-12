
def lcs_dp(str1:str, str2 : str ) -> int:
    str1 = ["-"]+[x for x in str1]
    str2 = ["-"]+[x for x in str2]
    n = len(str1)
    m = len(str2)
    lcs = [[0]*m for i in range(n)]
    direction = [['-']*m]*n
    for i in range(1, n):
        for j in range(1, m):
            if str1[i] == str2[j]:
                lcs[i][j] = lcs[i-1][j-1]+1
                direction[i][j] = "d"
            elif lcs[i-1][j] > lcs[i][j-1]:
                lcs[i][j] = lcs[i-1][j]
                direction[i][j] = "U"
            else:
                lcs[i][j] = lcs[i][j-1]
                direction[i][j] = "D"
    return lcs[n-1][m-1]

def midc(str1:str, str2 : str ):
    m = len(str1)
    n = len(str2)
    lcs_length = lcs_dp(str1, str2)
    print("Minimum deletions :", m-lcs_length)
    print("Minimum Insertions :", n - lcs_length)


# This is the main function in python
if __name__ == '__main__':
    test_cases = [["heap", "pea"],["geeksforgeeks","geeks"]]
    for test_case in test_cases:
        print("------------------")
        print("Testing for test case:", test_case)
        midc(test_case[0], test_case[1])
