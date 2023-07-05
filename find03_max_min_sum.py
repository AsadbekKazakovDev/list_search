def find_max_min_sum(data):
    """
    Given the list of numbers, return the sum of the maximum and minimum numbers in the list
    args:
        data: list of numbers
    returns: sum of the maximum and minimum numbers in the list
    """
    i=0
    j=0
    ans = data[0]
    while i<=len(data)-1:
        if ans<data[i]:
            ans = data[i]
            
        i+=1
    lst=data[0]
    while j<=len(data)-1:
        if lst>data[j]:
            lst=data[j]
        j+=1
    return lst+ans
data = [1,8,3,8,5,8,7,8]
print(find_max_min_sum(data))
