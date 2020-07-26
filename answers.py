#Answer_1
my_str = "MICHIGAN"
for val in my_str:
    print(val)

#Answer_2
several_things = ["hello", 2, 4, 6.0, 7.5, 234352354, "the end", "", 99]
for item in several_things:
    print(item)
for tpe in several_things:
    print(type(tpe))
    

#Answer_3
for item in str_list:
print(len(item))

#Answer_4
original_str = "The quick brown rhino jumped over the extremely lazy fox."

num_chars=0
for val in original_str:
    num_chars+=1

print(num_chars)

#Answer_5
addition_str = "2+5+10+20"
store=addition_str.split("+")
sum_val=0

for num in store:
    numstr=int(num)
    sum_val+=numstr
    
print(sum_val)

#Answer_6
week_temps_f = "75.1,77.7,83.2,82.5,81.0,79.5,85.7"
store=week_temps_f.split(",")
length=len(store)

avg=0

for temp in store:
    flstore=float(temp)
    avg+=flstore

avg_temp=avg/length
print(avg_temp)

#Answer_7
nums=range(0,68)
print(nums)

#Answer_8
original_str = "The quick brown rhino jumped over the extremely lazy fox"
store=original_str.split(" ")
num_words_list=[None]*len(store)
i=0
for item in store:
    val=len(item)
    num_words_list[i]=val
    i+=1
print(num_words_list)

#Answer_9
lett=""
for item in range(0,7):
    lett+='b'
print(lett)

#Answer_10
import turtle
def kochhop(w):
    for size in range(3):
        w.forward(20)
        w.stamp()
    return w
def describe(f):
    f.shape("turtle")
    f.pensize(4)
    return f
wn=turtle.Screen()
#s
s=turtle.Turtle()
describe(s)
s.color("Brown")
s.right(90)
kochhop(s)
#k
k=turtle.Turtle()
describe(k)
k.color("Hotpink")
k.right(45)
kochhop(k)
#l
l=turtle.Turtle()
describe(l)
l.color("Yellow")
kochhop(l)
#a
a=turtle.Turtle()
describe(a)
a.color("Green")
a.left(45)
kochhop(a)
#b
b=turtle.Turtle()
describe(b)
b.color("Blue")
b.left(90)
kochhop(b)
#z
z=turtle.Turtle()
describe(z)
z.color("Red")
z.left(135)
kochhop(z)
#y
y=turtle.Turtle()
describe(y)
y.color("Orange")
y.left(180)
kochhop(y)
#m
m=turtle.Turtle()
describe(m)
m.color("magenta")
m.right(135)
kochhop(m)