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

def login():

    # This function checks if the entered profile has a match in the 'profiles.csv' file 
    def authenticate(user,key):
        with open('profiles.csv', 'r') as file:
            reader = csv.dictReader(file)
            for row in reader:
                if row['User'] == user:
                    if row['Key'] == key:
                        checkpoint = int(row['Checkpoint'])
                        print('--- Login successful ---')
                        return [True,checkpoint]
                else:
                    return [False,'X']
    # Profile details entry and authentication       
    tries = 0
    while tries < 3:

        # Taking profile details (username and key)
        user = input('Username: ')
        key = input('Enter your 4-digit key: ')
        
        # Profile authentication
        logged,checkpoint = authenticate(user,key)
        if logged == True:
            print(f'Welcome back {user}')
            break
        else:
            print('Wrong username or password')
            tries += 1
    print('Too many wrong entries')

class play_game:
    def __init__(self,user='Guest',checkpoint='0'):
        self.user = user
        self.checkpoint = checkpoint

    def load_data(self):
        pass

def main_menu():
    print('''
                RISE OF AN EMPIRE  -  STORY GAME
                    [1] Log into profile
                    [2] Create new profile
                    [3] Play as guest
                    [4] Exit
             ''')
        option = int(input('Option >>  '))
        while True:
            try:
                if option == 1: # Old profile login
                    logged,checkpoint = login()
                    if logged == True:
                        user = play_game(user,checkpoint)
                        user.load_data()
                elif option == 2: # New profile login
                    
                elif option == 3: # Guest login
                    user = play_game()
                    user.load_data()
                elif option == 4: # Exit
                    break
                else: # Any other integer entry
                    print('Options can be 1,2,3,or 4 only')
            except Exception as e: # Exception handling
                print('An error occured: ', e)
