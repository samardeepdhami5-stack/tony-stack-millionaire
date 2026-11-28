# print ("hello sam")
# print ("sam")
# comment
# print("Samar")
# wefhfewhyu
# hjsacbejkb
# print("python","is","langunage",sep= "-");

# print("python")
# print("is")
# print("langunage")
# name = "sam"
# age = 23
# height = 5.7
# complex1 = 2+2j
# is_student = True

# print(name,age,height,is_student, sep="+")
# print("hello")
# print ("my name is samar")

# print(type(name))
# print(type(age))
# print(type(height))
# print(type(complex1))

# a=10
# b=11
# c=30
# a=b=10;
# a,b,c=10,11,30

# print(a,b,c)

# temp =0;
# temp =a;
# a=b
# b=temp

# print(a,b)

# x,y=50,50
# x=x+y;
# y=x-y;
# x=x-y;
# print(x,y)

# str1 = bool("34");
# print(type(str1),str1)

# str1 = "25";
# int1=int(str1)
# float1= float(str1)
# str2 = str(float1)
# bool1 =bool(1);

# print(str1,int1,float1,str2,bool1)

# str1 = "25";
# int1=int(str1)
# float1= float(str1)
# str2 = str(float1)
# bool1 =bool(());

# print(str1,int1,float1,str2,bool1)

# print(10-20)
# print(20+30)
# print(40/30)
# print(30%6)
# print(2//3)
# print(3**4)
# print(3*8)

# print(10==10)
# print(10!=10)
# print(10>10)
# print(10<10)
# print(10>=10)
# print(10<=10)

# x1=10
# x1+=20
# x1-=5
# x1*=2
# x1/=2
# x1//=2
# x1%=2
# x1**=4
# print(x1)

# print("a" in "cat");
# print("a" not in "cat");

# pet ="cat"
# checkVal = "c"
# print(checkVal in pet);

# print(10+5*2)
# print(20/5+3)
# print((10+5)*2)
# print(2+3**2)

# print("sam")
# print("Delhi")

# print(1, 2, end=" ")
# print(3)

# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))
# print("Sum:", a + b)
# print("Difference:", a - b)
# print("Product:", a * b)

# a = 10
# b = 20
# a, b = b, a
# print(a, b)  # 20 10

# radius = float(input("Enter radius: "))
# area = 3.14159 * (radius ** 2)
# print("Area:", area)

# celsius = float(input("Enter temperature in Celsius: "))
# fahrenheit = (celsius * 9 / 5) + 32
# print("Fahrenheit:", fahrenheit)

# age = 25
# has_license = True
# if age >= 18 and has_license:
#     print("You are allowed to drive.")  

# is_weekend = True
# is_holiday = False
# if is_weekend or is_holiday:
#     print("You can sleep in today!")  

# is_raining = False
# if not is_raining:
#     print("Let's go for a walk.")  

s = 'Hello my name is sam'
newstr= s.strip()
# print(s)
# print(s.strip());
# print(s.lower());
# print(s.strip().lower().upper())
# print(s.title());
# print(s.replace("sam","sami"));
# print(s.split());
# print(s.find('python'));
# print(newstr.find('s'));
# print(newstr.count('s'));
# print(newstr.startswith("f"));
# print(newstr.endswith("s"));
# print(len(newstr));

name, marks = "sam" , "20"
# print(name,marks); 
# print(f'{name} has scored {marks}');
# print('{} scored {}'.format(name,marks));
# print('%s scored %d'% (name,marks));

# escape charactors

# \n new line
# \t tab line
# str="Samardeep\\dhami"
# print(str)

# immutability
# str1="dog";
# # str1[0] = "p"
# str2 =str1;
# str1="dog1234"
# print(str1,str2)

# print('python'[1:2]);
# print('school'[::-1]);

# str3= "123";
# print(str3==str3[::-1])

# str3= "121";
# print(str3==str3[::-1])

# how we can get input

# marks =int(input("enter any no"))
# print(type(marks))

# control flow 

# age=int(input("Enter your age"))

# if age>=18:
#     print("you are eligible for vote")
# else:
#     print("you are not eligible")    

# m1 = float(input("Enter marks for Subject 1: "))
# m2 = float(input("Enter marks for Subject 2: "))
# m3 = float(input("Enter marks for Subject 3: "))
# m4 = float(input("Enter marks for Subject 4: "))
# m5 = float(input("Enter marks for Subject 5: "))

# total_marks = m1 + m2 + m3 + m4 + m5
# percentage = (total_marks / 500) * 100

# print("Total Marks:", total_marks, "/ 500")
# print(f"Percentage: {percentage:.2f}%")

# if percentage >= 90:
#     print("Grade: A+")
# elif percentage >= 75:
#     print("Grade: A")
# elif percentage >= 60:
#     print("Grade: B")
# elif percentage >= 33:
#     print("Grade: C (Pass)")
# else:
#     print("Result: Fail")

# let num = 10

# if num == 0:
#     print("num is zero")
# elif num < 0:
#     print("-ve");
# else:
#     print("+ve")

# num1=10;
# num2=20;

# if num1 > num2:
#     print(f"{num1} is greater")
# else:
#     print(f"{num2} is greater")

# a,b,c=10,20,15;

# if a > b and a > c:
#     print("a is greatest");
# elif b>a and b>c:
#     print("b is greatest");
# else:
#     print("c is greatest");

# age=int(input("18"))
# if age < 13:
#     print ("you are a child.")
# elif age >=13 and age < 20:
#     print("you are teenager")
# else:
#     print("you are a senior citizen")

# num1 = int(input("Enter first number: "))
# operator = input("Enter operator (+, -, *, /): ").strip()
# num2 = int(input("Enter second number: "))

# if operator == "+":
#     print("Result:", num1 + num2)
# elif operator == "-":
#     print("Result:", num1 - num2)
# elif operator == "*":
#     print("Result:", num1 * num2)
# elif operator == "/":
#     if num2 != 0:
#         print("Result:", num1 / num2)
#     else:
#         print("Error: Cannot divide by zero.")
# else:
#     print("Invalid operator! Please choose +, -, *, or /.")

# num = int(input("Enter a number: "))
# if 10 <= num <= 99:
#     print("num is a two-digit number.")
# elif 100 <= num <= 999:
#     print("num is a three-digit number.")
# elif 1000 <= num <= 9999:
#     print("num is a four-digit number.")
# else:
#     print("num is not a two-digit, three-digit, or four-digit number.")

# a, b, c = 20, 10, 30
# middle = sorted([a, b, c])[1]
# print(middle) 

# a=int(input("enter first number"))
# b=int(input("enter second number"))
# c=int(input("enter third number"))
# if a>b and a<c or a<b and a>c:
#     print("Middle number is",a)
# elif b>a and b<c or b<a and b>c:
#     print("Middle number is",b)
# else:
#     print("Middle number is",c)

# a = input("Enter a character: ")
# if len(a) != 1:
#     print("Please enter a single character.")
# elif a.isupper():
#     print("Uppercase letter")
# elif a.islower():
#     print("Lowercase letter")
# elif a.isdigit():
#     print("Digit")
# else:
#     print("Special character")

# salary = int(input("Enter your salary"))
# age = int(input("Enter your age"))
# if salary>=25000 and age>=21 and age<=60:
#     print("You are eligible for a loan")
# else:
#     print("You are not eligible for a loan")

# units = float(input("Enter units: "))

# if units <= 100:
#     bill = units * 5
# elif units <= 200:
#     bill = 500 + (units - 100) * 7
# else:
#     bill = 1200 + (units - 200) * 10

# print(f"Total Bill: ₹{bill:.2f}")

# print("hi i am samar")

# while loop
# a = 10
# d = 0
# while d < 10:
#     print("hi i am samar",d);
#     d+=1

# for loop
# for i in range(1,10,2):
#     print(i)

# reverse loop
# for i in range(10,0,-1):
#     print(i)

# break and continue
# for i in range (10):
#     print(i)
#     if(i==5):
#         break

# for i in range (10):
#     if(i==5):
#         continue
#     print(i)

# question
# for i in range(1, 11):
#     print(i)

# for i in range(10, 0, -1):
#     print(i)

# for i in range(2, 101, 2):
#     print(i)

# for i in range(1, 101, 2):
#     print(i)

# n = int(input("Enter N: "))
# total = 0

# for i in range(1, n + 1):
#     total += i
# print("Sum:", total)

# n = int(input("Enter N: "))
# total = 0
# for i in range(2, n + 1, 2):
#     total += i
# print("Sum of even numbers:", total)

# n = int(input("Enter N: "))
# total = 0
# for i in range(1, n + 1, 2):
#     total += i
# print("Sum of odd numbers:", total)

# num = int(input("Enter a number: "))
# for i in range(1, 11):
#     print(f"{num} x {i} = {num * i}")

# for num in range(1, 11):
#     print(f"--- Table of {num} ---")
#     for i in range(1, 11):
#         print(f"{num} x {i} = {num * i}")

# num = int(input("Enter a number: "))
# fact = 1
# for i in range(1, num + 1):
#     fact *= i
# print("Factorial:", fact)

# print 1 to 10
# for i in range(10,0,-1):
#     print(i)

# for i in range(1,11):
#     print(i)

# for i in range(1,10):
#     if i%2==0:
#         print(i)

# odd
# for num in range(1, 101, 2):
#   print(num)

#even
# for num in range(2, 101, 2):
#     print(num)
  
# input 5
# n=int(input("num"));
# total=0;
# for i in range("1,n+1"):
#     total += i
# print("total",total)

# for i in range(1,11):
#   print(f"{n} x {i} = {n"i"}")

# n = 5  
# factsum = 1
# for i in range(1, n + 1):
#   factsum *= i  
# print(factsum)  


# n = int(input("Enter a number: ")) 
# n = abs(n)                        
# count = 0
# if n == 0:
#     count = 1
# else:
#     while n > 0:
#         count += 1
#         n //= 10                   
# print("num of digit:", count)

# 123 ->321
# reverse digit
# n = int(input("enter the no"))
# reverse = 0
# while n > 0:
#     digit = n % 10
#     reverse = reverse * 10 + digit
#     n //= 10
# print(reverse)

#palindrome
# orignal==reverse
# num = int(input("Enter a number: "))
# if num < 0 or (num % 10 == 0 and num != 0):
#     print(False)
# else:
#     reversed_num = 0
#     original = num

#     while num > 0:
#         digit = num % 10
#         reversed_num = reversed_num * 10 + digit
#         num //= 10

#     print(original == reversed_num)

#prime no
# no = int(input("Enter any number"))
# if no%no or no%1==0:
#     print("Number is not prime")
# else:
#     print("Number is prime")

# find the largest number 
# num = 1294
# largest = 0

# while num > 0:
#     digit = num % 10
#     if digit > largest:
#         largest = digit
#     num //= 10

# print("largest digit", largest)

#Fibonacci series

# num=5
# a=0;
# b=1;
# for i in range(num):
#     print(a,end=" ");
#     a,b = b,a+b

#nested loops
# for min in range(0,2):
#     print("mins",min)
#     for sec in range(1,61):
#         print("secs",sec)

# for min in range(0,3):

#     for sec in range(0,3):
#         print("X",end=" ")
        
#     print("\n")

# triangle
# for outer in range(1,6):
#     for inner in range(outer):
#         print("X",end=" ")
#     print()

for outer in range (1,6):
    for inner in range (outer):
        print(f"{outer}",end="")
        print() 