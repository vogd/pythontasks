
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#Return even numbers
b=[x for x in a if x%2==0]
print b

#Sort By even numbers
y=sorted(a, key=lambda v: (v%2==0, v))
print y

#Return Odd numbers
odd=[n for n in a if n%2 !=0]
print odd
