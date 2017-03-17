#encoding=utf-8

def prime_sum(arg):
    if arg < 2:
        return 0;
    if is_prime(arg) == True:
        print(arg)
        return  prime_sum(arg -1) + arg
    else:
        return  prime_sum(arg -1)


def composite_sum(arg):
    if arg < 1:
        return 0;
    if is_prime(arg) == False:  #是否为素数
        return composite_sum(arg -1) + arg
    else:
        return composite_sum(arg - 1)

#是否为素数
def is_prime(arg):
    for i in range(2,arg):
        if arg % i == 0:
            return False
    return True


print("sum is ",prime_sum(100))
print("sum is ",composite_sum(100))
