def find_max_even(data):
    """
    Given the list of numbers, Find the maximum even number in the list
    args:
        data: list of numbers
    returns: maximum even number in the list
    """
    i=0
    lst = []
    y=0
    while y<=len(data)-1:
        if data[y]%2==0:
            lst.append(data[y])
        y+=1
    ans = lst[0]
    while i<=len(lst)-1:
        if ans<lst[i]:
            ans = lst[i]  
        i+=1
    return ans
data = [1,2,3,4,5,6,7,8,9]
print(find_max_even(data))

