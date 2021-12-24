name=input('Type your name ==>')
print('welcome',name,'to this adventure')

answer=input('you are on a dirt road, it has come to an end you can go left or right. which would like to go? ').lower()
if answer=='left':
    answer=input('you come to a river, you can walk around it or swim accross? type to walkand swim if you want to swimaccross ==>')
    if answer=='swim':
        print('you swim accross the river and were eaten by an alligator')
    elif answer=='walk':
        print('you walked miles, ran out of water and lost the game.')
    else:
        print('Mot a valid option. you lose')
elif answer=='right':
    answer=input("You came accoss a bridge,it looks wobbly, do you want to cross it orhead back (cross/back) ? ")
    if answer=='back':
        print('You go back and lose')
    elif answer=='cross':
        answer =input ('You caross the bridge and met a stranger. do you want to talk to him(yes/no)')
        if answer=='yes':
            print('You talk to the stranger and they gift tou the treasure. you won..!!!')
        elif answer=='no':
            print('you ignore the stranger and they getoffend anf you lose')
        else:
            print('invalid option you lose')
    else:
        print('invalid option you lose')
else:
    print('invalid option you lose!')
print('THANK YOU TRYING',name)