def check(string):
    b = set(string)
    s = {'0', '1'}
    if s == b or b == {'0'} or b == {'1'}:
        print("Binary String")
    else:
        print("Non Binary String")


s1 = "00110101"
# function calling
check(s1)
s2 = "1010100200111"
check(s2)