def greet(name):
    print('hello'+name)
    greet2(name)
    print('getting')
    bye()

def greet2(name):
    print('how are you',name)
def bye():
    print('ok,bye')
print(greet('666'))