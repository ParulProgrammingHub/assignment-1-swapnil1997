print ("Enter the first angle")
a = input()
print ("Enter the second angle")
b = input()
def thirdangle(a,b):
    c = 180 - a - b
    return c
c = thirdangle(a,b)
print("The third angle is ")
print (c)
