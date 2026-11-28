limit=99
cut=[]
primes=[]
digit=[]

print("Quiz code maker\n")

for i in range(2, limit+1):
    for l in range(2, limit+1):
        cut.append(i*l)

for i in range(2, limit+1):
    if i not in cut:
        primes.append(i)

for i in primes:
    if len(str(i))==2:
        digit.append(i)

print(digit)