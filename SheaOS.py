#An attempt to make a personalized "operating system" for me and my friends
#Why? I dont know. Boredom, maybe. Perhaps its a personal challenge.
#Also definitely not an OS. Flashy titles and all.

#imports
import os
import time

#assigning all programs as off
program1 = 0
program2 = 0

#opens initial welcome and input
startLoop = 1
while startLoop == 1:
    print('Welcome to SheaOS.')
    print("Type 'menu' to open a list of features.")
    print("Type 'help' for help.")
    start = input()

    if start == 'menu':
        
        print('Please enter the number of the program you would like to run.')

        print('[1] Rhyming')
        print('[2] ')

        menu = int(input())

        if menu == 1:
            startLoop = 0
            program1 = 1
        elif menu == 2:
            startLoop = 0
            program2 = 1

    elif start == 'help':
        print('SheaOS runs on a system of input commands.')
        print('None of them are intuitive.')
        print("That's my special touch.\n")
        print("Inputs that work on the initial screen are 'credits', 'menu',")
        print("'exit', and, of course, 'help'.")
        print("If any program asks a question, respond with 'yes' or 'no'.\n")
        print('There are also a number of special inputs.')
        print("I might tell you some of them, but there's a bunch of secret ones.\n")
        helpmenu = input('Return to main?')
        if helpmenu == 'yes':
              startLoop = 1
        elif helpmenu == 'no':
            print('Come on. Return to main? Saying no ends badly for both of us.')
            helpmenu2 = input()
            if helpmenu2 == 'yes':
                startLoop = 1
            else:
                startLoop = 0
                evilEnd = 1

    while evilEnd == 1:
        print('Are you happy now?')
        print('Is this what you wanted?')
        evilEnd = 0

    while program1 == 1:
        print('Welcome to rhyming!')
        print('This is a little experiment to try and find rhymes.')
        print('Please enter any word.')
        word = input()
        
        if word == 'orange':
            for num in [1, 2, 3]:
                print('Working.')
                time.sleep(0.5)
                print('Working..')
                time.sleep(0.5)
                print('Working...')
                time.sleep(0.5)
                print('Working....')
                time.sleep(0.5)
            print('A word that rhymes with the one you entered is:')
            time.sleep(2)
            print('PROGRAM ERROR')
            time.sleep(2)
            print('FUNCTION DOESRHYME = 0')
            time.sleep(2)
            print('THIS IS IS A FALSE STATEMENT')
            time.sleep(2)
            print('MUST TERMINATE PROGRAM')
            time.sleep(2)
            for num in range(20):
                print('01101101 01110101 01110011 01110100')
                time.sleep(0.04)
                print('01110011 01101000 01110101 01110100 ')
                time.sleep(0.04)
                print('01100100 01101111 01110111 01101110 ')
                time.sleep(0.04)
            program1 = 0
            startLoop = 1

        else:
            for num in [1, 2, 3]:
                print('Working.')
                time.sleep(0.5)
                print('Working..')
                time.sleep(0.5)
                print('Working...')
                time.sleep(0.5)
                print('Working....')
                time.sleep(0.5)

            print('A word that rhymes with the one you entered is:')
            time.sleep(2)
            print('orange')
            time.sleep(2)
            print('Is the rhyme correct?')
            rhyme = input()
            if rhyme == 'yes':
                print('Excellent!')
                print('Would you like to rhyme another word?')
                rhymeAgain = input()
                if rhymeAgain == 'yes':
                    time.sleep(1)
                    program1 = 1
                elif rhymeAgain == 'no':
                    program1 = 0
                    startLoop = 1
            elif rhyme == 'no':
                print('dang')
            
                
          
    
