# birden fazla değeri tutar ortak adlada onları referans edebilirsin


users = ['Dave', 'John', 'Sara']

data = ['Dave', "42" , True]

emptylist = []

print("Dave" in users) # Dave kelimesi o list içinde var mı sorusunu kontrol eder...

print(users[0])
print(users[-2]) #sondan 2.

print(users.index('Sara')) # saranın yeri sayı olarak
print(users[0:2]) #aralık belirler (RANGE)
print(users[1:])

print(len(data)) #içinde kaç tane list elamanı olduğunu gösterir

users.append('Elsa') #list'e eleman ekleme
print(users)

users += ['Jason'] # paranteze dikkat et bundada ekleme yaptık Bütün hepsi list sonuna eklenir. Eğer parantez olmazsa her harf tek tek yazılır.
print(users)

users.extend(['Robert' , 'Jimmy']) #list'e eleman ekleme
print(users)

users.extend(data) #Bütün data list'i users list'in en sonuna eklendi
print(users)

users.insert(0,'Bob') #List başına ekleme
print(users)

users[2:2] = ['Eddie' , 'Alex'] # O yere atama
print(users)

users.remove('Bob')
print(users)

print(users.pop()) #list'in son elamanını siler
print(users)

del users[0] #girilen list elamanını silme
print(users)

data.clear() #içini temizleme
print(data)

users.sort(key=str.lower) #alfabeye göre
print(users)

nums = [1,2,3,4,6,8]

nums.reverse() #tersine çevirme
print(nums)

""" nums.sort(reverse=True)
print(nums) """

print(sorted(nums, reverse= True))
print(nums)

numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)

#Constractor List

mylist = list([1 , "Neil" , True])
print(mylist)


# Tuples içinde yer değişikliği ve list elaman değişikliği yapılamaz

mytuple = tuple(('Dave' , 42 , True))

anothertuple = (1,4,2,8)
                                #tuple () ile açılıyor unutma
print(mytuple)
print(type(mytuple))
print(type(anothertuple))

newlist =list(mytuple)
newlist.append('Neil')  #orjinal tuple değişmedi sadece extradan yenisi farklı bir tuple içinde gözüktü
newtuple = tuple(newlist) #tuple sadece iki .'lı özelliği var biri count diğeri index
print(newtuple)

print(anothertuple.count(2)) # o tuple içinde kaç tane o değerden olduğunu sayar