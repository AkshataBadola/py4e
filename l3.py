#if
x=5
if x<15:
    print("Smaller")
if x>15:
    print("Bigger")
print("Finish")

#for
for i in range(5):
    print(i)
    if i>4:
        print("Number is bigger than 4")
    print("if loop completed")
print("all done") # this basically ends the loops

#if-else
x=4
if x>4:
    print("Bigger")
else:
    print("smaller/equal to")
    
# if-elif-else
x=49
if x<42:
    print("Smaller")
elif x<50:
    print("Medium")
else:
    print("Large")
    
#try-except
str = "Helllo Akshata"
try:
    istr = int(str)
except: 
    istr = -1
    
print('First', istr)

stri = '132'
try:
    istri = int(stri)
except:
    istri = -1
    
print("Second", istri)


name = "Bob"
try:
    print("Hello")
    iname = int(name)
    print("there")
except:
    iname = -1

print("Second", iname)

#Example
n = input("Enter a number: ")
try:
    ival = int(n)
except:
    ival = -1

if ival>0:
    print("Nice Work")
else:
    print("Not a number")
    
#exercise1
xh = input("Enter Hours: ")
xr = input("Enter Rate: ")
fh = float(xh)
fr = float(xr)
xp = fh*fr

print("Pay: ", xp)

if fh>40:
    print("Overtime!!")
    reg = fh * fr
    otp = (fh -40)*(fr*0.5)
    tp = reg+otp
    print(reg, otp,tp)
else:
    print("Regular")
    
    
#exercise2
xh = input("Enter Hours: ")
xr = input("Enter Rate: ")

try:
    fh = float(xh)
    fr = float(xr)
    #xp = fh*fr
    #print("Pay: ", xp)

except:
    print("Error please enter a numberic value")
    quit()
    
print(fh,fr)
    
if fh > 40:
    #print("Overtime!!")
    reg = fh * fr
    otp = (fh - 40)*(fr*0.5)
    tp = reg+otp
    #print(reg, otp, tp)
else:
    tp = fh*fr
    #print("Regular")
