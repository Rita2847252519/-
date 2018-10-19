import math
n=input("请输入时间n年:")
for i in range (int(n)):
    a=0.5*i
    earth=math.fsum([50,a])
    b=math.fsum([50,a])
    moon=0.165*b
print("地球体重:{:.2f}kg,月球体重:{:.2f}kg.".format(earth,moon))
