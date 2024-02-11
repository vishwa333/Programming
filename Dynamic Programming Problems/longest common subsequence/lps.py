
def lcs_dp(list_of_strings : list) -> int:
    str1, str2 = list_of_strings[0], list_of_strings[1]
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

def lps_dp(input_string:str):
    reverse_string = input_string[::-1]
    return lcs_dp(([input_string,reverse_string]))


# This is the main function in python
if __name__ == '__main__':
    test_cases = ["GEEKSFORGEEKS","BANANA"]
    for test_case in test_cases:
        print("------------------")
        print("Testing for test case:", test_case)
        print("Longest Common SubSequence is of length : ", lps_dp(test_case))
