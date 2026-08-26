age=20

#if conditions

if age>18:
    print("You can drink")
    print("Something else")
    if age == 23:
        print("This is awesome")
        print("Another line")
#else if in js
elif age<44:
    print("You are not that young")
else:
    print("Last else")

#for(let i=0; i<100; i++) {0-99}

#range(start,stop,step)
for i in range(0,200,1):
    print("I is ",i)

#for(let 1=0; i<ar.length; i++) {0-99}
ar=[1,2,3,4,5]
for i in range(0,len(ar)):
    single_item=ar[i]
    print(single_item)

#for(let singleitem of arr)
for single_item in ar:
    print("Single item is ", single_item)


#while loop
i=0
while i<10:
    k=k+1
    print("K is ",k)