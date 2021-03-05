first="hello"
print(first)

second=45
print(second)

third=90.4
print(third)
print(int(third))
print("A %s %s %s %s " % ("string","filled","by a","tuple"))
 
a=("first", "second", "third")
print("the first element is ", a[0])
print("the second element is ", a[1])
print("%d" % len(a))
print(a[len(a)-1])
b=(a,"b,s second element")
print(b[1])
print(b[0][0])
layer2=b[0]
print(layer2[0])
