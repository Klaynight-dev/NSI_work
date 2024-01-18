def delta(lst):
    if len(lst) == 1:
        return lst
    else:
        result = [lst[0]]
        for i in range(1, len(lst)):
            result.append(lst[i] - lst[i-1])
        return result

     
print(delta([1000,800,802,1000,1003]))
print(delta([42]))
