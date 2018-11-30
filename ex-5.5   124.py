def isPrime(n):
    for k in range(2,n):
        if n%k==0:
            return False
        return True
def main():
    while True:
        try:
            n=int(input("请输入一个整数"))
        except:
            print("输入错误")
            break

        if isPrime(n):
            print("n不是质数")
        else:
            print("n是质数")
main()
                  
