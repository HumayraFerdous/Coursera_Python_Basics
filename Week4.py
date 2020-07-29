#Methods
mylist=[]
mylist.append(5)
mylist.append(27)
mylist.append(3)
mylist.append(12)
print(mylist)

mylist.insert(1,12)
print(mylist)
print(mylist.count(12))

print(mylist.index(3))
print(mylist.count(5))

mylist.reverse()
print(mylist)

mylist.sort()
print(mylist)

mylist.remove(5)
print(mylist)

lastitem=mylist.pop()
print(lastitem)
print(mylist)

#Strings
scores=[("Rodney Dangerfield",-1),("Marlon Brando", 1),("You",100)]
for person in scores:
    name=person[0]
    score=person[1]
    print("Hello {}.Your score is {}.".format(name,score))

#calculating discount
origPrice=float(input('Enter the original price: $'))
discount=float(input('Enter discount percentage: '))
newPrice=(1-discount/100)*origPrice
calculation='${:.2f} discounted by {}% is ${:.2f}.'.format(origPrice,discount,newPrice)
print(calculation)

#Accumulator patterns
##
nums=[3,5,8]
accum=[]
for w in nums:
    x=w**2
    accum.append(x)
print(accum)
##
verbs = ["kayak", "cry", "walk", "eat", "drink", "fly"]
ing=[]
val=""
for word in verbs:
    val=word+"ing"
    ing.append(val)
    
print(ing)
##
numbs = [5, 10, 15, 20, 25]
newlist=[]

for item in numbs:
    newlist.append(item+5)
print(newlist) 
##
numbs = [5, 10, 15, 20, 25]
i=0
for item in numbs:
    item=item+5
    numbs[i]=item
    i+=1
               
print(numbs)
##
lst_nums = [4, 29, 5.3, 10, 2, 1817, 1967, 9, 31.32]
larger_nums=[]

for item in lst_nums:
    larger_nums.append(item*2)

print(larger_nums)
##
s=input("Enter some text: ")
ac=""
for c in s:
    ac=ac+c+"-"+c+"-"

print(ac)
##
s = "ball"
r = ""
for item in s:
   r = item.upper() + r
print(r) 

output=""

for i in range(35):
    output+='a'
print(output) 
##
a = ["holiday", "celebrate!"]
quiet = a
quiet.append("company")
print(a)