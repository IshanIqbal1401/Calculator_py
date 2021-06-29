from logo_calculator import logo
print(logo)

print('Simple  python CalCulator')
number_1=int(input('Enter UR First digit Here '))
number_2=int(input('Enter Second digit here '))
def add_function(number_1,number_2):
    return number_1+number_2
def sub_function(number_1,number_2):
    if number_2>number_1:
        return number_2-number_1
    else:
        return number_1-number_2
def mul_function(number_1,number_2):
    return number_1*number_2
def div_function(number_1,number_2):
    if number_2>number_1:
        return number_2/number_1
    else:
        return number_1/number_2
def ddiv_function(number_1,number_2):
    if number_2>number_1:
        return number_2//number_1
    else:
        return number_1//number_2
    
list_of_operations={'+':add_function,'-':sub_function,'*':mul_function,'/':div_function,'//':ddiv_function}
for key in list_of_operations:
    print(key,end=', ')
operation=input('Input the operation u want to perform  :  ')
operation_input=list_of_operations[operation]
answer=operation_input(number_1,number_2)
print(answer)






