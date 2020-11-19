#Exercise_1
def divident(num1,num2):
    try:
        rslt= int(num1)/ int(num2)
        print (rslt)
    except:
        print ('Denominator can not be zero')
divident(4,0)

#Exercise_2
def divident1(num1,num2):
    try:
        rslt1= int(num1)/ int(num2)
        print (rslt5)
    except NameError:
        print ('Name is not defined')
divident1(4,2)
#Exercise_3

def divident2(num1,num2):
    try:
        rslt2= int(num1)/ int(num2)
        print (rslt2)
    except ValueError:
        print ('Wrong Data Type')
divident2(14,'a')
