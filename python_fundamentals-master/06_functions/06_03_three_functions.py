'''
Write a program with 3 functions. Each function must call
at least one other function and use the return value to do something.

'''
class Math_is_Fun():
    
    def __init__(self,xy1,xy2):
        self.xy1 = xy1
        self.xy2 = xy2
    
    def dis(self):
        x1,y1 = self.xy1
        x2,y2 = self.xy2
        return format(((x2-x1)**2 + (y2-y1)**2)**0.5,'1.3f')
    
    def derivative(self):
        x1,y1 = self.xy1
        x2,y2 = self.xy2
        return (y2-y1)/(x2-x1)
    
    def __str__(self):
        return (f'{self.xy1},{self.xy2} we cam find:\n\t~ distance:{self.dis()}\n\t~ derivative:{self.derivative()}.')
    


g = Math_is_Fun((10,20),(2,9))
print('would you look at that...just by entering',Math_is_Fun.__str__(g))