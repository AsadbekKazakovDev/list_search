def find_min_count(data):
    """
    Given the list of numbers, Find count of minimum numbers in the list
    args:
        data: list of numbers
    returns: count of minimum numbers in the list
    """
    i=0
    ans = data[0]
    while i<=len(data)-1:
        
        if ans>data[i]:
            ans = data[i]
        i+=1
    j = 0
    k = 0
    while j<=len(data)-1:
        if data[j]==ans:
            k+=1
        j+=1
        
    return k
data =  [0, -4, 3, 9, -2, -4]
print(find_min_count(data))
