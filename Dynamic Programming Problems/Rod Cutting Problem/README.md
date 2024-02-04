# Problem Statement 
Give a rod of lenght n and you want to cut up the rod and sell the pirces in a way that maximizes the total amount og money you get. 

## Brute force method
Get the maximum possible cost by comparing all possible way of cutting the rod.

## DP (Idea : First have the maximum possible price by selling the left end of the rod and then tryy to find the optimal way to cut the remaining rod)

## DP Algorithm 
CUT_ROD(p,n) <- p referes to the array of price for length i. n the length of the given rod. length of p is n.
{
    R[0 ... n] = [0]
    R[0] = 0
    for i <- 1 to n
    {
        q = -inf
        for j <- 1 to i
        {
            q = max(q,p[i]+r[j-i]) <- check from the previous configuration which is best.
        }
        r[i] = q <- -inf would be replace by the first one
    }
    return r[n]
}

