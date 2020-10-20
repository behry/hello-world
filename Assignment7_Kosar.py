#Exercise_1
convers = int(input("Which conversion would you like? 1- Celcius to Fahrenheit / 2- Fahrenheit to Celcius"))
if convers == 1:
    C = float(input("Enter the temperature in Celcius: "))
    F = C / (5/9) + 32
    print(C," Celcius is equal to {:.2f} F". format(F))
elif convers == 2:
    F = float(input("Enter the temperature in Fahrenheit: "))
    C = (5/9)*(F-32)
    print(F," Fahrenheit is equal to {:.2f} C". format(C))
else :
    print ("Invalid input")

#Exercise_2
salary = float(input("Please enter your salary: "))
service = int(input("Please enter your year of service: "))
if service > 5 :
    bonus = salary * 0.05
    print("Your net bonus is: ", bonus)
else:
    print("You don't get any bonus")

#Exercise_3
a = int(input("Enter the age of Ahmet: "))
b = int(input("Enter the age of Bekir: "))
c = int(input("Enter the age of Celal: "))
if a>b and a>c :
    if b>c:
        print ("Oldest is Ahmet ")
        print ("Youngest is Celal")
    else:
        print("Oldest is Ahmet ")
        print("Youngest is Bekir")

elif a>b and c>a:
    print("Oldest is Celal")
    print("Youngest is Ahmet")

elif b>a and b>c :
    if a > c:
        print("Oldest is Bekir ")
        print("Youngest is Celal")
    else :
        print("Oldest is Bekir ")
        print("Youngest is Ahmet")

elif b>a and c>b:
    print("Oldest is Celal")
    print("Youngest is Ahmet")

else:
    print('One or more of the ages are equal')

#Exercise_4

num_class = int(input( "How many classes were held? :"))
num_att = int(input("How many classes were attended? :"))
check = (num_att/num_class)*100
print ("The percentage of the classes attended : % {:.1f}".format(check))
if check>=75:
    print ("The student is allowed to enter the exam")
else:
    print ("The student is NOT allowed to enter the exam")

#Exercise_5

test = input ("Enter a letter from the alphabet : ")

if test == 'a' or test == 'e' or test == 'i' or test == 'o' or test == 'u':
    print ('Your letter is a vowel')
elif test == 'y':
    print ('Y is sometimes a vowel and sometimes a consonant')
else:
    print ('Your letter is consonant')