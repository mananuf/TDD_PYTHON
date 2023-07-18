# userInput = int(input('enter jupyter command: '))

# while userInput % 2 == 0:
#     print(userInput, 'is  not an odd number')

#     userInput = int(input('enter jupyter command: '))

while True:
    userInput = int(input('enter jupyter command: '))

    if userInput % 2 == 0:
        print(userInput, 'is not an odd number')
    else:
        print(userInput, 'is an odd number')
        break









# userInput = input('enter command:').upper()

# while userInput != 'QUIT':
#     if userInput == "START":
#         print('starting engine...')
#         print('engine has started')       
#     elif userInput == "STOP":
#         print('stopping engine...')
#         print('engine has stopped')
#     else:
#         print('wrong input')

#     userInput = input('enter command:').upper()