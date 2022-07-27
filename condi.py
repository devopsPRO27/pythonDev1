# x = 12
#
# y= 12
#
#
# if x > y:
#     #true block
#     print('x is greater than y ')
# else:
#     #false block
#     print ('y is greater than x ')
#
#

# password= input('please enter your password ;) ')
#
# if password == 'Pa$$w0rd' :
#     print('hey sir have a nice day' )
# else:
#     print('nice try  you need to try harder ')

word = input('please enter the key word')

for guess in range(5):
    guess1= input('enter your guess')
    if guess1 == word:
        print('hateh esh mgiil shesh')
        break
    else:
        print('LOOOOOOOSER try again')