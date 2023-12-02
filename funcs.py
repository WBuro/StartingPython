#def = define

def hello():
    print("Hello world") #burada define ettik çağırmadık


hello() # çağırma

#placeholder = parameters

def sum(num1, num2): #param's can't change 
    print(num1 + num2)

sum(2,3) #passing argument but arguments can change
sum(1,9) 
sum(200,30) 


def sum(num1, num2): 
    return num1 + num2

total = sum(2,3)
print(total)


def sum(num1 = 10 , num2 = 12): # we gave default values in case we forget giving arguments later
    if(type(num1) is not int or type(num2) is not int):
        return 
    return num1 + num2

total = sum() # == none true ya da false değildir
print(total)


def multiple_items(*args): #for unknown amount of arguments(args genel ad yıldız * zorunlu)
    print(args)
    print(type(args))

multiple_items("Dave","John","Sara")

def mult_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))


mult_named_items(first = "Dave",
                 last ="Gray")
