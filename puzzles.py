#1,0,X
import random
import faker 


def game_passcode():
    random_passcode = faker.Faker().word()
    while True:
        response=''
        user_input=input()
        if user_input==random_passcode: 
            return True
        for i in range(0, len(user_input)):
            if user_input[i] not in random_passcode:
                response+='0'
            elif i<len(random_passcode) and user_input[i]==random_passcode[i]:
                response+='x'
            else: 
                response+='1'
        print(response)

def game_guessnumber():
    random_number = random.randint(1,1000)
    while True:
        response=''
        user_input=input()
        if user_input.isdigit():
            if int(user_input)==random_number: 
                return True
            elif int(user_input)> 1000:
                response='X'
            elif int(user_input)>random_number: 
                response='1'
            else: 
                response='0'
        else: response='X'
        print(response)
