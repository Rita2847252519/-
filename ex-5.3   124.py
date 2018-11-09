def isNum(s):
    try:
        n=eval(s)
        return True 
    except:
        return False
while 1:  
    print(isNum(input("请输入一个字符串:")))

