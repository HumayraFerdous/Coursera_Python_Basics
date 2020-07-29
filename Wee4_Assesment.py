
#Assesment_2
sports = ['cricket', 'football', 'volleyball', 'baseball', 'softball', 'track and field', 'curling', 'ping pong', 'hockey']
sports.insert(2,"horseback riding")
#print(sports)

trav_dest = ['Beirut', 'Milan', 'Pittsburgh', 'Buenos Aires', 'Nairobi', 'Kathmandu', 'Osaka', 'London', 'Melbourne']
trav_dest.remove('London')
#print(trav_dest)

trav_dest = ['Beirut', 'Milan', 'Pittsburgh', 'Buenos Aires', 'Nairobi', 'Kathmandu', 'Osaka', 'Melbourne']
trav_dest.append("Guadalajara")
print(trav_dest)

winners = ['Kazuo Ishiguro', 'Rainer Weiss', 'Youyou Tu', 'Malala Yousafzai', 'Alice Munro', 'Alvin E. Roth']
winners.sort()
print(winners)

winners = ['Alice Munro', 'Alvin E. Roth', 'Kazuo Ishiguro', 'Malala Yousafzai', 'Rainer Weiss', 'Youyou Tu']
z_winners=winners
z_winners.reverse()
print(z_winners)

#Assesment_3

str1 = "I love python"
# HINT: what's the accumulator? That should go here.
chars=[]

for word in str1:
    chars.append(word)
print(chars)

#Assesment_4
ael = "python!"
app=[]

for char in ael:
    app.append(char)
print(app)

wrds = ["end", 'work', "play", "start", "walk", "look", "open", "rain", "learn", "clean"]
past_wrds=[]

for each in wrds:
    past_wrds.append(each+"ed")

print(past_wrds) 

#Final_Assesment
#1
scores = "67 80 90 78 93 20 79 89 96 97 92 88 79 68 58 90 98 100 79 74 83 88 80 86 85 70 90 100"
scores_list=scores.split(" ")
#print(scores_list)

a_scores=0

for number in scores_list:
    sc=int(number)
    if sc>=90:
        a_scores+=1
print(a_scores) 

#2
stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
org = "The organization for health, safety, and education"
org2=org.split(" ")

acro=""
for word in org2:
    if word not in stopwords:
        acro+=word[0].upper()
print(acro)

#3
stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"

st=sent.split(" ")

acro=""
for word in st:
    if word not in stopwords:
        acro+=word[0].upper()+word[1].upper()+". "
        
acro=acro[:-2]
print(acro)

#4
p_phrase = "was it a car or a cat I saw"
p_list=p_phrase.split(" ")
r_list=p_list
r_list.reverse()
wrd=""
r_phrase=""

for word in r_list:
    length=len(word)
    for _ in range(len(word)):
        length-=1
        wrd+=word[length]
        
    r_phrase+=wrd+" "
    wrd=""

print(r_phrase)
print(r_phrase==p_phrase)

#5
inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]

for item in inventory:
    i=item.split(", ")
    print("The store has {} {}, each for {} USD.".format(i[1],i[0],i[2]))

        





            


