#while loop and for loop 

value = 1

""" while value < 10:
    print(value)
    if value == 5:
        break
    value += 1 """

while value < 10:
    value += 1
    if value == 5:
        continue # 5 ibasmaz diğerine atlar
    print(value)
else:
    print("Value is now equals to " + str(value)) #const str yaptık yoksa error veriyordu



names = ["Dave","John","Sara"]

""" for x in names:
    print(x)

for x in "Mississippi":
    print(x) """

for x in names:
    if x == "Sara":  #Sara'ya gelince duracak
        break
    print(x)

for x in names:
    if x == "Sara": #Sara atlanır
        continue
    print(x)



for x in range(5): # <5
    print(x)


for x in range(2,4):  #2-4 arası(2 dahil)
    print(x)

for x in range(0,101,5):  #kaçar kaçar artacağı son değerde belirlenir
    print(x)
else:
    print("Glad that's over")



#Nested loops

names = ["Dave","Sara","John"]
actions = ["codes","eats","sleeps"]

""" for name in names:
    for action in actions:
        print(name + " " + action + ".")"""  # Her biri 3 işide yapar  


for action in actions:
    for name in names:
        print(name + " " + action + ".") #Şimdi hepsi tek işi yapıp dönüyor