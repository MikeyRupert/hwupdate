'''
Improve the decorator from the previous exercise by allowing it to take
any specified HTML tag as an input - making it more general.

'''
def html_unwrapper(html_text):
    def wrapper():
        w = html_text().strip('<p>')
        print(w)
    return wrapper

@html_unwrapper 
def html():
    return '<p>60% of the time this works everytime<p>'
html()