from numpy import std
import scipy.stats as st

tim = """boca
maison
odd eye
because
red sun
starlight
in the frozen
sahara
black or white
piri
dont light my fire
cant get you out of my mind
whistle
paradise
diamond
jazz bar
alldaylong
fairytale
sleep walking
trap
poison love
my way
fly high
good night
breaking out
eclipse
together
full moon
chase me
entrancing
silent night
cherry
scream
over the sky
beauty full
wake up
always
which a star
i miss you
endless night
rose blue
no dot
tension
daybreak
deja vu
the curse of the spider
you and i
vision
airplane
locked inside a door
new days
playground
wind blows
shadow
for
and there was no one left
no more
july 7th
4 memory
mayday
scar
wonderland
winter
reason
some love
be the future
emotion
lullaby
daydream
purple korean
break the wall
rainy day
a heart of sunflower
polaris
dear
what""".lower().split("\n")

ari = """poison love
cherry
eclipse
daybreak
cant get you out of my mind
good night 
mayday 
you and i
fly high
paradise
entrancing
wind blows
vision
new days
red sun
sahara
full moon
chase me 
rose blue
4 memory
deja vu
whistle
winter
reason
in the frozen
because
starlight
tension
silent night 
breaking out
sleep walking
together
scream
Maison
no dot
playground
black or white 
beauty full
scar 
what
fairytale
piri
the curse of the spider
trap
some love
july 7th 
and there was no one left
daydream
which a star
no more
for
a heart of sunflower
Emotion
over the sky
locked inside a door
dont light my fire
odd eye
airplane
boca
shadow
break the wall
jazz bar
always
be the future
endless night
my way
i miss you 
purple korean
rainy day
wonderland
diamond
lullaby 
polaris
dear
alldaylong
wake up""".lower().split("\n")

disco = {
    "nightmare" : [
        "chase me",
        "emotion"
    ],
    "nightmare : fall asleep in the mirror" : [
        "good night",
        "lullaby"
    ],
    "prequel" : [
        "fly high",
        "wake up",
        "sleep walking",
        "purple korean"
    ],
    "nightmare : escape the ERA" : [
        "you and i",
        "mayday",
        "which a star"
    ],
    "alone in the city" : [
        "what",
        "wonderland",
        "trap",
        "july 7th"
    ],
    "over the sky" : [
        "over the sky"
    ],
    "the end of nightmare" : [
        "piri",
        "diamond",
        "and there was no one left",
        "daydream"
    ],
    "raid of dream" : [
        "deja vu",
        "the curse of the spider",
        "silent night",
        "polaris"
    ],
    "dystopia : tree of language" : [
        "scream",
        "tension",
        "red sun",
        "black or white",
        "jazz bar",
        "sahara",
        "in the frozen",
        "daybreak",
        "full moon",
        "paradise"
    ],
    "be the future" : [
        "be the future"
    ],
    "rose blue" : [
        "rose blue"
    ],
    "dystopia : lose myself" : [
        "boca",
        "break the wall",
        "cant get you out of my mind",
        "dear"
    ],
    "dystopia : road to utopia" : [
        "odd eye",
        "wind blows",
        "poison love",
        "4 memory",
        "new days"
    ],
    "summer holiday" : [
        "because",
        "airplane",
        "whistle",
        "alldaylong",
        "a heart of sunflower"
    ],
    "apocalypse : save us" : [
        "locked inside a door",
        "maison",
        "starlight",
        "together",
        "always",
        "cherry",
        "no dot",
        "entrancing",
        "winter",
        "for",
        "beauty full",
        "playground"
    ],
    "apocalypse : follow us" : [
        "vision",
        "fairytale",
        "some love",
        "rainy day"
    ],
    "reason" : [
        "reason"
    ],
    "shadow" : [
        "shadow"
    ],
    "japanese" : [
        "breaking out",
        "my way",
        "i miss you",
        "endless night",
        "eclipse",
        "dont light my fire",
        "no more"
    ]
}

for i in range(len(tim)):
    tim[i] = tim[i].strip()
for i in range(len(ari)):
    ari[i] = ari[i].strip()

for x in tim:
    if x not in ari:
        print("wtf", x)
for x in ari:
    if x not in tim:
        print("WTF", x)

dt = {}
for i, k in enumerate(tim, 1):
    dt[k] = i

for i, k in enumerate(ari, 1):
    dt[k] = (dt[k], i)

def f(x):
    return (x[0]*x[0] + x[1]*x[1]) ** 0.5

def g(x, mean, sd):
    return 100*st.norm.cdf((mean-x)/sd)

tracknums = [f(dt[track]) for track in tim]
trackmean = sum(tracknums) / len(tracknums)
tracksd = std(tracknums)

lpdt = {}
lpnums = []
for lp in disco:
    lpdt[lp] = [0,0]
    for person in range(2):
        ratings = [dt[track][person]**2 for track in disco[lp]]
        lpdt[lp][person] = (sum(ratings) / len(ratings)) ** 0.5
    lpnums.append(f(lpdt[lp]))
lpmean = sum(lpnums) / len(lpnums)
lpsd = std(lpnums)

for lp in sorted(lpdt, key=lambda k: f(lpdt[k])):
    print(f"{g(f(lpdt[lp]),lpmean,lpsd):.2f} -> {lp}")
    for track in sorted(disco[lp], key=lambda k: f(dt[k])):
        print(f"    {g(f(dt[track]),trackmean,tracksd):.2f} -> {track} ({dt[track][0]}, {dt[track][1]})")

##for k in sorted(dt, key=lambda k: dt[k][0]):
##    print(f(dt[k]), ":", k, f"({dt[k][0]}, {dt[k][1]})")

##import random
##thing = list(tim)
##random.shuffle(thing)
##while True:
##    for track in thing:
##        print("\n\n\ntrack:", track)
##        input()
##        print("tim said", dt[track][0])
##        print("ari said", dt[track][1])
