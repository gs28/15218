low = int(input("Enter lower range: "))  
up = int(input("Enter upper range: "))
for num in range(lower,upper + 1):
  s = 0
  temp = num
  while temp > 0:
    digit = temp % 10
    s += digit ** 3
    temp //= 10
  if num == s:
    print(num)
