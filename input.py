

# write a code that receives the name and the age of the user
# and print the next line ::
# hiii  , <username>  you are <age> years old

name = input('please enter your number : ')
age = input('please enter your age : ')


print('hiii , ' + name + ' your are ' + age + " years old " )
print(f'hiii , { name } your are { age }  years old ' )


# write a program that receives from the user
#the number of the children they have
# the numbers of pizzas they ordered
# and print how many slices each of the kids will get
# and how many leftovers


#print( type(kids))
kids = int(input('how many kids you have ? : '))
pizzas = int(input('how many pizzas you ordered : '))
#print( type(kids))

total_slices= pizzas * 8
slices_per_kid = total_slices // kids
left_overs = total_slices % kids

print('silces per kid :' + str(slices_per_kid))
print(f'leftovers : { left_overs }')
