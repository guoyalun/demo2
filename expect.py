# div = 0
# div1 = 1
# div2 = 0

def main():
    input = "a"

    try:
        print('try...')
        r = 10 / int(input)
        print('result:', r)
    except ValueError as e:
        print('ValueError:', e)
        print("请输入数字")
    except ZeroDivisionError as e:
        print('ZeroDivisionError:', e)
        print("不能输入0")
    else:
        print('no error!')
    finally:
        print('finally...')

    print('END')

if __name__ == '__main__':
    main()


# print('try...')
# r = 10 / div
# print('result:', r)
#
#

# try:
#     print('try...')
#     r = div2 * 10 /div/div1/div2
#     print('result:', r)
# except Exception as e:
#     print("1234567")
#     print(e)
# finally:
#     print("4678")
#
# print("11123245")
# print("11123245ssdafgh")
# print("11123245")
# print("11123245ssdafgh")
# print("11123245")
# print("11123245ssdafgh")
# print("11123245")
# print("11123245ssdafgh")
