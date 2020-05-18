'''
Write a decorator function that wraps text passed to it in a html <p> tag.

'''

def html(original_function):
    def wrapper_function():
        print(f'<p>{original_function()}<p>')
    return wrapper_function

@html  
def temple():
    return 'EPSTEIN DID NOT KILL HIMSELF'
temple()

@html 
def school():
    return 'book~pencil~markers'
school()
