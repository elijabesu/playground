###1
# code = 1 + 2 + 3 + 4 + … + 38 + 39 + 40
code = 0
for i in range(1, 41):
    code += i
print("#1:", code)

###2
# code = Total number of 3-digit combinations where digit1 < digit2 < digit3
code = 0
for i in range(0, 10):
    for j in range(0, 10):
        for k in range(0, 10):
            if i < j < k:
                code += 1
print("#2:", code)

###3
# code = Total number of 3-digit combinations where digit1, digit2 and digit3 are all even numbers
code = 0
for i in range(0, 10):
    if i % 2 == 0:
        for j in range(0, 10):
            if j % 2 == 0:
                for k in range(0, 10):
                    if k % 2 == 0:
                        code += 1
print("#3:", code)

###4
# code = Total number of 3-digit combinations where the sum of all three digits (digit1 + digit2 + digit3) is an odd number
code = 0
for i in range(0, 10):
    for j in range(0, 10):
        for k in range(0, 10):
            s = i + j + k
            if s % 2 == 0:
                code += 1
print("#4:", code)

###5
# code = Total number of 3-digit combinations where at least two digits are equal.
code = 0
for i in range(0, 10):
    for j in range(0, 10):
        for k in range(0, 10):
            if i == j or j == k or k == i:
                code += 1
print("#5:", code)

###6
# code = Total number of 3-digit combinations where one digit is equal to the sum of the other two digits.
code = 0
for i in range(0, 10):
    for j in range(0, 10):
        for k in range(0, 10):
            if (i == j + k) or (j == k + i) or (k == i + j):
                code += 1
print("#6:", code)

###7
# code = The largest 3-digit square number.
code = 0
for i in range(10, 100):
    i2 = i**2
    if code < i2 and i2 < 1000:
        code = i2
print("#7:", code)

###8
# code = The largest 3-digit prime number.
code = 0
for i in range(100, 1000):
    for j in range(2, 10):
        if i % j == 0:
            yes = 0
            break
        yes = 1
    code = i if code < i and yes == 1 else code
print("#8:", code)

###9
# code = The average of all prime numbers between 0 and 999 (rounded to the nearest value).
code = 0
total = 0
for i in range(2, 1000):
    yes = 1
    for j in range(2, i):
        if i % j == 0:
            yes = 0
    if yes == 1:
        code += i 
        total += 1
code = code / total
print("#9:", round(code))