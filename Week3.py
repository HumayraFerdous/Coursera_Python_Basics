"""Examples"""
percent_rain = [94.3, 45, 100, 78, 16, 5.3, 79, 86]
resps=[]
for item in percent_rain:
    if item>=90:
        resps+=["Bring an umbrella."]
    elif item>=80 and item<90:
        resps+=["Good for the flowers?"]
    elif item>=50 and item<80:
        resps+=["Watch out for clouds!"]
    else:
        resps+=["Nice day!"]
        
print(resps)


words = ["water", "chair", "pen", "basket", "hi", "car"]
num_words=0
for item in words:
    val=len(item)
    if val>3:
        num_words+=1
print(num_words)


words = ["adopt", "bake", "beam", "confide", "grill", "plant", "time", "wave", "wish"]
past_tense=[]

for item in words:
    if item[-1]=='e':
        past_tense+=[item+'d']
    else:
        past_tense+=[item+'ed']       
print(past_tense)

"""Graded Assessment"""
# 1
rainfall_mi = "1.65, 1.46, 2.05, 3.03, 3.35, 3.46, 2.83, 3.23, 3.5, 2.52, 2.8, 1.85"
rainfall=rainfall_mi.split(", ")
flt_rainfall=[]

for item in rainfall:
    val=float(item)
    flt_rainfall+=[val]

num_rainy_months=0

for nums in flt_rainfall:
    if nums>3.0:
        num_rainy_months+=1

print(num_rainy_months)

#2
sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"
sentence_list=sentence.split(" ")
#print(sentence_list)

same_letter_count=0

for item in sentence_list:
    if(item[0]==item[-1]):
        same_letter_count+=1
        
print(same_letter_count)

#3
items = ["whirring", "wow!", "calendar", "wry", "glass", "", "llama","tumultuous","owing"]

acc_num=0

for num in items:
    if 'w' in num:
        acc_num+=1
        
print(acc_num)

#4
sentence = "python is a high level general purpose programming language that can be applied to many different classes of problems."
sentence_list=sentence.split(" ")
#print(sentence_list)

num_a_or_e=0

for word in sentence_list:
    if 'a' in word:
        num_a_or_e+=1
    elif 'e' in word:
        num_a_or_e+=1

print(num_a_or_e)

#5
s = "singing in the rain and playing in the rain are two entirely different situations but both can be fun"
vowels = ['a','e','i','o','u']

num_vowels=0

for word in s:
    if word in vowels:
        num_vowels+=1
print(num_vowels)


