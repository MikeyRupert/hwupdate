'''
Demonstrate the use of the .enumerate() function.
'''
marathon_finalist = ('forrest gump','usaian bolt','flash','oprah')
for winners in enumerate(marathon_finalist,start=1):
    print(f'\t{winners[1].title()} placed {winners[0]} in this marathon.\t',end='')