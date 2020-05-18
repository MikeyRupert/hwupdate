'''
Write a script with a function that demonstrates the use of **kwargs.

'''
def boxing(**kwargs):
    for c,w in kwargs.items():
        print(f'\nBoxing Class: {c}\n\tWeight: {w}lbs\n')
boxing(Heavyweight='200+',Light_heavyweight='168-175',Middleweight='154-160',Welterweight=147,Lightweihgt=135,Featherweight=126,Bantamweight=118,Flyweight=112)