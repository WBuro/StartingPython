import math

""" x = 8
print('')
if x > 10:
    print('Right on!')
else:
    print('Not Today!') 


print('Right on!') if x > 10 else print('Not Today!') """


#Data Types

#literal assignment

first = "Buro" 
last = "Eser"

""" print(type(first))
print(type(first)== str)
print(isinstance(first, str))
 """
#constructor function

""" x = str("oops")

print(type(first))
print(type(first)== str)
print(isinstance(first, str)) """

#Concatenation 

fullname =  first + " " + last
fullname +="!"

print(fullname)


#Casting a number to a string

decade = str(1980)

print(type(decade))
print(decade)

statement = "I like rock music from the "  + decade +  "s."

print(statement)

#Multiple lines

multiline = '''

Hey, how are you ?

I was just checking in.

                            All good?

'''

print(multiline)

#Escaping a special characters

sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at \\located?'

print(sentence)

#String Methods(Func)(anlık olarak değiştirir.)

print(first)
print(first.lower())
print(first.upper())

print(multiline.title())
print(multiline.replace("good","ok"))

print(len(multiline))
multiline += "                        "
multiline = "          " + multiline
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))  #Soldakileri çıkartır
print(len(multiline.rstrip()))  #Sağdakileri çıkartır

#Build A Menu

title = "menu".upper()

print(title.center(20 , "="))

print("Coffee".ljust(16, ".")+ "$1".rjust(4))
print("Muffin".ljust(16, ".")+ "$3".rjust(4))
print("Cheesecake".ljust(16, ".")+ "$5".rjust(4))

print("")



#string index values

print(first[1]) #second v
print(first[-1]) #last v
print(first[1:-1])
print(first[1:])

#Some methods return boolean data

print(first.startswith("D"))  #onunla mı başlıyor
print(first.endswith("Z"))    #onunla mı bitiyor

# Boolean data types

myvalue = True
x = bool(False) 
print(type(x))
print(isinstance(myvalue , bool))


#Numeric data types

price = 100
best_price = int(55)


#float

gpa = 3.28
y = float(3.14)

#complex type

z = 5 + 3j
print(z.real) #karmaşık sayılar
print(z.imag)

# Built-in functions for numbers

print(abs(gpa))
print(abs(gpa * -1))

print(round(gpa))

print(round(gpa, 1))



print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))


#casting a string to a number

zipcode = "10001"
zip_value = int(zipcode)
print(type(zip_value))