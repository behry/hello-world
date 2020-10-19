#Exercise_1
weekdays = {
            '1': 'Monday',
            '2': 'Tuesday' ,
            '3': 'Wednesday',
            '4' : 'Thursday' ,
            '5' :  'Friday' ,
            '6' : 'Saturday',
             '7' : 'Sunday'
}
day1 = input("Choose the number of the first day (Between 1-7):")
day2 = input("Choose the number of the second day (Between 1-7):")
del weekdays[day1]
del weekdays[day2]
print(weekdays)

#Exercise_2
list_1 = {
    'John':{
        'Age':'25','Gender':'Male'},
    'Lisa':{
        'Age':'28','Gender':'Female'},
    'Linda':{
        'Age':'28','Gender':'Female'},
    'Michael':{
        'Age':'41','Gender':'Male'}
}

#Exercise_3
list_1 = {
    'John':{
        'Age':'25','Gender':'Male'},
    'Lisa':{
        'Age':'28','Gender':'Female'},
    'Linda':{
        'Age':'28','Gender':'Female',
        'child':{
            'Susan':{
                'Age':'6','Gender':'Female'}
            }
        },
    'Michael':{
        'Age':'41','Gender':'Male',
        'child':{
            'Karen':{
                'Age':'12', 'Sex': 'Female'},
            'Greg':{
                'Age':'7', 'Sex':'Male'}
            }
            }
}
#Exercise_4
print('Michael\'s children are: ', list_1['Michael']['child'])