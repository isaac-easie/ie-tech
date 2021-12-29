import time as t
import os
os.system('clear')
t.sleep(2)
os.system('date')
t.sleep(2)
#introduction
print('''          ___   ___  ___  ___ ____  __     ____
        // \\ // \\ ||\\//|| || )) ||    ||   
       (( ___ ||=|| || \/ || ||=)  ||    ||== 
        \\_|| || || ||    || ||_)) ||__| ||___by isaac-easie
                                              

Warning!!\nThis tool is meant for over 18 years only''')
t.sleep(2)
print('\nPlease fill in your cred your credentials')
t.sleep(2)
mn = input('\nwhats  your name: ')
t.sleep(2)
print('\nwow,thats a nice name',mn)
t.sleep(1)
age = input('\nhow old are you?,:\n')
t.sleep(1)
if age < '18':
   print('Sorry!,you are below 18\nThis game is only for 18+')
if age > '18':
    print('\nYou quality for this game...')
    e = input('\nAre you a male or female(m/f): ')
    t.sleep(1)
    if e == 'm':
        print('\nhuh!,....nice guy.... lets gamble small,')
    if e == 'f':
         print('\nTf!...you are a girl👀,hope you are not very addicted to gambLing ')
    t.sleep(2)
    print('\nanyways,lets proceed..')
    t.sleep(1)
    print('nice meet you, ',mn)
    victimOpinion = input("\nWell, I'm Isaac. Would you like to play a game with me?(y/n)\n:")
    os.system('clear')
    t.sleep(2)
    print(''' $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$_$$$$$$$$$$$$$$$$_$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$__$$$$$$$$$$$$$$_$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$_______________$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$___________________$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$____$$$_________$$$____$$$$$$$$$$$$$
$$$$$$$$$$$$$_____$$$_________$$$_____$$$$$$$$$$$$
$$$$$$$$$$$$___________________________$$$$$$$$$$$
$$$$$$$$$$$$___________________________$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$____$$$____________________________$$$____$$$
$$$$______$$____________________________$$______$$
$$$$______$$____________________________$$______$$
$$$$______$$____________________________$$______$$
$$$$______$$____________________________$$______$$
$$$$______$$____________________________$$______$$
$$$$______$$____________________________$$______$$
$$$$______$$____________________________$$______$$
$$$$______$$____________________________$$______$$
$$$$$____$$$____________________________$$$____$$$
$$$$$$$$$$$$____________________________$$$$$$$$$$
$$$$$$$$$$$$____________________________$$$$$$$$$$
$$$$$$$$$$$$___________________________$$$$$$$$$$$
$$$$$$$$$$$$$$$$$______$$$$$$_____$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$______$$$$$$_____$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$______$$$$$$_____$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$______$$$$$$_____$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$______$$$$$$_____$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$''')
    print ('\nloading....')
    t.sleep(3)
    if victimOpinion.upper()== 'Y':
        print('\nhello...',mn)
        t.sleep(1)
        print('here is the game we are going to play!\nfor each and every wins,the pay is....')
    else:
        print('Oh!..thanks homie,\nnice fun with you,nice day!')
    
    py = int(input('enter amount for every wins: '))
    print('wow!',py)
    print('\nthats a big ammount for me.....hope i win!')
 #game section
    con = 'y'
    while con == 'y':
       a = print('\nStart thinking',mn)
       b = int(input('\nwhat is your lucky number(0,1);'))
       import random
       c = random.randint(0,1)
       print('\ngetting random number###...')
       t.sleep(3)
       if b == c:
         print('congratulations!,you win\nYour pay is: ',py,',',mn)
         print('\nChoose\n 1. to seek your payment\n 2. to cancel payment')
         #payment section
         dm = input('1/2: ')
         if dm == '1':
             print('wait....')
             t.sleep(3)
             print('contacting CEO ie-tech...')
             t.sleep(3)
             print('\nopening WhatsApp...')
             os.system('xdg-open https://wa.me/+256776515577 ')
             
         else:
              print('cancelling.....')
              t.sleep(2)
              print('payment cancelled!')
              
       else:
            print('oh!..you lose, try again')
            print('lucky number is',c)
            t.sleep(2)
       con = input('\nWould you like to replay the game(y/n): ')
       if con == 'n':
           
           print('thanks dammie\nit was nice fun with you')
           