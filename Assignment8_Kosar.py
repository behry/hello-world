#Exercise_1
sayi = int(input('Enter a number: '))
for a in range(1,11):
    print(sayi, 'x', a, '=',sayi*a)
print('\n')

#Exercise_2
list_1 = []
list_2 = []
for b in range(1,21):
    if b%2!=0:
        list_1.append(b**2)
    else:
        list_2.append(b**3)
print(list_1)
print(list_2)
print('\n')

#Exercise_3
word = input('Enter a word: ')
x = len(word)
while x>=1:
    print(word[x-1],end=" ")
    x-=1
print('\n')

#Exercise_4
even_numbers = []
odd_numbers = []

for n in range(1,201):
    if n % 2 == 0:
        even_numbers.append(n)

    else:
        odd_numbers.append(n)

print("Even numbers: ", even_numbers)
print("Odd numbers : ", odd_numbers)
print('\n')

#Exercise_5
sequence=[]
d=0
r=0
while True:
    key = input('Enter sequence number (Enter x to finish sequence) : ')
    if key == 'x':
        break
    sequence.append(key)
    d+=1

item = input ('Choose one number from your inputs: ')
for count in range(d-1):
    if item == sequence[count]:
        r+=1
print(r)
print('\n')

#Exercise_6
en = input('Enter an integer: ')
toplam = 0
for num in en:
    toplam= toplam + int(num)

while True:
    if toplam <=9: break
    en=str(toplam)
    toplam = 0
    for num in en:
        toplam = toplam + int(num)

print(toplam)
print('\n')

#Exercise_7
div1 = []
div2 = []

sayi1 = int(input('Enter first number: '))
sayi2 = int(input('Enter second number: '))

for d1 in range(1, sayi1 + 1):
    if sayi1 % d1 == 0: div1.append(d1)

for d2 in range(1, sayi2 + 1):
    if sayi2 % d2 == 0: div2.append(d2)
div1.sort()
div2.sort()

if len(div1) >= len(div2):
    gcd = 0

    for x in range(len(div1) - 1):
        a = 0
        while a != len(div2):
            if div2[a] == div1[x]:
                gcd = div2[a]
            a = a + 1

print(gcd)
print('\n')

#Exercise_8
print('******************')
for x in range(1,51):
  if x%15==0:print('fizzbuzz')
  elif x%5==0:print('buzz')
  elif x%3==0:print('fizz')
  else:print (x)
print('\n')

#Exercise_9
a = 0
b = 1
fib = [0, 1]
for x in range(1, 49):
    x = a + b
    fib.append(x)
    a = b
    b = x
print(len(fib))
print(fib)










