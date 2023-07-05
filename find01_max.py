def find_max(data):
    """
    Given the list of numbers, return the maximum number in the list
    args:
        data: list of numbers
    returns: maximum number in the list
    """
    i=0
    ans = data[0]
    while i<=len(data)-1:
        if ans<data[i]:
            ans = data[i]
        i+=1
    return ans
data = [1,2,3,49,5,6,7,8]
print(find_max(data))
    