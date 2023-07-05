def find_max_count(data):
    """
    Given the list of numbers, Find count of maximum numbers in the list
    args:
        data: list of numbers
    returns: count of maximum numbers in the list
    """
    i=0
    anss=[]
    ans = data[0]
    while i<=len(data)-1:
        if ans<data[i]:
            ans = data[i]
            
        i+=1
    k = data.count(ans)
            
    return k
data = [1,8,3,8,5,8,7,8]
print(find_max_count(data))
