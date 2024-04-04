def fibo(num):
    if num==1:
        return 1
    elif num==2:
        return 1
    elif num in cache:
        return cache[num]
    else:
        num_def=fibo(num-1)+fibo(num-2)
        cache[num]=num_def
        return num_def
cache={}
print(cache)
print(fibo(10))
print(cache)