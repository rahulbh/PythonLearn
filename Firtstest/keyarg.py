def get_sum1(i,*arg):
    sum1=i
    for item in arg:
        sum1+=item
    return sum1

print(get_sum1(1,12,3))
