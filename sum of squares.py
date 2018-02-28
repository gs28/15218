def sum_of_squares(n):
    return sum(int(c) ** 2 for c in str(n))
print (sum_of_squares(123))
