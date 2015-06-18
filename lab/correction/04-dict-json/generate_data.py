import json
import random

names = []
with open('name_list.txt', 'r') as fd:
    names = fd.readlines()
    names = map(str.strip, names)

citizens = []
for name in names:
    vote = random.randint(0, 2)
    if vote == 0:
        vote = False
    else:
        vote = True
    citizen = {}
    citizen['name'] = name
    citizen['vote'] = vote
    citizen['children'] = random.randint(0, 10)
    citizens.append(citizen)

with open('votes.json', 'w') as fd:
    json.dump(citizens, fd)
