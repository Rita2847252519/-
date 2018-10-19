import math
dayup,dayfactor=1.0,0.01
for i in range(365):
    if i % 7 in [4,0]:
        dayup=dayup*(1+dayfactor)
    else:
        dayup=dayup
print("连续学习365天的能力值:{:.2f}.".format(dayup))
