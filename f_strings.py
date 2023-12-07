person = "Buro"
coins = 3

print("\n" + person + " has " + str(coins) + " coins left.") #new style


message = "\n%s has %s coins left" % (person, coins) #old style
print(message)

#.format

message = "\n{} has {} coins left.".format(person, coins)
print(message)


message = "\n{1} has {0} coins left.".format(coins , person)
print(message)


message = "\n{person} has {coins} coins left.".format(coins = coins , person = person)
print(message)

#.format with dicts
player = {"person": "Buro" , "coins":3}

message = "\n{person} has {coins} coins left.".format(**player)
print(message)


# f-string

message = f"\n{person} has {coins} coins left."
print(message)


message = f"\n{person} has {2*5} coins left."
print(message)

message = f"\n{person.lower()} has {2*5} coins left."
print(message)

message = f"\n{player['person']} has {2*6} coins left."
print(message)

#You can pass formatting options

num = 10
print(f"\n2.25 times {num} is {2.25 * num:.2f}\n")

for num in range(1,11):
    print(f"2.25 times {num} is {2.25 * num:.2f}")