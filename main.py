# Remember to perform read-write operations in real-time
# STORY GAME
import csv
def new_user():
        print('NEW USER PROFILE')
        check_point = 0
        while True:
            user = input('Username: ')
            key = input('Enter a 4-digit pin: ')
            try:
                with open('profiles.csv', 'a+') as file:
                    reader = csv.dictReader(file)
                    writer = dictWriter(file)
                    for row in reader:
                        if row['User'] == user:
                            if row['Key'] == key:
                                print('This profile already exits')
                            else:
                                # writer.append([user,key,checkpoint])  Check for right syntax
                                print('Account successfully created')
                                break    
            except Exception as e:
                print('An error occured: ', e)
