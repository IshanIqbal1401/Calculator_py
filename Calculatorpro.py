from logo_calculator import logo
print(logo)

print('Simple  python CalCulator')

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
def calculator():
    number_1=int(input('Enter UR First digit Here '))
    number_2=int(input('Enter Second digit here '))
    for key in list_of_operations:
        print(key,end=', ')
    operation_1=input('Input the operation u want to perform  :  ')
    operation_input=list_of_operations[operation_1]
    answer=operation_input(number_1,number_2)
    print(answer)
    operation_finished=False
    while not operation_finished:
        operation=input('Do u want another operation to be performed on the previous one?\nType Y for yes and N for no ').upper()
        if operation=='Y':
            operation_2=input('Enter ur operation here')
            number=int(input('Enter ur number here '))
            operation_symbol=list_of_operations[operation_2]
            second_answer=operation_symbol(answer,number)
            print(f'Answer is {second_answer}')
        if operation=='N':
            operation_finished=True
            print('\033c')
            calculator()
        
calculator()


