#encoding=utf-8
def main(arg):
    if arg > 0:
        if arg % 2 ==0:
            print(arg)
            return main(arg - 1) + arg
        else:
            return main(arg - 1)
    else:
        return 0;


if __name__ == '__main__':
    res = main(100)
    print("sum is ",res)
