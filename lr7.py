# 1
a = int(input())
if a % 2 == 0:
    print("Chislo chetnoe")
else:
    print("Chislo ne chetnoe")

# 2
a = int(input())
b = int(input())
c = int(input())
if a > b and a > c:
    print(a, "samoe bolshoe")
if b > a and b > c:
    print(b, "samoe bolshoe")
if c > a and c > b:
    print(c, "samoe bolshoe")

# 3
a = int(input())
f = 1
for i in range(1, a+1):
    f = f * i
print(f)

# 4
a = int(input())
for i in range(2, a):
    if a % i == 0:
        print("Chislo ne prostoe")
        break
else:
    print("Chislo prostoe")

# 5
a = int(input())
for i in range(1, 11):
    print(a, "*", i, "=", a * i)

# 6
a = input()
a = a.lower()
a = a.replace(" ", "")
a = a.replace(",", "")
a = a.replace(".", "")
if a == a[::-1]:
    print("this polindrom")
else:
    print("this not polindrom")

# 7
a = input()
g = "ауоиэыяюеё"
s = "бвгджзйклмнпрстфхцчшщьъ"
count_g = 0
count_s = 0
for i in a:
    if i in g:
        count_g = count_g + 1
    else:
        count_s += 1
print("Kolichestvo glasnih:", count_g)
print("Kolichestvo soglasnyh:", count_s)

# 8
a = [34, 67, 74, 28, 12]
summa = 0
for i in a:
    summa = summa + i 
print(summa)

# 9
a = int(input())
for i in range(a):
    print(a-i)
    
# 10
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
    