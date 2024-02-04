
#Dynamic
def rob_houses(nums : list) -> int:
    if(len(nums)<3):
        return max(nums)
    max_profit_on_robbing = [0]*len(nums) 
    max_profit_on_robbing[0] = nums[0]
    max_profit_on_robbing[1] = max(nums[0:2])
    for i in range(2,len(nums)):
        max_profit_on_robbing[i] = max(max_profit_on_robbing[i-2]+nums[i],max_profit_on_robbing[i-1])
    return max_profit_on_robbing[len(nums)-1]

# DP Optimised
def rob_houses_optimal(nums : list) -> int:
    if(len(nums)<3):
        return max(nums)
    rob_n_2 = nums[0]
    rob_n_1 = max(nums[0:2])
    for i in range(2,len(nums)):
        max_profit_on_robbing = max(rob_n_2+nums[i],rob_n_1)
        rob_n_2 = rob_n_1
        rob_n_1 =  max_profit_on_robbing
        
    return max_profit_on_robbing

# This is the main function in python
if __name__ == '__main__':
    test_cases = [[1,2,3,1],[2,7,9,3,1]]
    for test_case in test_cases:
        print("------------------")
        print("Testing for test case:",test_case)
        print("MAx profit that can be made : ",rob_houses(test_case))
        print("MAx profit that can be made (Optimsied): ",rob_houses_optimal(test_case))