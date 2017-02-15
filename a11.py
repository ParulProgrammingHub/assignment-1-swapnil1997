print ("enter the principle amount")
p = input()
print ("enter the rate of interest")
r = input()
print ("No of times the interest is compounded")
t = input()
print ("NO of years")
n = input();
def interest(p,r,t,n):
    i = p*(pow((1+(r/n)),(n*t)))
    return i
i = interest(p,r,t,n)
print ("Interest is....")
print (i)
