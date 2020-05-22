'''
- Write a script with three classes that model everyday objects.
- Each class should have an __init__ method that sets attributes
    to a default value if values are not passed.
- Create at least two objects of each class using the __init__ method.
- Each object should have at least three attributes.
- Each class should have at least two class attributes.
- Create a print method in each class that prints out the attributes
    in a nicely formatted string.
- Include a __str__ method in each class.
- Overload the __add__ method in one of the classes so that it's possible
    to add attributes of two instances of that class using the + operator.
- Once the objects are created, change some of the attribute values.

Be creative. Have some fun. :)
Using objects you can model anything you want.
Cars, animals, poker games, sports teams, trees, beers, people etc...


'''
class Tree(object):
    def __init__(self,env):
        self.env = env
        print((f'if you enter {env["x"]} for x and {env["y"]} for y in equation 1:{equation1}={equation1.eval(env)}'),(f'\nif you enter {env["x"]} for x and {env["y"]} for y in equation 2:{equation2}={equation2.eval(env)}'))
        
class Multiply(Tree):
    def __init__(self,l,r):
        self.l = l 
        self.r = r
        
    def __str__(self):
        return "(" + str(self.l) + "*"+ str(self.r) +")"
    
    def eval(self,env):
        return self.l.eval(env) * self.r.eval(env)
    
class Addition(Tree):
    def __init__(self,l,r):
        self.l = l 
        self.r = r
        
    def __str__(self):
        return "(" + str(self.l) + "+"+ str(self.r) +")"
    def eval(self,env):
        return self.l.eval(env) + self.r.eval(env)

class Constant(Tree):
    def __init__(self,value):
        self.value = value
        
    def __str__(self):
        return str(self.value)
        
    def eval(self,env):
        return self.value

class Variables(Tree):
    def __init__(self,name):
        self.name = name
        
    def __str__(self):
        return self.name
        
    def eval(self, env):
        return env[self.name]
    

equation1 = Multiply(Constant(4),Addition(Variables("y"),Variables("x")))
equation2 = Addition(Multiply(Constant(5),Variables("y")), Variables("x"))
(Tree(env = { "x":3, "y": 10}))  
