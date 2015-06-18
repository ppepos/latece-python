import json

# Generate the list of all Citizens of Rao who require eviction from the
# Kingdom of Rao! You can base your decisions on the results of the last
# elections in the votes.json file. You must also find how many children
# will be left orphaned.

with open('votes.json', 'r') as fd:
    votes = json.load(fd)

evicted = []
orphaned = 0
for citizen in votes:
    if citizen['vote'] == False:
        evicted.append(citizen['name'])
        orphaned += citizen['children']

print evicted
print orphaned
