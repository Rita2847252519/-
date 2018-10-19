import time
scale=3
t=time.clock()
for i in range(scale+1):
    a='.'*i
    b='*'*(scale-i)
    t-=time.clock()
    print("\rStarting{}{}Down!".format(a,b,-t),\
          end='')
    time.sleep(0.1)
