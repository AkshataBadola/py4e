#reserved functions
def thing():
    print("Hello")
    print("World")
    
thing()
print("Zip")
#thing() #Thus we can reuse it as many times as we want


#built in 
big = max("Hello Eorfz")
print(big)

#example
x = 5
print("Hello ")

def print_lyric():
    print("Im a studet and i am okay")
    print('i sleep all night and work all night')
    
print("yo")
x=x+4
print(x)
print_lyric()

#return values
def greet():
    return "Hello"

print(greet(), "Akshata")
greet()

#exercise
def computePay(hours,rate):
    print("in compute pay",hours,rate)
    
    if fh > fr:
        reg = rate*hours
        otp = (hours - 40.0) * (rate*0.5)
        pay = reg+otp
    else:
        pay = rate*hours
    #print("returning",pay)
    return pay

h = input("Enter hours: ")
r = input ("enter rate: ")
fh = float(h)
fr = float(r)

xp = computePay(fh,fr)

print("pay",xp)
