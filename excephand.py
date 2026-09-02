#for defining a return function we have to def a function
def funct1():
    try:
     a=int(input('Enter a nummber :- '))
     print(f'Multiplication Table of the given number : {a} is -')

     for i in range(1,11):
        print(f"{a}x{i} = {a*i}")
    except ValueError:
        print('Invalid Input...!')
        return 2
    except  Exception as e:
        print(e)
        return 0
    #also after the execution of return function the remain program under FINALLY will be execute
    finally:
        print("!!!......End of Program......!!!")
print(funct1())