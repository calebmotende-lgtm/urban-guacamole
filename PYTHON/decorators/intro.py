
def my_deco(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func() #try when comments are on and off
        print("Something is happening after the function is called.")
    return wrapper

def hello():
    print("Hello World function executes!")
    print("Hello World!")

@my_deco
def french_hello():
    print("Hello function executes!")
    print("Bonjour World!")
    

