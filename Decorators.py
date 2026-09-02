
def function(mfx):
    def decorator(*args,**kwargs):
        print("Good Morning !!")
        mfx(*args,**kwargs)
        print("Thanks for visiting ")
    return decorator

@function
def fn():
    print("Hello World!! ")
@function
def add(x,y):
    print("The sum is : ",x+y)
# function(fn)()   ------you can use this if don'want to decorate with "@function"
fn()
# function(add)(145,5)
add(145,5)