""" name = "Buro" #Global Scope

def greeting():
    print(name) #func'lar local scope özelliği taşır
                #local scope'u func dışında çağıramazsın

greeting()


def x(name): #Ama eğer param atarsak ve onu çağırırsak global scope işlevini yitirir
    color ="blue"
    print(color)
    print(name) 

x("John")

def another():
    greeting("Dave")

another() """

name ="Dave"
count = 1

def another():
    color ="green"
    global count #bu kadar uzun çunkü error verir
    count += 1
    #count = 2
    print(count)

    def greeting(name):
        nonlocal color
        color = "red"
        print(color)
        print(name)
    
    greeting("Dave")

another()