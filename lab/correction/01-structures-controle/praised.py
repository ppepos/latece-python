from poem import poem


count = 0
for word in poem.split():
    if word.lower().find('rao') != -1:
        count += 1

print 'Rao, our Grand Leader has been praised %s times!' % count
