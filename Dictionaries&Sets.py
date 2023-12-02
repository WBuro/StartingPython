# Dictionaries (They storage the data values in key value pair)(Look like JS Objects)

band = {

"vocals" : "Plant",
"guitar" : "Pager",
}

band2 = dict(vocals="Plant", guitar="Page") #const dict

#Aynı hepsi

print(band)
print(band2)


#Access items

print(band["vocals"])
print(band.get("guitar"))

#list all keys

print(band.keys())

#list all values

print(band.values())

#list of key/value pairs as tuples
print(band.items())

#verify a key exists
print("guitar" in band)
print("triangle" in band)

#Change values
band["vocals"] = "Coverdale"
band.update({"bass": "JPJ"})

print(band)

#Remove items
print(band.pop("bass"))
print(band)

band["drums"] = "Bonham"
print(band)

print(band.popitem()) #deletes last item and returns it tuple
print(band)

#Delete and clear

band["drums"] = "Bonham"
del band["drums"]
print(band)

band2.clear()
print(band2)

del band2

#Copy Dicts

#Wrong way make a copy 

""" band2 = band #create a reference
print("Bad copy!")
print(band2)
print(band)

band2["drums"] = "Dave"
print(band) """

band2 = band.copy()
band2["drums"] = "Dave"
print("Good copy!")
print(band)
print(band2)

# or use the dict() constructor func

band3 = dict(band)
print("Good copy!")
print(band3)

#Nested Dicts

member1 = {
    "name" : "Plant",
    "instrument": "Vocals"
}

member2 = {
    "name" : "Page",
    "instrument": "Guitar"
}

band = {
    "member1" : member1,
    "member2": member2
}

print(band)
print(band["member1"]["name"]) #katmanlara indik


#Sets

nums = {1,2,3,4} #set

nums2 = set((1,2,3,4)) #const set

print(nums)
print(nums2)

# No duplicate allowed

x = {1,2,2,6}
print(x)

# True is dupe of 1, False is a dupe of zero

y = {1, True, 2, False,3,4,0}
print(y)

#check if a value is in a set
print(2 in nums)

#but you cannot refer to an element in the set with an index position or a key

#Add a new element to a set

nums.add(10)
print(nums)

#Add elements from one set to another
morenums = {5,6,7}
nums.update(morenums)
print(nums)

#you can use update with lists, tuples, and dicts, too

#merge two sets to create a new set
one = {1,2,3}
two = {5,6,7}

mynewset = one.union(two)
print(mynewset)

#Keep only the duplicates
one = {1,2,3}
two = {2,3,4}

one.intersection_update(two)
print(one)

#Keep everything except the duplicates
one = {1,2,3}
two = {2,3,4}

one.symmetric_difference_update(two)
print(one)