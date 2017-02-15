print ("enter the principle amount")
p = input()
print ("enter the rate of interest")
r = input()
print ("enter the period of time")
n = input()
def interest(p,r,n):
    i=(p*r*n)/100
    return i
i = interest(p,r,n)
print ("Interest is")
print (i)
