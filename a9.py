print ("enter no of subjects")
n = input()
print  ("enter the total marks of every subject")
x = input()
print ("Enter the marks of each subject")
a=input()
b=input()
c=input()
y=(a+b+c)
f=y/n
print ("Mean of the marks is")
print(f)
g = (100*y)/(x*n)
print ("Percentage is ...")
print (g)
if (g<35):
    print ("FAIL!!!!!")
else:
    print("PASS")
