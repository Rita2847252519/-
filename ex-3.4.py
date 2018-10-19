NumStr=input("")
a=NumStr[0:5]
b=NumStr[::-1]
if a==b:
    print("{}是回文数".format(NumStr))
else:
    print("{}不是回文数".format(NumStr))
