# Exercise_1
my_list = [34, 56, 76, 45, 2, 12, 67, 98, 37, 54, 66]
my_list.sort ()
result_1 = my_list [0] + my_list [1]
print(result_1, "\n")
my_list.sort(reverse=True)
result_2 = my_list[0] + my_list[1]
print(result_2, '\n')

#Exercise_2
names = ["David", "Michael", "John", "James", "Greg", "Mark", "William", "Richard", "Thomas", "Steven",
         "Mary", "Susan", "Maria", "Karen", "Lisa", "Linda", "Donna", "Patricia", "Debra", "Eric"]
scores = [99, 87, 78, 86, 68, 94, 76, 97, 56, 98, 76, 87, 79, 90, 73, 93, 82, 69, 97, 98]

student = input("Enter a student name: " )
index_1 = names.index(student)
print("The score of " + student + " is: ", scores[index_1], '\n')

#Exercise_3
scores_1 = scores.copy()
scores_1.sort(reverse=True)
print ("Maximum score is: ", scores_1[0])
print("The number of students with the highest score:", scores_1.count(scores_1[0]), '\n')

#Exercise_4 (Not understood)
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
             'October', 'November', 'December']
day_counts = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
print(months, day_counts)

#Exercise_5 (Not understood)
Spring = [months[2], months[3], months[4]]
Summer = [months[5], months[6], months[7]]
Fall = [months[8], months[9], months[10]]
Winter = [months[11], months[0], months[1]]

print(Spring, Summer, Fall, Winter, '\n')

#Exercise_6 (Not understood)
Summer_days = day_counts[5] + day_counts[6] + day_counts[7]
print('There are {} days in Summer'.format(Summer_days))





