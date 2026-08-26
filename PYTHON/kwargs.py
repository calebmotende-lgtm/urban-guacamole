#testing kwargs

#List of kwargs
def myKwargs(**kwargs):
    print(kwargs)

#scenario 1


#scenario a=23,b=3-, =? {a:23,b:30}
myKwargs(a=23,b=30)

#scenario 3
#name="Samson" email= "Samson@gmail.com"
#myKwargs({"Name":"Samson",})
myKwargs(name="Samson",email="Samson@gmail.com",dict={"a":"a"})

def area_rectangle(length,width):
    area= length*width
    print(f"For rectangle with length {length} and width {width} area is {area}")

    #option 1...calling it directly with args
area_rectangle(5,2) #args
width=4
length=39
area_rectangle(length,width) #args
area_rectangle(width=width,length=length)#kwargs

#option 3 you with kwargs
area_rectangle(width=10,length=55)

#you have to match the parameter manmes with arguments
area_rectangle(width=10,length=55)
#area_rectangle(40)
    
