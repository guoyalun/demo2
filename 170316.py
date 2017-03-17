#1. 求100以内的偶数和  两种写法 2550.

#1.1

def sum(a):
    if a > 2:
        return sum(a - 2) + a
    else:
        return a 
print(sum(100))


#1.2
a = 0
for i in range(1,101):
	if i % 2 == 0:
		a += i
print (a)

#1.3
def main(arg):
	if arg > 0:
		if arg % 2 == 0:
			print(arg)
			return main(arg - 1) + arg
		else:
			return main (arg - 1)
	else:
		return 0
res = main(100)
print(res)



#2.1. 求100以内的质数和  两种写法
#质数的定义:只能被1和自己整除的正整数

#2.1

l = []
for n in range(2,101):
    if n == 2:
        l.append(2)
    else:
        if 0 not in [n % i for i in range(2,n)]:
            l.append(n)
print(sum(l))


#2.2

l = []
for a in range(2,100):
    b = 0
    for c in range(2,(a//2)+1):
        if a % c == 0:
            b = 1
    if b == 0:
    	l.append(a)
print(sum(l))


