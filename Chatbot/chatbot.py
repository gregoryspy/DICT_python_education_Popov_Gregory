print ("Hello! my name is John")
print ("I was created in 2021")
what = input ("Please, remind my your name:")
print ("What a great name you have," + str(what))
print ("Let me guess your age.")
print("Enter remainders of dividing your age by 3,5 and 7")
q = input ("First:")
w = input ("Second:")
e = input ("Third:")
age = ((int(q) / 3 * 70 + int(w) / 5 *21 + int(e) / 7 * 15)%105)
print ("Your age is " + str(age) + "; that a good time to start programming!")
number = float (input ("Now i will prove to you that i can count to any number you want:") )
i = 0
while i < 10:
    print(str(i) + "!")
    i = i + 1
    if i == number :
        break
print("Completed, have a nice day!")
print ("Let's test your programming knowledge.")
print ("Why do we use methods?")
a = print("1. To repeat a statement multiple times.")
b = print("2. To decompose a program into several smallsubroutimes.")
c =  print("3. To deternine the execution of a program.")
d = print("4. To interrupt the execution of a program.")
j = float(input("Your answer(1,2,3,4):") )
if j == 1 :
    print ("Please, try again.")
if j == 2 :
    print ("Completed, have a nice day!")
    print ("Congretulations, have a nice day!")
    'break'
if j == 3 :
    print ("Please, try again.")
if j == 4 :
    print ("Please, try again.")




