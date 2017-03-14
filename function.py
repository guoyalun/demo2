#encoding=utf8
# y = f(x)
#
# x = 1  y = 2
# x = 2  y = 5
#
# f(x) = x*x + 1
#
# f(6) = 37

# def mutiply(arg):  #形参
#     return (arg,arg * arg)
#
# result = mutiply(100)
# print(result)
# print(mutiply(1000))#实参
#
# print(mutiply(1000*1000))
#
# print(mutiply(5 ＊ 24 ＊ 3600 ＊ 1000))
def mutiply1(arg):
    for i in range(1,arg):
        for j in range(1,i+1):
            pass
            # print("%d * %d = %d"%(i,j,i*j),end="\t")
        # print("\t")

def plus(arg0,arg1=10,arg2=0):
    return arg0 + arg1 * arg2

def bbbb(arg0,arg1=10,arg2=0):
    return plus(arg0,arg1,arg2) + plus(arg0,arg1,arg2)

def sum(arg):
    sum = 0
    count = 0
    for i in range(1,arg+1):
        sum += i # sum = sum + i    sum /= i  sum++  = sum = sum + 1
        count += 1
    return (count,sum)



print(sum(9))


def testabs(arg0):
    if arg0 < 0:
        return arg0 * -1
    else:
        return arg0


# bbbb = plus
print(bbbb(1,2,3))
print(plus(1,2,3))


print(abs(-1000))

print(plus(1,2,3))
print(plus(1,2))
print(abs(plus(-10)))


# 1-arg 的求和
def aaaaa(arg):
    if arg > 1:
        return aaaaa(arg - 1) + arg
    else:
        return arg

print(aaaaa(9))

#使用循环的方式查找字母a
def checkA(str):
    count = 0
    for i in str:
        if i == "a":
            count += 1
    return count

#使用循环的方式查找字母b
def checkB(str):
    if len(str) == 0:
        return 0
    prefix = str[0:1]
    if prefix == "b":
        return checkB(str[1:]) + 1
    return checkB(str[1:]) + 0


bbbb = checkA("agsjjaaadjdjdj")
print("checkA is :",bbbb)

bbbb = checkB("babgsbjjaaadbjdjdjbbbbb")
print("checkB is : ",bbbb)


# mutiply1(9)
# mutiply1(8)
