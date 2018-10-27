s=input("请输入一行字符:")
zm,sz,kong,qt=0,0,0,0
for c in s:
    if 'a'<=c<='z' or 'A'<=c<='Z':
        zm=zm+1
    elif '1'<=c<='9':
        sz=sz+1
    elif c==' ':
        kong=kong+1
    else:
        qt=qt+1
    print("中英文的个数为:'{}',数字的个数为:'{}',空格的个数为:'{}',其他字符的个数为:'{}'.".format(zm,sz,kong,qt))
            
