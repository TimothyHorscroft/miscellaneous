import math

phi = float(input("phi: "))
eps = float(input("eps: "))

a = eps
b = 1 - eps

print("+ve CONJECTURE:", phi**(1-eps)-phi**eps+phi-phi**(2*eps))
print("-ve CONJECTURE:", -(phi**(1-eps)-phi**eps+phi**(1-2*eps)-1))

print("start:", a, b)

count = 0
while a > 1-2*eps and b < 2*eps:
    count += 1
    c = math.log(phi**eps+1-phi**(b-eps))/math.log(phi)
    #print("new a:", phi**c, phi**b, "change:", phi**c-phi**a)
    a = c
    if not (a > 1-2*eps and b < 2*eps):
        break
    count += 1
    d = math.log(phi**(1-eps)+phi-phi**(a+eps))/math.log(phi)
    #print("new b:", phi**a, phi**d, "change:", phi**d-phi**b)
    b = d

if b >= 2*eps:
    print("b exceeded")

if a <= 1-2*eps:
    print("a exceeded")

print(count)
