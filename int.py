# -*- coding: utf-8 -*-

#类型转换
birth = int("1982")
# birth = str(1982)

print(2017 - int("1982"))

print(str(2017) + "1982")


if birth < 2000:
    print('00前')
else:
    print('00后')


"[]您的验证码是:4432,请注意保密"

code = "4432"
a = "[]您的验证码是:" + code + ",请注意保密"
send("18601140270",a)

code = "4432"
a = "[]您的验证码是:" + code + ",请注意保密"
print("[]"+mobile+"您的验证码是:" + code + ",请注意保密,第"+str(n)+"次收到"+str(1000.0))

mobile = "19701001011"
n = 100
print("[]%s您的验证码是:%s,请注意保密,第%d次收到,您的收益%f" %(mobile,code,n,1001.00))
