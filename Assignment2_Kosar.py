#Exercise 1#
capital = 1000
daily_growth = 0.12
period = 7
final_growth_rate = daily_growth * period
result = capital + (capital * final_growth_rate)
print("$" + str(result),"\n") 

#Exercise 2#
print("`\"When we buy bitcoin with {} USD at the beginning of the week, \
we would earn {} USD at the end of the week, with an average gain of {}%.\"` \n".format (1000,1210.68,12))

#Exercise 3#
temp = input("Enter the temperature in Fahrenheit:")
result = (5/9)*(float(temp)-32)
print("Temperature (C) : {:.2f} \n". format (result))

#Exercise 4#
number = input("Enter a three digit number:")
result = int(number[0])+int(number[1])+int(number[2])
print("\"The sum of the digits in the number is " + str(result) + '"\n' )

#Exercise 5#
side_1 = input("first side lenght: ")
side_2 = input("second side lenght: ")
hypo = (int(side_1)**2+int(side_2)**2)**0.5
print("\"The lenght of the hypotenuse is {:.0f}\" ".format(hypo))