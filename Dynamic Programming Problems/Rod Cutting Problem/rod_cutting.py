

def cut_rod(prices: list, length_of_rod: int) -> int:
    max_price_for_length = [0]*(length_of_rod+1) 
    #print(max_price_for_length)
    for i in range(1,length_of_rod+1):
        tmp_price = prices[i-1]
        for j in range(i):
            #print("(i,j)",i,j)
            tmp_price = max(tmp_price,prices[j]+max_price_for_length[i-j])
        max_price_for_length[i] = tmp_price
        #print(max_price_for_length)
    return max_price_for_length[n]


# This is the main function in python
if __name__ == '__main__':
    p = [1,5,8,9,10,17,17,20]
    n = len(p)
    max_price = cut_rod(p,n)
    print("Max price is :",max_price)