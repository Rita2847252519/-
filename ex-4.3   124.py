m,n=eval(input("请输入两个整数:"))
a,b=m,n
r=m%n
while r!=0:
     m,n=n,r
     r=m%n
    
print('{}和{}最大公约数是：{}， 最小公倍数是：{}'.format(a, b,n , a * b / n))


