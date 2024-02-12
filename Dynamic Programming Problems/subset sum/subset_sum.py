
def is_subset_sum(input_set :list, sum_to_get: int) -> bool:
    n = len(input_set)
    input_set = [0] + input_set
    s_sum = [[False] * (sum_to_get + 1) for x in range(n + 1)]

    for i in range(n):
        s_sum[i][0] = True
    for i in range(1, n + 1):
        for sum_i in range(1, sum_to_get + 1):
            if sum_i >= input_set[i]:
                s_sum[i][sum_i] = s_sum[i - 1][sum_i] | s_sum[i - 1][sum_i - input_set[i]]
            else:
                s_sum[i][sum_i] = s_sum[i - 1][sum_i]
    return s_sum[n][sum_to_get]


if __name__ == '__main__':
    test_cases = [[[3, 34, 4, 12, 5, 2], 9], [[3, 34, 4, 12, 5, 2], 30], [[3, 34, 4, 12, 5, 2], 36]]
    for test_case in test_cases:
        print("------------------")
        print("Testing for test case:", test_case)
        print(f"With the given set the sum {test_case[1]} is acheivable :", is_subset_sum(test_case[0], test_case[1]))
