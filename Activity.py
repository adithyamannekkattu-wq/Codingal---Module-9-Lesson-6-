'''num=int(input("Enter a number: "))

result="The number is prime."
for i in range(2, num):
    if num%i==0:
        result="The number is not prime"
        if i*i>num:
            break

print(result)'''

cut=[]
primes=[]
palindromes=[]

limit=int(input("Enter an upper limit: "))

for i in range(2, limit+1):
    for l in range(2, limit+1):
        cut.append(i*l)

for j in range(2, limit+1):
    if j not in cut:
        primes.append(j)


for i in primes:
    v=str(i)
    if v==v[::-1]:
        palindromes.append(i)

print(primes)
print(palindromes)
