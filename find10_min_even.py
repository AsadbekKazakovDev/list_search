def find_min_even(data):
    """
    Given the list of numbers, Find the minimum even number in the list
    args:
        data: list of numbers
    returns: minimum even number in the list
    """
    j = 0
    ans=[]
    while j<=len(data)-1:
        if data[j]%2==0:
            ans.append(data[j])
        j+=1
            
    i=0
    mn = ans[0]
    while i<=len(ans)-1:
        if mn>ans[i]:
            mn = ans[i]  
        i+=1
    return mn
data = [29,-9,4,5,6,7,8,9]
print(find_min_even(data))

