

def is_ugly(n : int) -> bool:
    if (n==1) :
        return True
    if(n==0) :
        return False
    for factor in [2,3,5]:
        if(n%factor == 0):
            return is_ugly(n/factor)
    return False




if __name__ == "__main__":
    for num in range(0,200):
        if(is_ugly(num)):
            print(num,end=",")
    print()