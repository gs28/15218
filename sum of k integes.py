s= list()
K=2
N = input("Enter the number of elements:")
print ('Enter numbers in array: ')
for i in range(int(N)):
    n = input("number :")
    s.append(int(n))
print ('ARRAY: ',s)
print (sum(s[0:K]))
