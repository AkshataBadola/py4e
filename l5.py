"""#while loops
n = 5 #n is iteration variable
while n>0:
    print(n)
    n = n-1
print("Blastoff")
print(n)

#zero trip = like a if statement

#infinite loop  - a hyperspace jump
#break statement
while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)
print('Done!')
 

#continue statement
while True:
    line = input("> ")
    if line[0] == "#":
        continue
    if line == "done":
        break
    print(line )
print("All done")

#for 
for i in [5,4,3,2,1]:
    print(i )
print("Blasstoff")

friends = ['Akku', 'Ishu', 'Unku']
for friend in friends:
    print("Happy Birthday", friend)
print('Done')

print('before')
for thing in [9, 41, 12, 3, 74, 15]:
    print(thing)
print('After')

largest = -1
print('before', largest)
for n in [9,39,20, 83,2]:
    if n > largest:
        largest = n
    print("tjr largest number is:", largest,"numner is :",n)
print(largest)


#counting
count = 0
print('before'. count)
for i in [3,5,2,53,335,65,2]:
    count = count + 1
    print(count, i)
print("After", count)

count = 0
print('before'. count)
for i in [3, 5, 2, 53, 335, 65, 2]:
    count = count + i
    print(count, i)
print("After", count)

#average
count = 0
sum = 0
print("before", count, sum)
for value in [9,3,23,24,256,25,542]:
    count = count+1
    sum = sum+value
    print(count, sum, value)
print('After',count,sum,sum/count ) """

print("before")
for value in [9, 3, 23, 24, 256, 25, 542]:
    if value > 30:
        print('lARGE NYUMBER:', value)
print("After")


found = False
print('Before', found)
for value in [9, 3, 23, 24, 256, 25, 542]:
    if value == 25:
        found = True
        print(found, value)
    print(found, value) 
print('After', found)

#smallest
smallest = None
#none type only has one value its a constant , a special datatype, its like a marker
print('before')
for n in [9, 39, 20, 83, 2]:
    if smallest is None:
        smallest = n
    elif n < smallest:
        smallest = n
    print("the smallest number is:", smallest, "and number is :", n)
print(smallest)


#exercie
num = 0
tot = 0.0
while True:
    sval = input("Enter a number: ")
    if sval == 'done':
        break
    try:
        fval = float(sval)
    except:
        print("Invalid")
        continue
    #print(fval)
    num = num+1
    tot = tot+fval
    
#print('All done')
print(tot,num,tot/num)