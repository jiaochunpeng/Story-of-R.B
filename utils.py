import json

def waitforkeys(key='space'):
    while True:
        user_input=input()
        match key:
            case 'space': break
            