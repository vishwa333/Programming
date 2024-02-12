
def knapsack01(W: list, P: list, M: int=0) -> int:
    ks01 =[[0]*(M+1) for x in range(len(P)+1)]
    W = [0] + W
    P = [0] + P
    n = len(P)
    for i in range(1,n):
        for w in range(1,M+1):
            if W[i] > w:
                ks01[i][w] = ks01[i-1][w]
            elif (ks01[i-1][w]) > (ks01[i-1][w-W[i]]+P[i]):
                ks01[i][w] = ks01[i-1][w]
            else:
                ks01[i][w] = ks01[i-1][w-W[i]]+P[i]
    return ks01[n-1][M]


if __name__ == '__main__':
    test_cases = [[[2,3,4,5],[3,4,5,6],5]]
    for test_case in test_cases:
        print("------------------")
        print("Testing for test case:", test_case)
        print("Profit for the given test case :", knapsack01(test_case[0], test_case[1],test_case[2]))