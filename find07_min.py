def find_min(data):
    """
    Given the list of numbers, return the minimum number in the list
    args:
        data: list of numbers
    returns: minimum number in the list
    """

    i=0
    lst = []
    ans = data[0]
    while i<=len(data)-1:
        if ans>data[i]:
            ans = data[i]  
        i+=1
    return ans
data = [2,-9,4,5,6,7,8,9]
print(find_min(data))