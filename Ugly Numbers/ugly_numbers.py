import time


def is_ugly(n : int) -> bool:
    if (n==1) :
        return True
    if(n==0) :
        return False
    for factor in [2,3,5]:
        if(n%factor == 0):
            return is_ugly(n/factor)
    return False

def get_ugly(n:int) -> int:
    if((n in [0,1]) or (n < 0)):
        return n
    count = 1
    current = 2
    while(True):
        if(is_ugly(current)):
            count += 1
            if(count == n):
                return current
        current += 1
    return 0

def get_ugly_dynamic(n:int) -> int:
    ugly = [0]*n
    if((n in [0,1]) or (n < 0)):
        return n
    ugly[1] = 2
    i2=i3=i5=0
    next_ugly = 1
    next_multiple_2 = 2
    next_multiple_3 = 3
    next_multiple_5 = 5
    for i in range(1,n):
        next_ugly = min(next_multiple_2,next_multiple_3,next_multiple_5)
        ugly[i] = next_ugly
        if(next_ugly == next_multiple_2):
            i2 = i2+1
            next_multiple_2 = ugly[i2]*2
        if(next_ugly == next_multiple_3):
            i3 = i3+1
            next_multiple_3 = ugly[i3]*3
        if(next_ugly == next_multiple_5):
            i5 = i5+1
            next_multiple_5 = ugly[i5]*5
        #print(i,":",next_ugly,":",next_multiple_2,next_multiple_3,next_multiple_5)
    return next_ugly

def get_int_user():
    while(True):
        try:
            n = int(input("Enter an ugly number: "))
            print("The entered number is:", n)
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue
    return n

if __name__ == "__main__":
    
    n = get_int_user()
    st = time.process_time()
    ugly_required = get_ugly(n)
    et = time.process_time()
    print(n,"Ugly number:",ugly_required, "\n\tTime Taken",et-st)
    st = time.process_time()
    ugly_required = get_ugly_dynamic(n)
    et = time.process_time()
    print(n,"Ugly number:",ugly_required, "\n\tTime Taken",et-st)

