def find_max_index(data):
    
    """
    Given the list of numbers, return the index of maximum number in the list
    args:
        data: list of numbers
    returns: index of maximum number in the list
    """
    i=0
    j=0
    ans = data[0]
    while i<=len(data)-1:
        if ans<data[i]:
            ans = data[i]
            
        i+=1
    g = 0
    while j<=len(data)-1:
        if data[j]==ans:
            g=j
        j+=1
    return g
data = [1,2,3,49,5,8,3]
print(find_max_index(data))
