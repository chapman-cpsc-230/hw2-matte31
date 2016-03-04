b_str = raw_input("enter a floating point number: ")
b = float(b_str)

while b == 1.0:
    b_str = raw_input("Nah dude can't do 1.0")
    b = float(b_str)

n_str = raw_input("enter a natural number: ")
n = int(n_str)

val = 0
i = 0
while i <= n:
    val += b**i
    i += 1

print val
print (b**(n + 1)- 1)/(b - 1)
